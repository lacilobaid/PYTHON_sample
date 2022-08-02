import log_sign_in as sl
import c_menu as m
import c_odeme as o
import time

print("EXYemek'e Hosgeldiniz........")
print("******************************")

bool=sl.sign_in()
if bool!=False:
    deger = sl.log_in()
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
                m.menu_1devam()
            elif (menu == "2"):
                m.restoran_listele()
                m.restoran_secim(m.restoranlar)
            elif (menu == "3"):
                print("Sepetiniz: {}".format(o.sepet))

