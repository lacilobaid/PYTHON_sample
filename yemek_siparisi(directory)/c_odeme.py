import log_sign_in as sl
import c_menu as m
import time
import random

kartNo = ""
kartKod = ""
kartTarih = ""
bakiye = 500
kullanici_kartNo =[]
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


def odeme():
    global kartNo, kartTarih, kartKod, kart_kayit, odeme_hakki, kayitli_kart_odeme, bakiye, getir_secim
    print("**************************")
    odeme_hakki = 3
    while True:
        if m.secim == "Q" or m.secim=="q":
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
            if m.secim == "1":
                if bakiye==0:
                    print("Yetersiz bakiye")
                    break
                if bakiye < fiyat:
                    print("Yetersiz bakiye")
                    break
                if sl.kullanici_telefon.startswith("542") or sl.kullanici_telefon.startswith("544") or sl.kullanici_telefon.startswith("546") or sl.kullanici_telefon.startswith("549"):
                    if m.getir_secim=="1":
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
                elif m.getir_secim == "1":
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
            if m.secim == "2":
                if bakiye == 0:
                    print("Yetersiz bakiye")
                    break
                if bakiye < fiyat2:
                    print("Yetersiz bakiye")
                    break
                if sl.kullanici_telefon.startswith("542") or sl.kullanici_telefon.startswith("544") or sl.kullanici_telefon.startswith("546") or sl.kullanici_telefon.startswith("549"):
                    if m.getir_secim == "1":
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
                elif m.getir_secim == "1":
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
            if m.secim == "3":
                if bakiye==0:
                    print("Yetersiz bakiye")
                    break
                if bakiye < fiyat3:
                    print("Yetersiz bakiye")
                    break
                if sl.kullanici_telefon.startswith("542") or sl.kullanici_telefon.startswith("544") or sl.kullanici_telefon.startswith("546") or sl.kullanici_telefon.startswith("549"):
                    if m.getir_secim == "1":
                        bakiye = bakiye - indirimli_vodafoneEX3
                        print("**+7 TL getirme ücreti....")
                        print("**Vodafone'lu indiriminden yararlandınız....")
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
                elif m.getir_secim == "1":
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
        print("Siparisiniz {} adresine, {}'a teslim edildi.".format(sl.kullanici_adres,sl.kullanici_adi))
    elif son_teslimat == restoran_teslimat:
        print("Siparisiniz zamanında teslim edildi.")
        print("Siparisiniz {} adresine, {}'a teslim edildi.".format(sl.kullanici_adres,sl.kullanici_adi))
    elif son_teslimat > restoran_teslimat:
        print("Siparisiniz {} saniye gec teslim edildi.".format(gecikme_suresi))
        print("Siparisiniz {} adresine, {}'a teslim edildi.".format(sl.kullanici_adres, sl.kullanici_adi))