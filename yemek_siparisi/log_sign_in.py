import random

kullanici_adi = ""
kullanici_eposta = ""
kullanici_telefon = ""
kullanici_adres = ""
kayitli_kullanici_telefon = ""
kayitli_kullanici_ad = ""

def sign_in():
    global kullanici_adi, kullanici_eposta, kullanici_telefon, kullanici_adres, kod, dogrulama, kod_hakki, giris_hakki, kullanici_sifre, kullanici_sifre_tekrar
    kod_hakki=3
    giris_hakki=3
    kullanici_adi = input("Ad ve soyad giriniz: ")
    kullanici_eposta = input("Eposta giriniz: ")
    kullanici_sifre = input("Sifrenizi giriniz: ")
    kullanici_sifre_tekrar = input("Sifrenizi tekrar giriniz: ")
    kullanici_telefon = input("Telefon numarası giriniz (basında 0 olmadan): ")
    kullanici_adres = input("Adresinizi giriniz: ")
    while True:
        if (kullanici_sifre==kullanici_sifre_tekrar):
            if (kullanici_eposta.endswith("@gmail.com") or kullanici_eposta.endswith("@hotmail.com")):
                if (len(kullanici_telefon) == 10 and kullanici_telefon.startswith("5")):
                    kod = random.randint(1000, 10000)
                    print("**EXYemek Dogrulama Kodunuz: {}".format(kod))
                    dogrulama = int(input("{} Nolu telefona gelen kodu giriniz: ".format(kullanici_telefon)))
                    if (kod == dogrulama):
                        print("{} EXYemek Kaydınız Başarılı... Giris Yapabilirsiniz... ".format(kullanici_adi))
                        return True
                    else:
                        kod_hakki -= 1
                        print("Kod hatali")
                        print("********************")
                    if (kod_hakki == 0):
                        print("Kayıt gerceklestirilemedi...")
                        return False
                else:
                    giris_hakki -= 1
                    print("********************")
                    print("Hatali numara....")
                    kullanici_telefon = input("Telefon numarası giriniz (basında 0 olmadan): ")
            else:
                giris_hakki -= 1
                print("********************")
                print("Hatali eposta...")
                kullanici_eposta = input("Eposta giriniz: ")
        else:
            giris_hakki-=1
            print("********************")
            print("Hatali sifre...")
            kullanici_sifre = input("Sifrenizi giriniz: ")
            kullanici_sifre_tekrar = input("Sifrenizi tekrar giriniz: ")
        if (giris_hakki == 0):
            print("Hakkınız bitti... Kayıt basarısız....")
            return False

def log_in():
    global kayitli_kullanici_telefon, giris_kod, giris_dogrulama, hak_kod, hak_giris
    hak_kod = 3
    hak_giris = 4
    kayitli_kullanici_telefon=input("Telefon numaranızı girin (basında 0 olmadan): ")
    while True:
        if (len(kayitli_kullanici_telefon) == 10 and kayitli_kullanici_telefon.startswith("5")):
            if (kullanici_telefon == kayitli_kullanici_telefon):
                giris_kod = random.randint(1000, 10000)
                print("**EXYemek dogrulama kodunuz: {}".format(giris_kod))
                giris_dogrulama = int(input("{} Nolu telefona gelen kodu giriniz: ".format(kayitli_kullanici_telefon)))
                if (giris_dogrulama == giris_kod):
                        print("{} EXYemek'e Hoşgeldiniz...".format(kullanici_adi))
                        break
                else:
                    hak_kod -= 1
                    print("Hatalı kod...")
                    print("********************")
                if (hak_kod==0):
                    print("Giris basarısız...")
                    return False
            else:
                hak_giris-=1
                print("Gecersiz numara...")
                kayitli_kullanici_telefon = input("Telefon numaranızı girin: ")

        else:
            hak_giris -= 1
            print("********************")
            print("Bu numaraya kayitli bir kullanıcı bulunmamaktadır.")
            kayitli_kullanici_telefon = input("Telefon numaranızı girin: ")
        if (hak_giris==0):
            print("Giris basarısız...")
            return False