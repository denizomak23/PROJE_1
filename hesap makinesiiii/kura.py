import random

def kura_cek(liste):
    return random.choice(liste)

def main():
    print("Kura Çekme Programına Hoş Geldiniz!")
    
    katilimcilar = input("Katılımcıların isimlerini virgülle ayırarak girin: ").split(',')
    katilimcilar = [isim for isim in katilimcilar if isim]  

    if not katilimcilar:
        print("Geçerli katılımcı isimleri girin.")
        return

    kazanan = kura_cek(katilimcilar)
    print(f"Kazanan: {kazanan}")

if __name__ == "__main__":
    main()