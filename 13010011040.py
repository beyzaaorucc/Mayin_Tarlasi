# 13010011040-BEYZA NUR ORUC
import random


class Oyun_Alani():
    def __init__(self, satir_sayisi, sutun_sayisi, gizlimod):
        self.atis = 0
        self.hamle = int((satir_sayisi * sutun_sayisi * 0.7))
        # hamle sayısı oyun alanın %70 ı kadar olacak.
        self.gizlimod = gizlimod
        self.mayin = []
        self.satir_sayisi = satir_sayisi
        self.sutun_sayisi = sutun_sayisi
        if (satir_sayisi < 10 or sutun_sayisi < 10):
            print("Boyut 10x10'dan daha küçük olamaz..!")
            return
        self.oyun_alani = []
        for i in range(satir_sayisi):
            liste = []
            for j in range(sutun_sayisi):
                liste.append(Hucre())
            self.oyun_alani.append(liste)

    def mayinlari_yerlestir(self, mayinsayisi):
        # self.mayin değişkeninde bütün mayinlari bir liste içine atıyoruz.
        # Daha sonra mayinlara vurulup vurulmadığını ilk indexteki True ya da False ile kontrol ediyoruz.

        mayin = [False]

        while (True):
            # Mayınlar  1 ise sütunda 0 ise yatayda yer alır.
            kontrol = random.randint(0, 1)
            # mayinin rastgele yerleştirileceği koordinatlar aşağıdaki kodlarla sağlanıyor.
            satir = random.randint(0, self.satir_sayisi)
            sutun = random.randint(0, self.sutun_sayisi)
            if (kontrol):
                # bu for döngüsü sınırları kontrol edecek. Eğer index out of range hatası alınırsa veya
                # o hücrede zaten başka bir mayin var ise tekrar random değerler belirlenmesi için döngüyü tekrar başlatacak.
                # Eğer sınırlar içindeyse ve mayin yoksa, hata vermeden devam edeceği için mayin hücrelere yerleştirilir
                try:
                    for i in range(mayinsayisi):
                        if (self.oyun_alani[satir + i][sutun].mayin_var_mi()):
                            raise
                    for i in range(mayinsayisi):
                        self.oyun_alani[satir + i][sutun].mayin_yerlestir(self.gizlimod)
                        mayin.append([satir + i, sutun])
                except:
                    continue
                break

            else:
                # Satira yerleştirilen mayinlar için ;
                try:
                    for i in range(mayinsayisi):
                        if (self.oyun_alani[satir][sutun + i].mayin_var_mi()):
                            raise
                    for i in range(mayinsayisi):
                        self.oyun_alani[satir][sutun + i].mayin_yerlestir(self.gizlimod)
                        mayin.append([satir, sutun + i])
                except:
                    continue

                break
        self.mayin.append(mayin)

    def oyunalani_goster(self):  # Oyun alanını gösteren fonksiyon
        for i in range(self.satir_sayisi):
            for j in range(self.sutun_sayisi):
                print(self.oyun_alani[i][j].hucreyi_goster(), end="   ")
            print()
        # Oyunla ilgili son durum burada gösterilir.
        print("Başarılı atış:", self.atis, "   Hamle sayısı:", self.hamle)

    def atis_yap(self, satir, sutun):
        # Girilen sayılar sınırlar içerisinde mi kontrol edilir.
        if (satir > len(self.oyun_alani) or sutun > len(self.oyun_alani[0])):
            print("Sınırlar dışına atış yapamazsınız..!")
            return
        # Eğer daha önce atış yapıldıysa kullanıcıya uyarı verir.
        if (self.oyun_alani[satir][sutun].atis_yapildi_mi()):
            print("Bu alana daha önce atış yapmıştınız..!")
        else:
            if not self.oyun_alani[satir][sutun].atis_isabet():
                # Eğer True harici bir değer döndürürse  boşluğa atış yapıldı demektir.
                print("Ucuz kurtulduk..!")
                self.hamle += 1
                self.atis += 1
            # Eğer vurduğumuz yerde mayin varsa hücredeki fonksiyon bize True döndürecek.
            else:
                print("Dikkat MAYİN..!Maalesef kaybettiniz..!\nOYUN BİTTİ..!")
                self.atis = 0

    # Eğer atış sayısı sıfıra eşit olursa mayına isabet etmiş demektir ve bu durumda oyun kaybedilir ve biter.
    # Eğer yukarıdaki şart sağlanmıyorsa oyun kazanılır ve hamle sayısı puan olarak kullanıcıya gösterilir.
    def oyun_devam_ediyor_mu(self):
        if (self.atis == 0):
            print("Maalesef kaybettiniz")
            return False

        else:
            print("TEBRİKLER OYUNU KAZANDINIZ! Puanınız:", self.hamle)
            return True


class Hucre():
    # Her bir hücrenin verisini tuttuğumuz sınıf yapısı
    def __init__(self):
        # Class dışından erişilememesi için değişkenler "__" ile belirtilmiştir.
        self.__hucre_sekli = "?"
        self.__mayin_var_mi = False
        self.__vuruldu_mu = False

    def atis_isabet(self):
        self.__vuruldu_mu = True
        if (self.__mayin_var_mi):
            self.__hucre_sekli = "X"
            return True
        else:
            self.__hucre_sekli = "0"
            return False

    def hucreyi_goster(self):
        return self.__hucre_sekli

    def mayin_yerlestir(self, gizlimod):
        if (not (gizlimod)):
            self.__hucre_sekli = "X"
        self.__mayin_var_mi = True

    def mayin_var_mi(self):
        return self.__mayin_var_mi

    def atis_yapildi_mi(self):
        return self.__vuruldu_mu

    satir_sayisi = 0
    sütun_sayisi = 0

    # kullanıcıdan oyun başlangıcı şartlarını belirleyecek parametreler alınır
    while (True):

        satir_sayisi = int(input("Oyun alanı satır sayısını giriniz"))

        sütun_sayisi = int(input("Oyun alanı sutün sayısını giriniz"))

        gizlimod = input("Gizli mod için 'G' , Açık mod için 'A' yazınız.")
        gizlimod.lower()
        if (gizlimod == 'g'):
            oyun = Oyun_Alani(satir_sayisi, sütun_sayisi, True)
            break
        elif (gizlimod == 'a'):
            print("Mayinlar X ile gösterilmektedir")
            oyun = Oyun_Alani(satir_sayisi, sütun_sayisi, False)
            break
        else:
            print("Geçersiz girdi.")
            continue

    # toplam oyun hücresinin %30'u adedince mayın yerleştirilir
    oyun.mayinlari_yerlestir(mayinsayisi=int((satir_sayisi * sütun_sayisi * 0.3)))

    while (True):
        if (oyun.oyun_devam_ediyor_mu):
            oyun.oyunalani_goster()
            atis_satir = int(input("Atış yapmak istediğiniz satır"))
            atis_sutun = int(input("Atış yapmak istediğiniz sutün"))
            oyun.atis_yap(atis_satir - 1, atis_sutun - 1)
        else:
            print("\nOyun bitti..!")
            islem = input("Yeni bir oyun oynamak için 'Y', çıkış yapmak için 'C' yazınız")
            if (islem.lower() == "Y"):
                continue
            elif (islem.lower() == "C"):
                break
            break
