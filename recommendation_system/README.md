# Analisis Sentimen pada Data Ulasan Produk dengan Naive Bayes

Ini adalah contoh implementasi analisis sentimen menggunakan metode Naive Bayes pada data teks dalam bahasa Indonesia. Prosesnya dilakukan dalam beberapa tahap:

## Import Library

- `pandas`: Digunakan untuk manipulasi dan analisis data, khususnya dalam format DataFrame.
- `nltk`: Natural Language Toolkit adalah library pemrosesan bahasa alami yang digunakan untuk tokenisasi dan penghapusan stopwords.
- `re`: Library untuk ekspresi reguler, digunakan untuk membersihkan teks dari URL, tanda pagar, dan sebagainya.
- `requests`: Untuk mengambil data teks dari URL, seperti daftar stopwords tambahan.
- `matplotlib.pyplot`: Library untuk membuat visualisasi grafik, digunakan untuk visualisasi data sentimen.
- `sklearn`: Library untuk machine learning, digunakan untuk pembagian data latih dan uji, ekstraksi fitur TF-IDF, label encoding, dan evaluasi model.
- `TfidfVectorizer`: Dari sklearn, digunakan untuk mengubah teks ke representasi vektor menggunakan metode TF-IDF.
- `LabelEncoder`: Dari sklearn, digunakan untuk mengkodekan label sentimen menjadi angka.
- `accuracy_score`: Dari sklearn, digunakan untuk menghitung akurasi model.
- `classification_report`: Dari sklearn, digunakan untuk membuat laporan klasifikasi berdasarkan hasil prediksi.
- `MultinomialNB`: Dari sklearn, digunakan untuk melatih model klasifikasi sentimen dengan algoritma Naive Bayes.
- `word_tokenize`: Dari nltk, digunakan untuk tokenisasi kata.
- `WordCloud`: Library untuk membuat visualisasi word cloud.
- `StemmerFactory`: Dari Sastrawi, digunakan untuk stemming kata dalam bahasa Indonesia.
- `pickle`: Library untuk menyimpan dan membaca objek Python.

## Membaca Data
Data produk dan ulasan dibaca dari file CSV.

## Visualisasi Data Sentimen
Data sentimen pada ulasan divisualisasikan dalam bentuk grafik batang.

## Word Cloud Positif dan Negatif
Dilakukan word cloud untuk sentimen positif dan negatif untuk melihat kata-kata yang paling umum muncul dalam ulasan tersebut.

## Text Cleaning
Proses pembersihan teks, termasuk menghilangkan URL, tanda pagar (#), mention handle pengguna (@), tanda baca, dan mengonversi teks menjadi huruf kecil.

## Custom Stopword List
Sebuah daftar kata-kata stopword khusus untuk bahasa Indonesia diunduh dari beberapa sumber dan digabungkan menjadi satu daftar stopword.

## Remove Stopwords
Menghilangkan stopword dari teks ulasan.

## Stemming and Lemmatization
Melakukan stemming dan lemmatization pada teks ulasan menggunakan library Sastrawi untuk bahasa Indonesia.

## Tokenization
Melakukan tokenisasi pada teks ulasan.

## Balancing the Dataset
Mengequilibrasi dataset dengan mengambil sampel jumlah ulasan positif dan negatif yang sama.

## Encoding Sentiment Labels
Mengkodekan label sentimen menjadi angka.

## Splitting the Dataset
Membagi dataset menjadi data latih dan data uji.

## TF-IDF Vectorization
Melakukan vektorisasi menggunakan metode TF-IDF.

## Training a Multinomial Naive Bayes Model
Melatih model klasifikasi sentimen menggunakan algoritma Multinomial Naive Bayes.

## Making Predictions
Melakukan prediksi sentimen pada data uji.

## Evaluating the Model
Menghitung akurasi dan membuat laporan klasifikasi berdasarkan hasil prediksi.

## Contoh Prediksi
Melakukan prediksi sentimen pada beberapa contoh ulasan.

## Merging Data
Menggabungkan data ulasan dan data produk berdasarkan kolom "product".

## Menghitung Rating Rata-Rata
Menghitung rating rata-rata berdasarkan ulasan.

## Merging Rating Rata-Rata ke Data Produk
Menyatukan rating rata-rata kembali ke dataframe produk.

## Menghitung Rating Gabungan
Menghitung rating gabungan sebagai rata-rata dari rating produk dan rating ulasan.

## Mengurutkan Produk Rekomendasi
Mengurutkan produk berdasarkan rating gabungan tertinggi dan harga terendah.

## Menghapus Kolom Rating Rata-Rata
Menghapus kolom rating rata-rata.

## Menghapus Kolom Rating
Mengganti nama kolom rating rata-rata menjadi "rating".

## Mencetak Produk Rekomendasi
Menampilkan produk yang direkomendasikan beserta nama, harga, gambar produk, dan rating.

## Simpan Data Rekomendasi ke dalam File Pickle
Produk rekomendasi disimpan dalam file pickle.

## Membaca Data Produk Rekomendasi dari File Pickle
Mengambil data produk rekomendasi dari file pickle.

## Menampilkan Data Produk Rekomendasi
Menampilkan data produk rekomendasi yang telah dimuat dari file pickle.
