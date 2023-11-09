package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
)

func main() {
	// Buka file CSV yang berisi data produk
	csvFile, err := os.Open("products.csv")
	if err != nil {
		fmt.Printf("Gagal membuka file CSV: %v\n", err)
		return
	}
	defer csvFile.Close()

	// Buat pembaca CSV
	csvReader := csv.NewReader(csvFile)

	// Membuka file log untuk mencatat aktivitas unduhan
	logFile, err := os.Create("download_log.txt")
	if err != nil {
		fmt.Printf("Gagal membuka file log: %v\n", err)
		return
	}
	defer logFile.Close()

	// Membuat logger
	logger := log.New(logFile, "", log.LstdFlags)

	// Loop melalui setiap baris dalam file CSV
	for {
		row, err := csvReader.Read()
		if err == io.EOF {
			break // Akhiri loop jika sudah mencapai akhir file
		} else if err != nil {
			fmt.Printf("Gagal membaca baris CSV: %v\n", err)
			return
		}

		// Ambil URL gambar dari kolom yang sesuai dalam CSV
		imageURL := row[2] // Ganti indeks sesuai dengan posisi kolom URL gambar
		// Ambil nama produk dari kolom "name"
		productName := row[1] // Ganti indeks sesuai dengan posisi kolom "name"

		// Membuat nama file dari nama produk dengan mengganti spasi dengan garis bawah
		fileName := fmt.Sprintf("%s.jpg", strings.Replace(productName, " ", "_", -1))

		// Cetak URL gambar dan nama file
		fmt.Printf("URL Gambar: %s\n", imageURL)
		fmt.Printf("Nama File: %s\n", fileName)

		// Unduh dan simpan gambar di direktori "assets"
		err = downloadImage(imageURL, fileName, "assets", logger)
		if err != nil {
			logger.Printf("Gagal mengunduh gambar: %v\n", err)
		} else {
			logger.Printf("Unduhan berhasil: %s\n", fileName)
		}
	}
}

func downloadImage(url, fileName, directory string, logger *log.Logger) error {
	// Mengganti karakter tilde dengan karakter yang valid dalam URL
	url = strings.Replace(url, "~", "%7E", -1)

	// Membuat path file lokal
	filePath := fmt.Sprintf("%s/%s", directory, fileName)

	// Membuat permintaan HTTP GET ke URL gambar
	response, err := http.Get(url)
	if err != nil {
		return err
	}
	defer response.Body.Close()

	// Membuka file lokal untuk menyimpan gambar
	file, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	// Menyalin isi dari respons HTTP ke file lokal
	_, err = io.Copy(file, response.Body)
	if err != nil {
		return err
	}

	return nil
}
