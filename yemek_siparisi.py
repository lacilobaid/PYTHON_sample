# Gelismis Yemek Siparisi

# filtreleme, +
# vodafone menusu 542, 544, 546, 549, +
# kayıt olma, +
# sepete ekle, +
# adres, +
# tutar, +
# gönderen, +
# ödeme, +
# ex getirsin +7, +
# restoran getirsin +0tl, +
# kredi kart bilgisini ödeme ekranında al, +
# kaydetmek isterse kaydet, +
# ilk siparişte kartı mutlaka yazmalı, +
# bakiye tutar karsılastırması, +

import random
import time
import manuel_sort_fonksiyonu


kullanici_adi = ""
kullanici_eposta = ""
kullanici_telefon = ""
kullanici_adres = ""
kayitli_kullanici_telefon = ""
kayitli_kullanici_ad = ""
menu_devam=""
kartNo = ""
kartKod = ""
kartTarih = ""
getir_secim = ""
bakiye = 500
kullanici_kartNo =[]
restoranlar = []


restoranlar_dizi=[("McDonald's","4.4","17"), ("Adıyamanlı Cigkofteci","4.6","12"), ("Tuğra Dürüm","3.9","20"), ("Komagene Cigkofte","4.2","7"), ("Zater Döner","4.7","18"), ("Bambara Ekmek Arası","4.5","12"), ("Pillavi","4.6","10"), ("Okuzefendi Burger","4,3","14"), ("Ekleristan","4.5","12")]
restoranlar_sure=[("17","4.4","McDonald's"), ("13","4.6","Adıyamanlı Cigkofteci"), ("20","3.9","Tuğra Dürüm"), ("10","4.2","Komagene Cigkofte"), ("18","4.7","Zater Döner"), ("15","4.5","Bambara Ekmek Arası"), ("10","4.6","Pillavi"), ("14","4,3","Okuzefendi Burger"), ("11","4.5","Ekleristan")]
restoranlar_puan=[("4.4","McDonald's","17"), ("4.6","Adıyamanlı Cigkofteci","12"),("4.3","Okuzefendi Burger","14"), ("4.5","Ekleristan","12"),("3.9","Tuğra Dürüm","20"), ("4.2","Komagene Cigkofte","7"), ("4.7","Zater Döner","18"), ("4.5","Bambara Ekmek Arası","12"), ("4.6","Pillavi","10")]
manuel_sort_fonksiyonu.ikinci(restoranlar_puan,0,len(restoranlar_puan)-1)
manuel_sort_fonksiyonu.ikinci(restoranlar_sure,0,len(restoranlar_sure)-1)
tersten_sure=[("17","4.4","McDonald's"), ("13","4.6","Adıyamanlı Cigkofteci"), ("20","3.9","Tuğra Dürüm"), ("10","4.2","Komagene Cigkofte"), ("18","4.7","Zater Döner"), ("15","4.5","Bambara Ekmek Arası"), ("10","4.6","Pillavi"), ("14","4,3","Okuzefendi Burger"), ("11","4.5","Ekleristan")]
tersten_puan=[("4.4","McDonald's","17"), ("4.6","Adıyamanlı Cigkofteci","12"),("4.3","Okuzefendi Burger","14"), ("4.5","Ekleristan","12"),("3.9","Tuğra Dürüm","20"), ("4.2","Komagene Cigkofte","7"), ("4.7","Zater Döner","18"), ("4.5","Bambara Ekmek Arası","12"), ("4.6","Pillavi","10")]
manuel_sort_fonksiyonu.ikinci_tersten(tersten_puan,0,len(tersten_puan)-1)
manuel_sort_fonksiyonu.ikinci_tersten(tersten_sure,0,len(tersten_sure)-1)
sepet=[]

EXYemek_fiyat = 57
indirimli_vodafoneEX = EXYemek_fiyat * 0.70
EXYemek_fiyat2 = 77
indirimli_vodafoneEX2 = EXYemek_fiyat2 * 0.70
EXYemek_fiyat3 = 106
indirimli_vodafoneEX3 = EXYemek_fiyat3 * 0.70

fiyat=50
indirimli_fiyat = fiyat * 0.70
fiyat2=70
indirimli_fiyat2 = fiyat2 * 0.70
fiyat3=99
indirimli_fiyat3 = fiyat3 * 0.70

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

def restoran_listele():
    global restoranlar
    restoranlar = input("1. McDonald's \n2. Adıyamanlı Cigkofteci \n3. Tuğra Dürüm \n4. Komagene Cigkofte \n5. Zater Döner \n6. Bambara Ekmek Arası \n7. Pillavi \n8. Okuzefendi Burger \n9. Ekleristan \nBir secim yapınız: ")

