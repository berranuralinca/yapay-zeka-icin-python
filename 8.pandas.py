import pandas as pd


# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.

veri = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet", "Elif"],
    "yas": [25, 30, 28, 35, 22, 27],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500, 6500]
}

df = pd.DataFrame(veri)

print("VERİ SETİ")
print(df)
print("-" * 50)



# SORU 1
# DataFrame'in ilk 3 satırını gösterin.

ılk_uc = df.head(3)
print(ılk_uc)

# SORU 2
# DataFrame'deki sütun isimlerini ekrana yazdırın.

print(f"Sütunlar:{df.columns}")


# SORU 3
# Sadece "isim" sütununu seçin.

print(f"İsim sütunu:\n{df["isim"]}")

# SORU 4
# Sadece "isim" ve "maas" sütunlarını birlikte gösterin.

print(f"isim ve maaş:\n {df[["isim","maas"]]}")


# SORU 5
# Yaşı 28'den büyük olan kişileri filtreleyin.

print(f"28'den büyük:\n {df[df["yas"] > 28 ]}")

# SORU 6
# Maaşı 6000'den büyük olan kişilerin sadece isim ve maaş bilgilerini gösterin.

print(f"maaşı 6000'den büyük \n {df[df["maas"]>6000][["isim","maas"]]}")


# SORU 7
# Maaşa göre küçükten büyüğe sıralayın.

print(f"maasa göre artan: \n {df.sort_values("maas")}")


# SORU 8
# Maaşa göre büyükten küçüğe sıralayın.


print(f"maasa göre azalan: \n {df.sort_values("maas",ascending=False)}")


# SORU 9
# Şehirlere göre gruplama yapın ve her şehir için ortalama maaşı hesaplayın.

print(f"sehirlere gore grupla: \n {df.groupby("sehir")["maas"].mean()}")


# SORU 10
# "yillik_maas" adında yeni bir sütun oluşturun.
# Bu sütun maaşın 12 ile çarpılması ile oluşturulacaktır.

df["yillik_maas"] = df["maas"]*12
print(df["yillik_maas"])