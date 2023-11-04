import pandas as pd
import string
import spacy
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB

# from tensorflow import keras
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from apps.review.models import Review


class ProductRecommendationView(APIView):
    def get(self, request, format=None):
        products = (
            Product.objects.values(
                "id", "name", "price", "rating", "description", "image_product"
            )
            .filter(countInStock__gt=0)
            .order_by("?")
        )
        reviews = Review.objects.values("product_id", "comment", "rating")

        products_df = pd.DataFrame.from_records(products)
        reviews_df = pd.DataFrame.from_records(reviews)

        # Load the spaCy English language model
        nlp = spacy.load("en_core_web_sm")

        # Function to preprocess text using spaCy for tokenization
        def text_preprocessing(text):
            text = text.lower()
            text = "".join([char for char in text if char not in string.punctuation])
            doc = nlp(text)
            tokens = [
                token.text
                for token in doc
                if token.text not in stopwords.words("english")
            ]
            stemmer = SnowballStemmer("english")
            tokens = [stemmer.stem(word) for word in tokens]
            return " ".join(tokens)

        # Create and fit the TF-IDF vectorizer for sentiment analysis
        tfidf_vectorizer_sentiment = TfidfVectorizer(max_features=1000)
        tfidf_vectorizer_sentiment.fit(reviews_df["comment"])

        # Preprocess the review texts and analyze sentiment
        preprocessed_texts = []
        sentiments = []

        for review_text in reviews_df["comment"]:
            preprocessed_text = text_preprocessing(review_text)
            preprocessed_texts.append(preprocessed_text)

        # Transform review text using the sentiment analysis vectorizer
        X_review_text_tfidf = tfidf_vectorizer_sentiment.transform(preprocessed_texts)
        X_review_text_tfidf = X_review_text_tfidf.toarray()

        # Load the saved sentiment analysis model
        sentiment_model = MultinomialNB()
        sentiment_model.fit(
            X_review_text_tfidf, reviews_df["rating"]
        )  # Training with actual ratings

        # Analyze sentiment using the sentiment analysis model
        predicted_sentiments = sentiment_model.predict(X_review_text_tfidf)

        sentiment_labels = ["positive", "negative"]
        predicted_labels = [
            sentiment_labels[np.argmax(sentiment)] for sentiment in predicted_sentiments
        ]

        # Add the preprocessed text and sentiment to the reviews DataFrame
        reviews_df["preprocessed_text"] = preprocessed_texts
        reviews_df["sentiment"] = predicted_labels

        # Merge the 'reviews' and 'products' DataFrames based on 'product_id'
        merged_df = pd.merge(
            reviews_df, products_df, left_on="product_id", right_on="id"
        )

        # Calculate the average review rating for each product
        average_review_ratings = (
            merged_df.groupby("id")["rating_x"].mean().reset_index()
        )
        products_df["average_review_rating"] = average_review_ratings["rating_x"]

        products_df["combined_rating"] = (
            products_df["rating"] + products_df["average_review_rating"]
        ) / 2

        # Sort products by highest combined rating and lowest price
        recommended_products = products_df.sort_values(
            by=["combined_rating", "price"], ascending=[False, True]
        )

        recommended_products = recommended_products.rename(
            columns={"combined_rating": "rating"}
        )

        recommended_products["preprocessed_text"] = merged_df["preprocessed_text"]
        recommended_products["sentiment"] = merged_df["sentiment"]

        # Prepare the response data
        recommended_products_data = recommended_products[
            [
                "id",
                "name",
                "price",
                "image_product",
                "description",
                "rating",
                "preprocessed_text",
                "sentiment",
            ]
        ][:10]

        recommended_products_json = recommended_products_data.to_dict(orient="records")

        return Response(recommended_products_json, status=status.HTTP_200_OK)