def getir():
    global getir_secim
    print("**************************")
    getir_secim=input("1. EXYemek getirsin(+7 TL) \n2. Restoran getirsin \nBir secim yapınız: ")
    if getir_secim=="1" or getir_secim=="2":
        restoran_listele()
        restoran_secim(restoranlar)

def menu_1devam():
    global menu_devam
    print("**************************")
    menu_devam = input("1. Restoran puanına göre sırala \n2. Teslimat süresine göre sırala \n3. Teslimat yöntemine göre sırala \nBir secim yapınız: ")
    if menu_devam == "3":
        getir()
    elif menu_devam == "1" or menu_devam == "2":
        azMi_cokMu()
    else:
        print("Gecersiz islem...")

def azMi_cokMu():
    global sirala,sirali_secim
    print("**************************")
    sirala=input("1. Yuksekten dusuge sırala \n2. Dusukten yuksege sırala \nBir secim yapınız: ")
    if menu_devam=="1" and sirala == "1":
        print(tersten_puan)
        sirali_secim = input("Bir secim yapınız: ")
        restoran_secim(sirali_secim)
    elif menu_devam=="2" and sirala == "1":
        print(tersten_sure)
        sirali_secim = input("Bir secim yapınız: ")
        restoran_secim(sirali_secim)
    elif menu_devam=="1" and sirala == "2":
        print(restoranlar_puan)
        sirali_secim = input("Bir secim yapınız: ")
        restoran_secim(sirali_secim)
    elif menu_devam=="2" and sirala == "2":
        print(restoranlar_sure)
        sirali_secim = input("Bir secim yapınız: ")
        restoran_secim(sirali_secim)
    else:
        print("Gecersiz islem...")

def restoran_detay(sayi):
    global detay, secim
    print("**************************")
    detay=input("1. Restoranın puanı/teslimat süresi \n2. Restoran menu \nBir secim yapınız: ")
    if detay == "1" and menu_devam =="1" and sirala == "1":
        print("{}, Teslimat suresi: {} Puan: {}".format(tersten_puan[sayi][1],tersten_puan[sayi][2],tersten_puan[sayi][0]))
        print("*********************************")
    elif detay == "1" and menu_devam =="2" and sirala == "1":
        print("{}, Teslimat suresi: {} Puan: {}".format(tersten_sure[sayi][2],tersten_sure[sayi][0],tersten_sure[sayi][1]))
        print("*********************************")
    elif detay == "1" and menu_devam =="1" and sirala == "2":
        print("{}, Teslimat suresi: {} Puan: {}".format(restoranlar_puan[sayi][1],restoranlar_puan[sayi][2], restoranlar_puan[sayi][0]))
        print("*********************************")
    elif detay == "1" and menu_devam =="2" and sirala == "2":
        print("{}, Teslimat suresi: {} Puan: {}".format(restoranlar_sure[sayi][2],restoranlar_sure[sayi][0], restoranlar_sure[sayi][1]))
        print("*********************************")
    elif detay == "1":
        print(restoranlar_dizi[sayi])
    elif detay=="2":
        print("1. 50TL yemek + icecek\n2. 70TL yemek + icecek + tatli\n3. 99TL 2'li menu + 2 icecek + patates kızartması")
        secim = input("Bir menu seciniz(Cıkıs icin q): ")
        if secim != "1" and secim != "2" and secim != "3" and secim != "q" and secim != "Q":
            print("Gecersiz menu secimi...")
        else:
            odeme()
    if detay!="1" and detay!="2":
        print("Gecersiz islem...")

