import random

kullanıcı_galibiyeti = 0
bilgisayar_galibiyeti = 0
seçenekler = ["taş", "kağıt", "makas"]

tur_sayisi = int(input("Kaç tur oynanacağını seçiniz: "))
tur = 0

while tur < tur_sayisi:
    kullanıcı_girdisi = input("Taş/Kağıt/Makas veya çıkmak için q tuşuna basınız:").lower()

    if kullanıcı_girdisi == "q":
        break

    if kullanıcı_girdisi not in seçenekler:
        print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")
        continue

    rastgele_sayı = random.randint(0, 2)
    bilgisayar_secimi = seçenekler[rastgele_sayı]
    print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

    if kullanıcı_girdisi == bilgisayar_secimi:
        print("Berabere!")
    elif (kullanıcı_girdisi == "taş" and bilgisayar_secimi == "makas") or \
         (kullanıcı_girdisi == "kağıt" and bilgisayar_secimi == "taş") or \
         (kullanıcı_girdisi == "makas" and bilgisayar_secimi == "kağıt"):
        print("Kazandınız!")
        kullanıcı_galibiyeti += 1
    else:
        print("Kaybettiniz!")
        bilgisayar_galibiyeti += 1

    tur += 1

if tur_sayisi == tur:
    print(f"{tur_sayisi} tur oynandı.")
    print(f"Siz {kullanıcı_galibiyeti} kez kazandınız.")
    print(f"Bilgisayar {bilgisayar_galibiyeti} kez kazandı.")

    if kullanıcı_galibiyeti > bilgisayar_galibiyeti:
        print("Oyunu kazanan sizsiniz!")
    elif kullanıcı_galibiyeti < bilgisayar_galibiyeti:
        print("Oyunu kaybettiniz!")
    else:
        print("Oyun berabere bitti.")

print("Görüşürüz!")
