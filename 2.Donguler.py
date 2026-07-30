# ============================================================
# SORU 1 (IF)
# Kullanıcıdan bir sayı alın.
# Sayı pozitifse "Pozitif", negatifse "Negatif", sıfırsa "Sıfır" yazdırın.
# ============================================================

sayi=int(input("Sayi giriniz:"))

if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sıfır")

# ============================================================
# SORU 2 (FOR)
# 1'den 10'a kadar (10 dahil) sayıları yazdırın.
# Ayrıca bu sayıların toplamını hesaplayıp ekrana yazdırın.
# ============================================================

toplam = 0

for i in range(1, 11):
    print(i)
    toplam += i

print("Toplam:", toplam)

# ============================================================
# SORU 3 (WHILE)
# Kullanıcıdan "q" yazana kadar sürekli giriş alın.
# Kullanıcı her giriş yaptığında "Girdiniz: ..." şeklinde ekrana yazdırın.
# Kullanıcı "q" yazarsa döngü bitsin ve "Çıkış yapıldı" yazsın.
# ============================================================


giris = ""

while giris != "q":
    giris = input("Bir şey yazın (çıkmak için q): ")
    if giris != "q":
        print(f"Girdiniz: {giris}")

print("Çıkış yapıldı")

# ============================================================
# SORU 4 (NESTED)
# 1'den 20'ye kadar sayıları dolaşın.
# Eğer sayı çiftse "Çift", tekse "Tek" yazdırın.
# Ayrıca sayı 10'dan büyükse yanına "Büyük", değilse "Küçük/Eşit" yazdırın.
# Örnek çıktı: 12 -> Çift - Büyük
# ============================================================

for i in range(1, 21):

    if i % 2 == 0:
        tur = "Çift"
    else:
        tur = "Tek"


    if i > 10:
        boyut = "Büyük"
    else:
        boyut = "Küçük/Eşit"

    print(f"{i} -> {tur} - {boyut}")

