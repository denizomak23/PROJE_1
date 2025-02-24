def bilgi_yarismasi():
    sorular = [
        {"soru": "Türkiye'nin başkenti neresidir?", "cevap": "Ankara"},
        {"soru": "Dünyanın en büyük okyanusu hangisidir?", "cevap": "Pasifik"},
        {"soru": "Einstein'ın ünlü denklemi nedir?", "cevap": "E=mc^2"},
        {"soru": "Python hangi yıl ortaya çıktı?", "cevap": "1991"},
        {"soru": "Dünyanın en yüksek dağı hangisidir?", "cevap": "Everest"},
        {"soru": "İstanbul hangi iki kıta arasında yer alır?", "cevap": "Avrupa ve Asya"},
        {"soru": "Dünyanın en uzun nehri hangisidir?", "cevap": "Nil"},
        {"soru": "Güneş sistemindeki en büyük gezegen hangisidir?", "cevap": "Jüpiter"},
        {"soru": "İnternetin ilk adı nedir?", "cevap": "ARPANET"},
        {"soru": "Dünyanın en kalabalık ülkesi hangisidir?", "cevap": "Çin"}
    ]

    score = 0

    for i, soru in enumerate(sorular, 1):
        print(f"Soru {i}: {soru['soru']}")
        cevap = input("Cevabınız: ")

        if cevap.lower() == soru["cevap"].lower():
            print("Doğru!")
            score += 1
        else:
            print(f"Yanlış. Doğru cevap: {soru['cevap']}")

    print(f"Yarışma bitti! Toplam doğru sayınız: {score}/{len(sorular)}")

if __name__ == "__main__":
    bilgi_yarismasi()