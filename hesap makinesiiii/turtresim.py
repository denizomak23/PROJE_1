import turtle

def draw_square():
    artist = turtle.Turtle()
    artist.shape("turtle")
    artist.color("blue")
    artist.speed(2)

    for _ in range(4):
        artist.forward(100)
        artist.right(90)

def draw_triangle():
    artist = turtle.Turtle()
    artist.shape("turtle")
    artist.color("green")
    artist.speed(2)

    for _ in range(3):
        artist.forward(100)
        artist.left(120)

def draw_circle():
    artist = turtle.Turtle()
    artist.shape("turtle")
    artist.color("red")
    artist.speed(2)

    artist.circle(100)

def main_menu():
    window = turtle.Screen()
    window.bgcolor("white")

    while True:
        print("************************************")
        print("*                                  *")
        print("*        ŞEKİL ÇİZME MENÜSÜ        *")
        print("*                                  *")
        print("************************************")
        print("1 - Kare çiz")
        print("2 - Üçgen çiz")
        print("3 - Daire çiz")
        print("4 - Çıkış")
        print("************************************")
        secim = input("Seçiminiz: ")

        if secim == "1":
            draw_square()
        elif secim == "2":
            draw_triangle()
        elif secim == "3":
            draw_circle()
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

    window.bye()

if __name__ == "__main__":
    main_menu()