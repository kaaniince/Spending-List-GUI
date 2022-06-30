import json
from tkinter import *
from tkinter import filedialog as fd


class Harcamalar(Frame):#Baska elemanlari icine alan bir kapsayici eleman ile yaratıldı

    def __init__(self, parent,harcama_listesi): #parent->> root bağlndı
        Frame.__init__(self, parent,harcama_listesi)
        self.parent = parent #özniteliğe atıldı.
        self.harcama_listesi = harcama_listesi
        self.initUI()

    def initUI(self):#uygulamanın görselliği buradan değiştiriliyor.
        self.pack(fill=BOTH, expand=1)
        self.harcama_listesi = []
        self.lb = Listbox(self, selectmode="single")

        aktar_btn = Button(self,text="Aktar", command=self.aktar)
        secili_sil_btn = Button(self, text="Secili Sil",command=self.secili_sil)
        hepsini_sil_btn = Button(self,text="Hepsini Sil",command=self.hepsini_sil)

        self.lb.pack(expand=True, fill=X)#görsel eleman gözüktü.  pencere genişliği arttıkca lb nin de artması sağlandı.
        aktar_btn.pack(side=LEFT) #görsel eleman gözüktü. sol tarafa sıkıştı
        secili_sil_btn.pack(side=LEFT)#görsel eleman gözüktü. sol tarafa sıkıştı
        hepsini_sil_btn.pack(side=LEFT)#görsel eleman gözüktü. sol tarafa sıkıştı

    def aktar(self):
        dosya_ismi = fd.askopenfilename()

        with open(dosya_ismi) as dosya:
            veriler = json.load(dosya)
            for veri in veriler:
                #self.harcama_listesi.append(str( veri['isim'])+" " +veri['stok']+" " +veri['marka']+" " +veri['fiyat']+" " +veri['aciklama']+" " +str(veri['kategori'])+" " +veri['link'])
                self.harcama_listesi.append(f"İsim: {str(veri['isim'])} Stok: {veri['stok']} Marka:{veri['marka']} Fiyat:{veri['fiyat']} Aciklama:{veri['aciklama']} Kategori:{str(veri['kategori'])} Link:{veri['link']}")

        for indeks, harcama in enumerate(self.harcama_listesi):
            self.lb.insert(indeks, harcama)

    def secili_sil(self):
        try:
            print("Siliyorum", self.lb.curselection())
            self.lb.delete(self.lb.curselection())
        except TclError:
            print("Ürün seçmediniz!")

    def hepsini_sil(self):
        self.lb.delete(0, END)




