def hmmenu():
    import yazitura
    import hesapmakinesi
    import taskagit
    import turtresim
    import sayıtahmin
    import doviz
    import kura
    import Dortislem
    import bilgi

    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║           PROJE ANA MENÜSÜ             ║")
        print("║                                        ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1 - Yazı Tura                          ║")
        print("║ 2 - Hesap Makinesi                     ║")
        print("║ 3 - Taş Kağıt Makas                    ║")
        print("║ 4 - Şekil Çizme                        ║")
        print("║ 5 - Sayı Tahmin                        ║")
        print("║ 6 - Döviz Hesaplama                    ║")
        print("║ 7 - Kura Çek                           ║")
        print("║ 8 - Dört İşlem Sınavı                  ║")
        print("║ 9 - Bilgi Yarışması                    ║")
        print("║ 10 - Çıkış                             ║")
        print("╚════════════════════════════════════════╝")
        secim = input("Seçiminiz: ")

        if secim == "1":
            yazitura.play_yazitura()
        elif secim == "2":
            hesapmakinesi.hesapmenu()
        elif secim == "3":
            taskagit.play_game()
        elif secim == "4":
            turtresim.main_menu()
        elif secim == "5":
            sayıtahmin.sayi_tahmin()
        elif secim == "6":
            doviz.main()
        elif secim == "7":
            kura.main()
        elif secim == "8":
            Dortislem.main()
        elif secim == "9":
            bilgi.bilgi_yarismasi()
        elif secim == "10":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

hmmenu()