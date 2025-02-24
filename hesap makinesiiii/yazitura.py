import random

def yazitura():
    result = random.choice(["Yazı", "Tura"])
    return result

def play_yazitura():
    user_choice = input("Seçiminizi yapın (Yazı, Tura): ")
    while user_choice not in ["Yazı", "Tura"]:
        user_choice = input("Geçersiz seçim. Lütfen tekrar deneyin (Yazı, Tura): ")
    
    result = yazitura()
    print(f"Sonuç: {result}")
    
    if user_choice == result:
        print("Kazandınız!")
    else:
        print("Kaybettiniz!")

if __name__ == "__main__":
    play_yazitura()