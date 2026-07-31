"""
Öğrenci Not Analiz Projesi

Plan/Program:
    1. csv dosyasından öğrenci verileri oku
    2. temel istatistiksel hesaplamalar
    3. filtreleme
    4. öğrenci notu görselleştirme
    5. OOP ile yapıyı class üzerinde toplama
    6. hata yönetimi

Veri seti:
    - isim, yas, bolum ve not

Kurulumlar:
pip install numpy pandas matplotlib

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class StudentAnalysier:
    """
    ogrenci not verilerini oku
    analiz et
    filtrele
    gorsellestir
    Attributes:
        doc_path(str):okunacak csv dosya yolu
        df:okunan veri seti
    
    """
    

    def __init__(self,doc_path):
        self.doc_path = doc_path
        self.df = None

    # veri okuma
    def read_data(self):
        """
        csv dosyasını okur.
        """
        try:
            self.df = pd.read_csv(self.doc_path)

            if self.df.empty:
                raise ValueError("csv dosyası boş")

            columns = {"isim","yas","bolum","not"}

            if not columns.issubset(self.df.columns):
                raise ValueError("gerekli sutunlar eksik")

            self.df["not"] = pd.to_numeric(self.df["not"],errors ="raise")
            print("Veri okundu")
            print(self.df)

        except FileNotFoundError:
            print("dosya yolu bulunamadı.")

        except pd.errors.EmptyDataError:
            print("dosya boş")

        except ValueError as error:
            print(error)

        except Exception as e:
            print(e)

    def analysis(self):
        """
        ortalama,min,max,std
        """
        try:
            if self.df is None:
                raise ValueError("veri yok.")

            notlar = self.df["not"].to_numpy()

            print(f"Ortalama:{np.mean(notlar)}")
            print(f"En az not:{np.min(notlar)}")
            print(f"En büyük not:{np.max(notlar)}")
            print(f"Standart sapma:{np.std(notlar)}")
        except ValueError as hata:
            print(f"hata: {hata}")
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu. {e}")

    
    
    def filter(self):
        """
        Filtrelemeler:
            - notu 80 den büyük olan öğrenciler
            - bölümü yapay zeka olanlar
            - yaşı 22 den büyük olanlar
        """
        try:
            if self.df is None:
                raise ValueError("Önce veri okunmalıdır")
            
            print("Pandas ile filtreleme sonuçları")

            # notu 80 den büyük olan öğrenciler
            bigger = self.df[self.df["not"] > 80]
            print(f"Notu 80 den büyük olan öğrenciler: \n{bigger}")

            # bölümü yapay zeka olanlar
            ai = self.df[self.df["bolum"] == "Yapay Zeka"]
            print(f"Bölümü yapay zeka olanlar: \n{ai}")

            # 22 yaşında büyük olan öğrenciler
            older = self.df[self.df["yas"] > 22]
            print(f"22 yaşından büyük olanlar: \n{older}")

        except ValueError as hata:
            print(f"hata: {hata}")
        except Exception as e:
            print(f"Beklenmeyen bir hata: {e}")

    def graphic(self):
        """
            öğrenci notlarını sütun grafiği ile görselleştirme
        """
        try:
            if self.df is None:
                raise ValueError("önce veri okunmalı")
            
            # grafik boyutu ayarla
            plt.figure(figsize=(10, 5))

            # isimleri x eksenine ve notları y eksenine ekle
            plt.bar(self.df["isim"], self.df["not"])
            plt.title("Öğrenci Not Grafiği")
            plt.xlabel("Öğrenci İsimleri")
            plt.ylabel("Notlar")

            plt.tight_layout() # grafik daha güzel görünsün

            plt.show()

        except Exception as e:
            print(f"hata: {e}")

    def all_func_run(self):

        # 1. veriyi okuma
        self.read_data()

        # eğer veri yüklenmezse
        if self.df is None:
            print("analiz durduruldu")
            return
        
        # 2. numpy hesaplamaları
        self.analysis()

        # 3. filtreleme
        self.filter()

        # 4. görselleştirme
        self.graphic()

# programın başlangıç noktası
if __name__ == "__main__":
    
    dosya_yolu = "ogrenci_notlari.csv"
    system = StudentAnalysier(dosya_yolu)

    system.all_func_run()