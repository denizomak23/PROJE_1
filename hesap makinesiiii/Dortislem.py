import random

def generate_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)

    if operation == '/':
        # Ensure division results in an integer
        num1 = num1 * num2

    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def main():
    print("Dört İşlem Matematik Sınavına Hoş Geldiniz!")
    score = 0
    soru_sayisi = 5

    for _ in range(soru_sayisi):
        question, answer = generate_question()
        print(f"Soru: {question}")
        kullanici_cevap = input("Cevabınız: ")

        try:
            kullanici_cevap = float(kullanici_cevap)
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
            continue

        if kullanici_cevap == answer:
            print("Doğru!")
            score += 1
        else:
            print(f"Yanlış. Doğru cevap: {answer}")

    print(f"Sınav bitti! Toplam doğru sayınız: {score}/{soru_sayisi}")

if __name__ == "__main__":
    main()