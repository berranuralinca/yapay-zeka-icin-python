"""
Soru 1 (Kolay)

Aşağıdaki değişkenleri oluştur.

isim = "Ahmet"
yaş = 22
boy = 1.78

Sonra ekrana şu şekilde yazdır.

Ahmet 22 yaşında ve boyu 1.78 metredir.
"""

isim="Ahmet"
yas=22
boy=1.78

print(f"{isim} {yas} yaşında ve boyu {boy} metredir.")

"""
Soru 2

Aşağıdaki listeyi oluştur.

meyveler = ["elma", "muz", "kivi"]

Sonra

En sona "çilek" ekle.
İlk elemanı "armut" yap.
"muz"u sil.

Son durumda liste ne olur?
"""
meyveler=["elma","muz","kivi"]
meyveler.append("çilek")
meyveler[0]="armut"
meyveler.pop(1)
print(meyveler)

"""
Soru 3

Aşağıdaki sözlüğü oluştur.

ogrenci = {
    "isim":"Ayşe",
    "yas":20
}

Sonra

"not" anahtarını ekle ve değeri 95 olsun.
"yas" değerini 21 yap.

En son sözlüğü yazdır.
"""
ogrenci={
    "isim":"ayşe",
    "yas":20
}

ogrenci["not"]=95
ogrenci["yas"]=21
print(ogrenci)

"""
Soru 4

Aşağıdaki listenin tekrar eden elemanlarını kaldır.

sayilar = [1,2,2,3,4,4,5,5,5]

Bunun için set kullan.
"""
sayilar={1,2,2,3,4,4,5,5,5}
print(sayilar)

"""
Soru 5 (Biraz düşündüren)

Bir ürünün fiyatı 250 TL.

KDV oranı %20.

Program sonunda şu yazsın:

Ürün fiyatı: 250 TL
KDV'li fiyat: 300 TL
"""
fiyat=250
kdv_oran=0.2
kdvli_fiyat=fiyat*1.2
print(f"Ürün fiyatı:{fiyat}")
print(f"KDV'li fiyat:{kdvli_fiyat}")