notlar = []

with open("notlar.txt", "r", encoding="utf-8") as dosya:
    
    for satir in dosya:
        try:
            notlar.append(int(satir.strip()))
        except ValueError:
            print(f"Hatalı veri {satir.strip()}")

print(notlar)