def odeme():
    global kartNo, kartTarih, kartKod, kart_kayit, odeme_hakki, kayitli_kart_odeme, bakiye, getir_secim
    print("**************************")
    odeme_hakki = 3
    while True:
        if secim == "Q" or secim=="q":
            print("Sayfadan cıkılıyor...")
            break
        kayitli_kart_odeme = input("Kayitli kartinizdan ödeme yapmak isterseniz E tusuna basınız: ")
        if (kayitli_kart_odeme == "e" or kayitli_kart_odeme == "E"):
            if len(kullanici_kartNo) != 0:
                print("Odeme yapılacak kart bilgileri: ", kullanici_kartNo)
            else:
                print("Kayıtlı kartınız yok...")
                kartNo = input("Kart numaranızı giriniz: ")
                kartTarih = input("Son kullanma tarihiniz giriniz (a/y): ")
                kartKod = input("Guvenlik kodunu giriniz: ")
                if (len(kartNo) != 16 or len(kartTarih) != 5 or len(kartKod) != 3):
                    odeme_hakki -= 1
                    print("Hatali kart bilgisi...")
                else:
                    kart_kayit = input("Kartınızı kaydetmek isterseniz E tusuna basınız: ")
                    if (kart_kayit == "E" or kart_kayit == "e"):
                        time.sleep(2.0)
                        kullanici_kartNo.append(kartNo)
                        kullanici_kartNo.append(kartKod)
                        kullanici_kartNo.append(kartTarih)
                        print("Kartınız kaydedildi")
                    else:
                        print("Kart kaydedilmeden devam ediliyor..")
        else:
            kartNo = input("Kart numaranızı giriniz: ")
            kartTarih = input("Son kullanma tarihiniz giriniz (a/y): ")
            kartKod = input("Guvenlik kodunu giriniz: ")
            if (len(kartNo) != 16 or len(kartTarih) != 5 or len(kartKod) != 3):
                odeme_hakki -= 1
                print("Hatali kart bilgisi...")
            else:
                kart_kayit = input("Kartınızı kaydetmek isterseniz E tusuna basınız: ")
                if (kart_kayit == "E" or kart_kayit == "e"):
                    time.sleep(2.0)
                    kullanici_kartNo.append(kartNo)
                    kullanici_kartNo.append(kartKod)
                    kullanici_kartNo.append(kartTarih)
                    print("Kartınız kaydedildi")
                else:
                    print("Kart kaydedilmeden devam ediliyor..")
        if odeme_hakki==0:
            print("Odeme basarısız...")
            break
        if (len(kartNo)==16 and len(kartTarih)==5 and len(kartKod)==3):
            if secim == "1":
                if bakiye==0:
                    print("Yetersiz bakiye")
                    break
                if bakiye < fiyat:
                    print("Yetersiz bakiye")
                    break
                if kullanici_telefon.startswith("542") or kullanici_telefon.startswith("544") or kullanici_telefon.startswith("546") or kullanici_telefon.startswith("549"):
                    if getir_secim=="1":
                        bakiye = bakiye - indirimli_vodafoneEX
                        print("**Vodafone'lu indiriminden yararlandınız....")
                        print("**+7 TL getirme ücreti....")
                        print("Odeme basarılı")
                        print("Kalan bakiyeniz: {}".format(bakiye))
                        sepet.append("50TL yemek + icecek")
                        odeme_sonrasi()
                        break
                    else:
                        bakiye = bakiye - indirimli_fiyat
                        print("**Vodafone'lu indiriminden yararlandınız....")
                        print("Odeme basarılı")
                        print("Kalan bakiyeniz: {}".format(bakiye))
                        sepet.append("50TL yemek + icecek")
                        odeme_sonrasi()
                        break
                elif getir_secim == "1":
                    bakiye = bakiye - EXYemek_fiyat
                    print("**+7 TL getirme ücreti....")
                    print("Odeme basarılı")
                    print("Kalan bakiyeniz: {}".format(bakiye))
                    sepet.append("50TL yemek + icecek")
                    odeme_sonrasi()
                    break
                else:
                    bakiye = bakiye - fiyat
                    print("Odeme basarılı")
                    print("Kalan bakiyeniz: {}".format(bakiye))
                    sepet.append("50TL yemek + icecek")
                    odeme_sonrasi()
                    break
            if secim == "2":
                if bakiye == 0:
                    print("Yetersiz bakiye")
                    break
                if bakiye < fiyat2:
                    print("Yetersiz bakiye")
                    break
                if kullanici_telefon.startswith("542") or kullanici_telefon.startswith("544") or kullanici_telefon.startswith("546") or kullanici_telefon.startswith("549"):
                    if getir_secim == "1":
                        bakiye = bakiye - indirimli_vodafoneEX2
                        print("**Vodafone'lu indiriminden yararlandınız....")
                        print("**+7 TL getirme ücreti....")
                        print("Odeme basarılı")
                        print("Kalan bakiyeniz: {}".format(bakiye))
                        sepet.append("70TL yemek + icecek + tatli")
                        odeme_sonrasi()
                        break
                    else:
                        bakiye = bakiye - indirimli_fiyat2
                        print("**Vodafone'lu indiriminden yararlandınız....")
                        print("Odeme basarılı")
                        print("Kalan bakiyeniz: {}".format(bakiye))
                        sepet.append("70TL yemek + icecek + tatli")
                        odeme_sonrasi()
                        break
                elif getir_secim == "1":
                    bakiye = bakiye - EXYemek_fiyat2
                    print("**+7 TL getirme ücreti....")
                    print("Odeme basarılı")
                    print("Kalan bakiyeniz: {}".format(bakiye))
                    sepet.append("70TL yemek + icecek + tatli")
                    odeme_sonrasi()
                    break
                else:
                    bakiye = bakiye - fiyat2
                    print("Odeme basarılı")
                    print("Kalan bakiyeniz: {}".format(bakiye))
                    sepet.append("70TL yemek + icecek + tatli")
                    odeme_sonrasi()
                    break
            if secim == "3":
                if bakiye==0:
                    print("Yetersiz bakiye")
                    break
                if bakiye < fiyat3:
                    print("Yetersiz bakiye")
                    break
                if kullanici_telefon.startswith("542") or kullanici_telefon.startswith("544") or kullanici_telefon.startswith("546") or kullanici_telefon.startswith("549"):
                    if getir_secim == "1":
                        bakiye = bakiye - indirimli_vodafoneEX3
                        print("**Vodafone'lu indiriminden yararlandınız....")
                        print("**+7 TL getirme ücreti....")
                        print("Odeme basarılı")
                        print("Kalan bakiyeniz: {}".format(bakiye))
                        sepet.append("99TL 2'li menu + 2 icecek + patates kızartması")
                        odeme_sonrasi()
                    else:
                        bakiye = bakiye - indirimli_fiyat3
                        print("**Vodafone'lu indiriminden yararlandınız....")
                        print("Odeme basarılı")
                        print("Kalan bakiyeniz: {}".format(bakiye))
                        sepet.append("99TL 2'li menu + 2 icecek + patates kızartması")
                        odeme_sonrasi()
                        break
                elif getir_secim == "1":
                    bakiye = bakiye - EXYemek_fiyat3
                    print("**+7 TL getirme ücreti....")
                    print("Odeme basarılı")
                    print("Kalan bakiyeniz: {}".format(bakiye))
                    sepet.append("99TL 2'li menu + 2 icecek + patates kızartması")
                    odeme_sonrasi()
                    break
                else:
                    bakiye = bakiye - fiyat3
                    print("Odeme basarılı")
                    print("Kalan bakiyeniz: {}".format(bakiye))
                    sepet.append("99TL 2'li menu + 2 icecek + patates kızartması")
                    odeme_sonrasi()
                    break

