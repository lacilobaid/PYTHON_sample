import c_odeme as o
import manuel_sort_fonksiyonu

menu_devam = ""
getir_secim = ""
secim = ""
restoranlar=[]
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
            o.odeme()
    if detay!="1" and detay!="2":
        print("Gecersiz islem...")

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