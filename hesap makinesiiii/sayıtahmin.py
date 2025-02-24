import random

def sayi_tahmin():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")

    while True:
        user_guess = input("Tahmininiz: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        attempts += 1

        if user_guess < number_to_guess:
            print("Daha büyük bir sayı söyleyin.")
        elif user_guess > number_to_guess:
            print("Daha küçük bir sayı söyleyin.")
        else:
            print(f"Tebrikler! {attempts} denemede doğru tahmin ettiniz.")
            break

if __name__ == "__main__":
    sayi_tahmin()