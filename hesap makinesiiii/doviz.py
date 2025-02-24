def doviz_hesapla(miktar, kur):
    return miktar * kur

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    print("Döviz Hesaplama Programına Hoş Geldiniz!")
    
    miktar = input("Lütfen dönüştürmek istediğiniz miktarı girin: ")
    kur = input("Lütfen döviz kurunu girin: ")

    if not is_float(miktar) or not is_float(kur):
        print("Lütfen geçerli bir sayı girin.")
        return

    miktar = float(miktar)
    kur = float(kur)

    sonuc = doviz_hesapla(miktar, kur)
    print(f"Dönüştürülen miktar: {sonuc}")

if __name__ == "__main__":
    main()