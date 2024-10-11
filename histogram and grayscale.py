# ANGGA PUTRA DWI DITANDRA - 5220411081
# Pemrosesan Citra Digital

# memanggil library openCV dan numpy
import cv2 #import library openCV
import numpy as np  #import library openCV dan numpy

#membaca citra digital dari gambar
citra = cv2.imread('c:\\Users\\ACER\\OneDrive\\Pictures\\Saved Pictures\\1.jpg')

#menampilkan citra digital ke dalam jendela
cv2.imshow('gambar', citra)

b, g, r = cv2.split(citra) #memisahkan channel warna
citra_gray = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY) #mengubah citra ke grayscale

#menyimpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(citra)
jum_kolom = len(citra[0])
tot_pixel = jum_baris * jum_kolom

#menghitung nilai pixel grayscale
hist_gray = np.zeros(256) #inisialisasi histogram grayscale

for i in range(jum_baris):
    for j in range(jum_kolom):
        pixel = int(citra_gray[i][j])
        hist_gray[pixel] += 1

#menampilkan histogram grayscale
import matplotlib.pyplot as plt
plt.bar(range(256), hist_gray)

#tampilkan gray image
cv2.imshow('gambar - gray', citra_gray) #menampilkan citra grayscale

# Menghitung histogram untuk setiap channel RGB
hist_b = np.zeros(256)
hist_g = np.zeros(256)
hist_r = np.zeros(256)

for i in range(jum_baris):
  for j in range(jum_kolom):
    hist_b[b[i][j]] += 1
    hist_g[g[i][j]] += 1
    hist_r[r[i][j]] += 1

# Menampilkan histogram RGB secara terpisah
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.title("Histogram Blue Channel")
PIXEL_VALUE_LABEL = "Pixel value"

plt.xlabel(PIXEL_VALUE_LABEL)
plt.ylabel("Frequency")
plt.bar(range(256), hist_b, color='b')

plt.subplot(3, 1, 2)
plt.title("Histogram Green Channel")
plt.xlabel(PIXEL_VALUE_LABEL)
plt.ylabel("Frequency")
plt.bar(range(256), hist_g, color='g')

plt.subplot(3, 1, 3)
plt.title("Histogram Red Channel")
plt.xlabel(PIXEL_VALUE_LABEL)
plt.ylabel("Frequency")
plt.bar(range(256), hist_r, color='r')

plt.tight_layout()
plt.show()

#tutup histogram ketika user menekan tombol sembarang
plt.waitforbuttonpress()