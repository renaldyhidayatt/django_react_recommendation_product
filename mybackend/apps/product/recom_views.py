import pickle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd


class RecomProductListView(APIView):
    def get(self, request):
        try:
            with open("recommended_products.pkl", "rb") as file:
                loaded_recommended_products = pickle.load(file)[:10]

            loaded_recommended_products_list = loaded_recommended_products.to_dict(
                orient="records"
            )

            return Response(
                loaded_recommended_products_list,
            )

        except FileNotFoundError:
            return Response(
                {"message": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )
