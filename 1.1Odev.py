# ============================================================
# SORU 1
# Bir değişken tanımlayalım: ad = "Kaan", yas = 25, ortalama = 3.45
# Bu değişkenlerin tiplerini type() ile yazdıralım.
# ============================================================

ad="Kaan"
yas=25
ortalama=3.45
print(type(ad))
print(type(yas))
print(type(ortalama))

# ============================================================
# SORU 2
# Kullanıcıdan yaş bilgisini input() ile alalım.
# Bu yaşın tipini ekrana basalım ve 5 yıl ekleyip sonucu yazdıralım.
# Not: input() her zaman string döndürür, int'e çevirmeyi unutmayalım.
# ============================================================

yas_bilgisi=int(input("Yaş giriniz:"))
print(type(yas_bilgisi))
print(f"yas+5:{yas_bilgisi+5}")

# ============================================================
# SORU 3
# Bir ürün fiyatı (float) alalım. %18 KDV hesaplayalım.
# Toplam fiyatı 2 basamak olacak şekilde yazdıralım.
# ============================================================

float_fiyat = float(input("Ürün fiyatı giriniz:"))
kdvli = float_fiyat * 1.18
print(f"Toplam fiyat:{round(kdvli)}")

# ============================================================
# SORU 4
# Bir liste oluşturalım: sayilar = [10, 20, 30, 40, 50]
# - İlk elemanı yazdıralım
# - Son elemanı yazdıralım
# - 2. indexten sona kadar olan parçayı yazdıralım
# - Listeye 60 ekleyelim
# - Listedeki 20 değerini silelim
# ============================================================

sayilar=[10, 20, 30, 40, 50]
print(f"ilk eleman:{sayilar[0]}")
print(f"son eleman:{sayilar[4]}")
print(f"son 3 eleman:{sayilar[2:]}")
sayilar.append(60)
sayilar.pop(1)
print(sayilar)

# ============================================================
# SORU 5
# Bir tuple oluşturalım: koordinat = (12, 34)
# - Tuple içindeki değerleri unpacking ile x ve y değişkenlerine alalım
# - x ve y'yi yazdıralım
# - Tuple'ın değiştirilemediğini göstermek için (yorum satırıyla) örnek verelim
# ============================================================

koordinat = (12, 34)
x, y = koordinat
print("x:", x)
print("y:", y)

# SORU 6
# Bir sözlük (dictionary) oluşturalım:
# ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
# - Öğrencinin ismini yazdıralım
# - "not" anahtarı ile 90 ekleyelim
# - "yas" değerini 23 yaparak güncelleyelim
# - Tüm anahtarları ve tüm değerleri yazdıralım
# ============================================================
ogrenci = {
    "isim": "Ayşe",
    "yas": 22,
    "bolum": "Yazılım"
    }

print("İsim:", ogrenci["isim"])

ogrenci["not"] = 90
ogrenci["yas"] = 23

print("Güncel sözlük:", ogrenci)
print("Anahtarlar:", list(ogrenci.keys()))
print("Değerler:", list(ogrenci.values()))

# ============================================================
# SORU 7
# Set oluşturalım ve tekrar edenleri temizleyelim:
# liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
# - listeyi set'e çevirip benzersiz isimleri yazdıralım
# - benzersiz isim sayısını yazdıralım
# ============================================================

liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
benzersiz_isimler = set(liste)
print("Benzersiz isimler:", benzersiz_isimler)
print("Benzersiz isim sayısı:", len(benzersiz_isimler))