import random

def get_computer_choice():
    choices = ["taş", "kağıt", "makas"]
    return random.choice(choices)

def get_user_choice():
    user_input = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()
    while user_input not in ["taş", "kağıt", "makas"]:
        user_input = input("Geçersiz seçim. Lütfen tekrar deneyin (taş, kağıt, makas): ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere!"
    elif (user_choice == "taş" and computer_choice == "makas") or \
         (user_choice == "kağıt" and computer_choice == "taş") or \
         (user_choice == "makas" and computer_choice == "kağıt"):
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

def play_game():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f"Bilgisayarın seçimi: {computer_choice}")
    print(f"Sizin seçiminiz: {user_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()