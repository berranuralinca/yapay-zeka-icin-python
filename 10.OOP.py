"""
Veri analizi aracı
    - sayı listesi tutma
    - bu sayıların toplamını hesapla
    - ortalamasını bul
    - en büyük ve en küçük değerleri göster
"""

class VeriAnalizAraci:

#veri al
    def __init__(self,veriler):
        self.veriler = veriler

#veri goster
    def veri_goster(self):
        print(f"veriler:\n {self.veriler}")
#toplam bul
    def toplama(self):
        toplam = sum(self.veriler)
        print(f"toplam:{toplam}")

#ortalama bul
    def ortalama(self):
        ort = sum(self.veriler)/len(self.veriler)
        print(f"ortalama:{ort}")

#max-min
    def min_max(self):
        minumum = min(self.veriler)
        maximum = max(self.veriler)
        print(f"min:{minumum} ,max:{maximum}")
    
veriler1 = VeriAnalizAraci([10,20,30,40,50])
veriler1.veri_goster()
veriler1.toplama()
veriler1.ortalama()
veriler1.min_max()  


"""
Veriler: [10, 20, 30, 40, 50]
Toplam: 150
Ortalama: 30.0
Maksimum değer: 50
Minimum değer: 10
"""