def restoran_secim(restoranlar):
    if restoranlar == "1":
        restoran_detay(0)
    elif restoranlar == "2":
        restoran_detay(1)
    elif restoranlar == "3":
        restoran_detay(2)
    elif restoranlar == "4":
        restoran_detay(3)
    elif restoranlar == "5":
        restoran_detay(4)
    elif restoranlar == "6":
        restoran_detay(5)
    elif restoranlar == "7":
        restoran_detay(6)
    elif restoranlar == "8":
        restoran_detay(7)
    elif restoranlar == "9":
        restoran_detay(8)
    else:
        print("Gecersiz islem...")

def odeme_sonrasi():
    global son_teslimat, float_teslimat, gecikme_suresi, erken_sure
    print("***************************")
    time.sleep(2.0)
    print("Siparisiniz hazırlanıyor...")
    restoran_teslimat = random.randint(1, 20)
    son_teslimat = random.randint(1,20)
    float_teslimat = float(son_teslimat)
    gecikme_suresi = son_teslimat - restoran_teslimat
    erken_sure = restoran_teslimat - son_teslimat
    print("Tahmini teslimat süresi: {}".format(restoran_teslimat))
    time.sleep(float_teslimat)
    if son_teslimat < restoran_teslimat:
        print("Siparisiniz {} saniye erken teslim edildi.".format(erken_sure))
        print("Siparisiniz {} adresine, {}'a teslim edildi.".format(kullanici_adres,kullanici_adi))
    elif son_teslimat == restoran_teslimat:
        print("Siparisiniz zamanında teslim edildi.")
        print("Siparisiniz {} adresine, {}'a teslim edildi.".format(kullanici_adres,kullanici_adi))
    elif son_teslimat > restoran_teslimat:
        print("Siparisiniz {} saniye gec teslim edildi.".format(gecikme_suresi))
        print("Siparisiniz {} adresine, {}'a teslim edildi.".format(kullanici_adres, kullanici_adi))

print("EXYemek'e Hosgeldiniz........")
print("******************************")

bool=sign_in()
if bool!=False:
    deger = log_in()
    if deger!=False:
        while (True):
            menu = input(
                "1. Filtreleme yap \n2. Tüm restoranları listele \n3. Sepete git \nQ. Cıkıs yap \nBir secim yapınız: ")
            if menu == "q" or menu == "Q":
                print("Oturum kapatılıyor...")
                time.sleep(1.0)
                print("Yine bekleriz...")
                break
            elif (menu == "1"):
                menu_1devam()
            elif (menu == "2"):
                restoran_listele()
                restoran_secim(restoranlar)
            elif (menu == "3"):
                print("Sepetiniz: {}".format(sepet))

