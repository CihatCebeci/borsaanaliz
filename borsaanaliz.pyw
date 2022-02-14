from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
class borsaAnaliz(QDialog):
    def __init__(self,parent=None):
        super(borsaAnaliz,self).__init__(parent)
        grid=QGridLayout()
        ###PİVOT HESAPLAMA####################################################################################################################
        self.imii = QPixmap("./destek.png")
        self.labelii = QLabel()
        self.labelii.setPixmap(self.imii)
        grid.addWidget(self.labelii,0,0,1,2)
        grid.addWidget(QLabel("En Yüksek Değer:"),1,0)
        grid.addWidget(QLabel("En Düşük Değer:"),2,0)
        grid.addWidget(QLabel("Kapanış Değeri:"),3,0)
        self.enYuksek=QLineEdit()
        self.enDusuk=QLineEdit()
        self.kapanis=QLineEdit()
        grid.addWidget(self.enYuksek,1,1)
        grid.addWidget(self.enDusuk,2,1)
        grid.addWidget(self.kapanis,3,1)
        butonpivot=QPushButton('Pivot Hesapla')
        grid.addWidget(butonpivot,4,0,1,2)
        butonpivot.clicked.connect(self.pivotHesaplama)
        self.pivot1=(QLabel("<b><font color='blue'>Pivot Değeri:</font></b>"))
        self.pivot12=(QLabel("-----"))
        grid.addWidget(self.pivot12,5,1)
        grid.addWidget(self.pivot1,5,0)
        self.direnc1=(QLabel("<b><font color='red'>1. Direnç Değeri:</b></font>"))
        self.direnc12=(QLabel("-----"))
        grid.addWidget(self.direnc1,6,0)
        grid.addWidget(self.direnc12,6,1)
        self.direnc2=(QLabel("<font color='red'><b>2. Direnç Değeri:</b></font>"))
        self.direnc22=(QLabel("-----"))
        grid.addWidget(self.direnc2,7,0)
        grid.addWidget(self.direnc22,7,1)
        self.destek1=(QLabel("<font color='green'><b>1. Destek Değeri:</b></font>"))
        self.destek12=(QLabel("-----"))
        grid.addWidget(self.destek1,8,0)
        grid.addWidget(self.destek12,8,1)
        self.destek2=(QLabel("<font color='green'><b>2. Destek Değeri:</b></font>"))
        self.destek22=(QLabel("-----"))
        grid.addWidget(self.destek2,9,0)
        grid.addWidget(self.destek22,9,1)
        self.imi = QPixmap("./ayrac.png")
        self.labeli = QLabel()
        self.labeli.setPixmap(self.imi)
        grid.addWidget(self.labeli,10,0,1,2)
        ###PİVOT SONU########################################################################################################################
        ###RSI DEĞERİ########################################################################################################################
        self.imii = QPixmap("./rsi.png")
        self.labelii = QLabel()
        self.labelii.setPixmap(self.imii)
        grid.addWidget(self.labelii,11,0,1,2)
        grid.addWidget(QLabel("Kapanış RSI Değeri:"),12,0)
        grid.addWidget(QLabel("2 Önceki RSI Değeri:"),13,0)
        grid.addWidget(QLabel("3 Önceki RSI Değeri:"),14,0)
        self.rsibir=QLineEdit()
        self.rsiiki=QLineEdit()
        self.rsiuc=QLineEdit()
        grid.addWidget(self.rsibir,12,1)
        grid.addWidget(self.rsiiki,13,1)
        grid.addWidget(self.rsiuc,14,1)
        rsiButon=QPushButton("RSI Puanla")
        grid.addWidget(rsiButon,15,0,1,2)
        rsiButon.clicked.connect(self.rsiHesaplama)
        grid.addWidget(QLabel("<b>RSI Puan:</b> 10 üzerinden <b>---></b>"),16,0)
        self.puanlama=(QLabel("---"))
        grid.addWidget(self.puanlama,16,1)
        self.imi = QPixmap("./ayrac.png")
        self.labeli = QLabel()
        self.labeli.setPixmap(self.imi)
        grid.addWidget(self.labeli,17,0,1,2)
        ###RSI SONU############################################################################################################################
        ###STOCH RSI###########################################################################################################################
        self.imii = QPixmap("./stochrsi.png")
        self.labelii = QLabel()
        self.labelii.setPixmap(self.imii)
        grid.addWidget(self.labelii,18,0,1,2)
        grid.addWidget(QLabel("Kapanış %D (Kırmızı):"),19,0)
        grid.addWidget(QLabel("Kapanış %K (Yeşil):"),20,0)
        grid.addWidget(QLabel("2 Önceki Kapanış %D (Kırmızı):"),21,0)
        grid.addWidget(QLabel("2 Önceki Kapanış %K (Yeşil):"),22,0)
        self.dbir=QLineEdit()
        self.kbir=QLineEdit()
        self.diki=QLineEdit()
        self.kiki=QLineEdit()
        grid.addWidget(self.dbir,19,1)
        grid.addWidget(self.kbir,20,1)
        grid.addWidget(self.diki,21,1)
        grid.addWidget(self.kiki,22,1)
        stokbuton=QPushButton("Stoch RSI Puanla")
        stokbuton.clicked.connect(self.stokRsi)
        grid.addWidget(stokbuton,23,0,1,2)
        grid.addWidget(QLabel("<b>STOCH RSI Puan:</b> 10 üzerinden <b>---></b>"),24,0)
        self.stokpuani=(QLabel("   ---"))
        grid.addWidget(self.stokpuani,24,1)
        ###STOCH RSI SONU#######################################################################################################################
        ###BOLLINGER ÖLÇME######################################################################################################################
        self.imii = QPixmap("./bollinger.png")
        self.labelii = QLabel()
        self.labelii.setPixmap(self.imii)
        grid.addWidget(self.labelii,0,4,1,2)
        grid.addWidget(QLabel("<b>NOT:</b> Pivot hesaplamadaki kapanış değeri doldurulmalıdır."),1,4,1,2)
        grid.addWidget(QLabel("Bollinger üst kapanış:"),2,4)
        grid.addWidget(QLabel("Bollinger orta kapanış:"),3,4)
        grid.addWidget(QLabel("Bollinger alt kapanış:"),4,4)
        grid.addWidget(QLabel("Bant Kesiyor Mu? <b>E/H:</b>"),5,4)
        self.bollUst=QLineEdit()
        self.bollOrta=QLineEdit()
        self.bollAlt=QLineEdit()
        self.kesme=QLineEdit()
        grid.addWidget(self.kesme,5,5)
        grid.addWidget(self.bollUst,2,5)
        grid.addWidget(self.bollOrta,3,5)
        grid.addWidget(self.bollAlt,4,5)
        bollButon=QPushButton("Bollinger Puanla")
        bollButon.clicked.connect(self.bollHesap)
        grid.addWidget(bollButon,6,4,1,2)
        grid.addWidget(QLabel("<b>Bollinger Notu:</b> 10 üzerinden <b>---></b>"),7,4)
        self.bollPuani=(QLabel("   ---"))
        grid.addWidget(self.bollPuani,7,5)
        self.imi = QPixmap("./ayrac.png")
        self.labeli = QLabel()
        self.labeli.setPixmap(self.imi)
        grid.addWidget(self.labeli,8,4,1,2)
        ###BOLLINGER ÖLÇME SONU###################################################################################################################
        ###AROON TREND ANALİZİ####################################################################################################################
        self.imii = QPixmap("./aroon.png")
        self.labelii = QLabel()
        self.labelii.setPixmap(self.imii)
        grid.addWidget(self.labelii,9,4,1,2)
        grid.addWidget(QLabel("Upper(Turuncu) Kapanış Değeri:"),10,4)
        grid.addWidget(QLabel("Lower(Mavi) Kapanış Değeri:"),11,4)
        grid.addWidget(QLabel("Trend Uzunluğu:"),12,4)
        self.turuncuDeger=QLineEdit()
        self.maviDeger=QLineEdit()
        self.trendDegeri=QLineEdit()
        grid.addWidget(self.turuncuDeger,10,5)
        grid.addWidget(self.maviDeger,11,5)
        grid.addWidget(self.trendDegeri,12,5)
        aroonButon=QPushButton("Trend Puanla")
        aroonButon.clicked.connect(self.aroonHesap)
        grid.addWidget(aroonButon,13,4,1,2)
        grid.addWidget(QLabel("<b>Aroon Trend Kalitesi:</b> 10 üzerinden <b>---></b>"),14,4)
        self.aroonPuani=(QLabel("   ---"))
        grid.addWidget(self.aroonPuani,14,5)
        self.imi = QPixmap("./ayrac.png")
        self.labeli = QLabel()
        self.labeli.setPixmap(self.imi)
        grid.addWidget(self.labeli,15,4,1,2)
        ###AROON TREND ANALİZİ SONU#################################################################################################################
        ###MACD TREND ANALİZİ#######################################################################################################################
        self.imii = QPixmap("./macd.png")
        self.labelii = QLabel()
        self.labelii.setPixmap(self.imii)
        grid.addWidget(self.labelii,16,4,1,2)
        grid.addWidget(QLabel("Son Histogram Değeri:"),17,4)
        grid.addWidget(QLabel("Bir Önceki Histogram Değeri:"),18,4)
        grid.addWidget(QLabel("Trend Uzunluğu:"),19,4)
        self.sonDeger=QLineEdit()
        self.oncekiDeger=QLineEdit()
        self.trendUzunluk=QLineEdit()
        grid.addWidget(self.sonDeger,17,5)
        grid.addWidget(self.oncekiDeger,18,5)
        grid.addWidget(self.trendUzunluk,19,5)
        macdbuton=QPushButton("Macd Ölç")
        grid.addWidget(macdbuton,20,4,1,2)
        macdbuton.clicked.connect(self.macdHesaplama)
        grid.addWidget(QLabel("<b>Macd Puanlaması:</b> 10 üzerinden <b>---></b>"),21,4)
        self.macdPuani=(QLabel("   ---"))
        grid.addWidget(self.macdPuani,21,5)
        self.imi = QPixmap("./ayrac.png")
        self.labeli = QLabel()
        self.labeli.setPixmap(self.imi)
        grid.addWidget(self.labeli,22,4,1,2)
        ###MACD TREND ANALİZİ SONU###################################################################################################################
        self.im = QPixmap("./foto1.png")
        self.label = QLabel()
        self.label.setPixmap(self.im)
        grid.addWidget(self.label,23,4,1,2)
        ###SAR DEĞERİ ÖLÇME##########################################################################################################################
        self.imii = QPixmap("./sar.png")
        self.labelii = QLabel()
        self.labelii.setPixmap(self.imii)
        grid.addWidget(self.labelii,0,7,1,2)
        grid.addWidget(QLabel("<b>NOT:</b> Pivot hesaplamadaki kapanış değeri doldurulmalıdır."),1,7,1,2)
        grid.addWidget(QLabel("Son Sar Değeri:"),2,7)
        grid.addWidget(QLabel("Trend Uzunluğu:"),3,7)
        self.sarDegeri=QLineEdit()
        self.sarTrendi=QLineEdit()
        grid.addWidget(self.sarDegeri,2,8)
        grid.addWidget(self.sarTrendi,3,8)
        sarButon=QPushButton("Sar Ölç")
        sarButon.clicked.connect(self.sarHesaplama)
        grid.addWidget(sarButon,4,7,1,2)
        grid.addWidget(QLabel("<b>Sar Değeri:</b> 10 üzerinden <b>---></b>"),5,7)
        self.sarPuani=(QLabel("   ---"))
        grid.addWidget(self.sarPuani,5,8)
        self.imi = QPixmap("./ayrac1.png")
        self.labeli = QLabel()
        self.labeli.setPixmap(self.imi)
        grid.addWidget(self.labeli,6,7,1,2)
        ###SAR DEĞERİ SONU############################################################################################################################
        ###ANALİZ TAMAMLAMA###########################################################################################################################
        self.imii = QPixmap("./tamamlama.png")
        self.labelii = QLabel()
        self.labelii.setPixmap(self.imii)
        grid.addWidget(self.labelii,7,7,1,2)
        grid.addWidget(QLabel("<b>NOT:</b> Bu işlemi yapmadan önce tüm analizleri yapın."),8,7,1,2)
        grid.addWidget(QLabel("Coin/Hisse Adı:"),9,7)
        grid.addWidget(QLabel("RSI Puanı:"),10,7)
        grid.addWidget(QLabel("STOCH RSI Puanı:"),11,7)
        grid.addWidget(QLabel("Bollinger Notu:"),12,7)
        grid.addWidget(QLabel("Aroon Kalite Notu:"),13,7)
        grid.addWidget(QLabel("Macd Puanlaması:"),14,7)
        grid.addWidget(QLabel("Sar Değeri:"),15,7)
        self.coinAdi=QLineEdit()
        self.rsiDeger=QLineEdit()
        self.stochrsiDeger=QLineEdit()
        self.bollingerDeger=QLineEdit()
        self.aroonDeger=QLineEdit()
        self.macdDeger=QLineEdit()
        self.sarDeger=QLineEdit()
        grid.addWidget(self.coinAdi,9,8)
        grid.addWidget(self.rsiDeger,10,8)
        grid.addWidget(self.stochrsiDeger,11,8)
        grid.addWidget(self.bollingerDeger,12,8)
        grid.addWidget(self.aroonDeger,13,8)
        grid.addWidget(self.macdDeger,14,8)
        grid.addWidget(self.sarDeger,15,8)
        sonucButon=QPushButton("Analizi Tamamla")
        grid.addWidget(sonucButon,16,7,1,2)
        sonucButon.clicked.connect(self.sonucHesaplama)
        grid.addWidget(QLabel("<h3>SONUÇ:</h3>"),17,7)
        self.sonucBir=(QLabel("Sonucunuz Burada Gözükecek."))
        self.sonucKi=(QLabel("Borsa Analiz V3.0"))
        self.sonucUc=(QLabel("Bu Program Cihat Cebeci tarafından kodlanmıştır."))
        self.sonucDort=(QLabel("Kopyalanması ve paylaşılması yasaktır."))
        self.sonucBes=(QLabel("Bu bir teknik analiz programıdır, %100 doğru sonuç verme garantisi yoktur."))
        self.sonucAlti=(QLabel("Borsa Analiz V3.0'ı kullandığınız için teşekkürler."))
        grid.addWidget(self.sonucBir,18,7,1,2)
        grid.addWidget(self.sonucKi,19,7,1,2)
        grid.addWidget(self.sonucUc,20,7,1,2)
        grid.addWidget(self.sonucDort,21,7,1,2)
        grid.addWidget(self.sonucBes,22,7,1,2)
        grid.addWidget(self.sonucAlti,23,7,1,2)
        hakkindaButon=QPushButton("Hakkında")
        grid.addWidget(hakkindaButon,24,7)
        bilgiButon=QPushButton("Bilgi")
        grid.addWidget(bilgiButon,24,8)
        ###
        grid.addWidget(QLabel("<h2>|</h2>"),0,3)
        grid.addWidget(QLabel("<h2>|</h2>"),1,3)
        grid.addWidget(QLabel("<h2>|</h2>"),2,3)
        grid.addWidget(QLabel("<h2>|</h2>"),3,3)
        grid.addWidget(QLabel("<h2>|</h2>"),4,3)
        grid.addWidget(QLabel("<h2>|</h2>"),5,3)
        grid.addWidget(QLabel("<h2>|</h2>"),6,3)
        grid.addWidget(QLabel("<h2>|</h2>"),7,3)
        grid.addWidget(QLabel("<h2>|</h2>"),8,3)
        grid.addWidget(QLabel("<h2>|</h2>"),9,3)
        grid.addWidget(QLabel("<h2>|</h2>"),10,3)
        grid.addWidget(QLabel("<h2>|</h2>"),11,3)
        grid.addWidget(QLabel("<h2>|</h2>"),12,3)
        grid.addWidget(QLabel("<h2>|</h2>"),13,3)
        grid.addWidget(QLabel("<h2>|</h2>"),14,3)
        grid.addWidget(QLabel("<h2>|</h2>"),15,3)
        grid.addWidget(QLabel("<h2>|</h2>"),16,3)
        grid.addWidget(QLabel("<h2>|</h2>"),17,3)
        grid.addWidget(QLabel("<h2>|</h2>"),18,3)
        grid.addWidget(QLabel("<h2>|</h2>"),19,3)
        grid.addWidget(QLabel("<h2>|</h2>"),20,3)
        grid.addWidget(QLabel("<h2>|</h2>"),21,3)
        grid.addWidget(QLabel("<h2>|</h2>"),22,3)
        grid.addWidget(QLabel("<h2>|</h2>"),23,3)
        grid.addWidget(QLabel("<h2>|</h2>"),24,3)
        grid.addWidget(QLabel("<h2>|</h2>"),0,6)
        grid.addWidget(QLabel("<h2>|</h2>"),1,6)
        grid.addWidget(QLabel("<h2>|</h2>"),2,6)
        grid.addWidget(QLabel("<h2>|</h2>"),3,6)
        grid.addWidget(QLabel("<h2>|</h2>"),4,6)
        grid.addWidget(QLabel("<h2>|</h2>"),5,6)
        grid.addWidget(QLabel("<h2>|</h2>"),6,6)
        grid.addWidget(QLabel("<h2>|</h2>"),7,6)
        grid.addWidget(QLabel("<h2>|</h2>"),8,6)
        grid.addWidget(QLabel("<h2>|</h2>"),9,6)
        grid.addWidget(QLabel("<h2>|</h2>"),10,6)
        grid.addWidget(QLabel("<h2>|</h2>"),11,6)
        grid.addWidget(QLabel("<h2>|</h2>"),12,6)
        grid.addWidget(QLabel("<h2>|</h2>"),13,6)
        grid.addWidget(QLabel("<h2>|</h2>"),14,6)
        grid.addWidget(QLabel("<h2>|</h2>"),15,6)
        grid.addWidget(QLabel("<h2>|</h2>"),16,6)
        grid.addWidget(QLabel("<h2>|</h2>"),17,6)
        grid.addWidget(QLabel("<h2>|</h2>"),18,6)
        grid.addWidget(QLabel("<h2>|</h2>"),19,6)
        grid.addWidget(QLabel("<h2>|</h2>"),20,6)
        grid.addWidget(QLabel("<h2>|</h2>"),21,6)
        grid.addWidget(QLabel("<h2>|</h2>"),22,6)
        grid.addWidget(QLabel("<h2>|</h2>"),23,6)
        grid.addWidget(QLabel("<h2>|</h2>"),24,6)
        ###
        oImage = QImage("background.jpg")
        sImage = oImage.scaled(QSize(1200,740))  
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        ###
        self.setWindowIcon(QIcon('icon.png'))
        self.setLayout(grid)
        self.setWindowTitle("Borsa Analiz V3.0")
    def pivotHesaplama(self):
        enYuksek=self.enYuksek.text()
        enYuksek=float(enYuksek)
        enDusuk=self.enDusuk.text()
        enDusuk=float(enDusuk)
        kapanis=self.kapanis.text()
        kapanis=float(kapanis)
        pivot=(enYuksek+enDusuk+kapanis)/3
        ilkDestek=(2*pivot)-enYuksek
        ilkDirenc=(2*pivot)-enDusuk
        ikinciDestek=pivot-(ilkDirenc-ilkDestek)
        ikinciDirenc=pivot+(ilkDirenc-ilkDestek)
        pivotDegeri=str(pivot)
        self.pivot12.setText(pivotDegeri)
        direncDegeri=str(ilkDirenc)
        self.direnc12.setText(direncDegeri)
        direnc2Degeri=str(ikinciDirenc)
        self.direnc22.setText(direnc2Degeri)
        destekDegeri=str(ilkDestek)
        self.destek12.setText(destekDegeri)
        destek2Degeri=str(ikinciDestek)
        self.destek22.setText(destek2Degeri)
    def rsiHesaplama(self):
        rsiPuan=0
        ilkRsi=self.rsibir.text()
        ilkRsi=float(ilkRsi)
        ikinciRsi=self.rsiiki.text()
        ikinciRsi=float(ikinciRsi)
        ucuncuRsi=self.rsiuc.text()
        ucuncuRsi=float(ucuncuRsi)
        rsiOrtalama=(ilkRsi+ikinciRsi+ucuncuRsi)/3
        if ilkRsi<=30:
            if ilkRsi<20:
                rsiPuan+=9
            elif ilkRsi<10:
                rsiPuan+=10
            else:
                rsiPuan+=8
        elif ilkRsi>=70:
            if ilkRsi>80:
                rsiPuan+=1
            elif ikinciRsi>90:
                rsiPuan+=0
            else:
                rsiPuan+=2
        else:
            if 40>rsiOrtalama>30:
                if ikinciRsi>ilkRsi:
                    if ucuncuRsi>ikinciRsi:
                        rsiPuan+=1
                    elif ikinciRsi>ucuncuRsi:
                        rsiPuan+=2
                    else:
                        rsiPuan+=3
                else:
                    if ucuncuRsi>ikinciRsi:
                        rsiPuan+=4
                    elif ikinciRsi>ucuncuRsi:
                        rsiPuan+=7
                    else:
                        rsiPuan+=6
            elif 50>rsiOrtalama>40:
                if ikinciRsi>ilkRsi:
                    if ucuncuRsi>ikinciRsi:
                        rsiPuan+=1
                    elif ikinciRsi>ucuncuRsi:
                        rsiPuan+=2
                    else:
                        rsiPuan+=3
                else:
                    if ucuncuRsi>ikinciRsi:
                        rsiPuan+=4
                    elif ikinciRsi>ucuncuRsi:
                        rsiPuan+=7
                    else:
                        rsiPuan+=5
            elif 60>rsiOrtalama>50:
                if ikinciRsi>ilkRsi:
                    if ucuncuRsi>ikinciRsi:
                        rsiPuan+=1
                    elif ikinciRsi>ucuncuRsi:
                        rsiPuan+=2
                    else:
                        rsiPuan+=3
                else:
                    if ucuncuRsi>ikinciRsi:
                        rsiPuan+=4
                    elif ikinciRsi>ucuncuRsi:
                        rsiPuan+=8
                    else:
                        rsiPuan+=6
            elif 70>rsiOrtalama>60:
                if ikinciRsi>ilkRsi:
                    if ucuncuRsi>ikinciRsi:
                        rsiPuan+=1
                    elif ikinciRsi>ucuncuRsi:
                        rsiPuan+=3
                    else:
                        rsiPuan+=4
                else:
                    if ucuncuRsi>ikinciRsi:
                        rsiPuan+=3
                    elif ikinciRsi>ucuncuRsi:
                        rsiPuan+=7
                    else:
                        rsiPuan+=6
        rsiPuan=str(rsiPuan)
        self.puanlama.setText(rsiPuan)
    def stokRsi(self):
        stokpuan=0
        ilkKirmizi=self.dbir.text()
        ilkKirmizi=float(ilkKirmizi)
        ikinciKirmizi=self.diki.text()
        ikinciKirmizi=float(ikinciKirmizi)
        ilkYesil=self.kbir.text()
        ilkYesil=float(ilkYesil)
        ikinciYesil=self.kiki.text()
        ikinciYesil=float(ikinciYesil)
        ortalamaStok=(ilkKirmizi+ilkYesil+ikinciYesil+ikinciKirmizi)/4
        ilkOrtalama=(ilkKirmizi+ilkYesil)/2
        ikinciOrtalama=(ikinciKirmizi+ikinciYesil)/2
        if ilkOrtalama>ikinciOrtalama:
            if 80>ilkOrtalama>=60:
                stokpuan+=8
            elif 60>ilkOrtalama>40:
                stokpuan+=6
            elif 20<ilkOrtalama<=40:
                stokpuan+=5
            elif ilkOrtalama>=80:
                stokpuan+=10
            elif ilkOrtalama<=20:
                stokpuan+=8
        elif ikinciOrtalama>ilkOrtalama:
            if ilkOrtalama>=60:
                stokpuan+=5
            elif 60>ilkOrtalama>40:
                stokpuan+=3
            elif 20<ilkOrtalama<=40:
                stokpuan+=1
            elif 10<ilkOrtalama<=20:
                stokpuan+=2
            elif ilkOrtalama<=10:
                stokpuan+=4
        else:
            if ortalamaStok>=80:
                stokpuan+=8
            elif 80>ortalamaStok>40:
                stokpuan+=5
            elif 40>=ortalamaStok>20:
                stokpuan+=8
            elif ortalamaStok<=20:
                stokpuan+=7
        stokpuan=str(stokpuan)
        self.stokpuani.setText(stokpuan)
    def bollHesap(self):
        bollPuan=0
        bollSon=self.bollUst.text()
        bollSon=float(bollSon)
        bollOrtalama=self.bollOrta.text()
        bollOrtalama=float(bollOrtalama)
        bollAlt=self.bollAlt.text()
        bollAlt=float(bollAlt)
        kapanisbir=self.kapanis.text()
        kapanisbir=float(kapanisbir)
        kesim=self.kesme.text()
        kesim=str(kesim)
        if kapanisbir>=bollSon:
            if kesim=="E":
                bollPuan+=9
            elif kesim=="H":
                bollpuan+=2
            else:
                self.bollPuani.setText("Hatalı İşlem Yapıldı")
        elif bollAlt>=kapanisbir:
            if kesim=="E":
                bollPuan+=3
            elif kesim=="H":
                bollPuan+=8
        elif bollOrtalama>=kapanisbir>bollAlt:
            if kesim=="E":
                bollPuan+=5
            elif kesim=="H":
                bollPuan+=3
            else:
                self.bollPuani.setText("Hatalı İşlem Yapıldı")
        elif bollSon>kapanisbir>bollOrtalama:
            if kesim=="E":
                bollPuan+=6
            elif kesim=="H":
                bollPuan+=7
            else:
                self.bollPuani.setText("Hatalı İşlem Yapıldı")
        else:
            self.bollPuani.setText("Hatalı İşlem Yapıldı")
        bollPuan=str(bollPuan)
        self.bollPuani.setText(bollPuan)
    def aroonHesap(self):
        aroonPuan=0
        turuncu=self.turuncuDeger.text()
        turuncu=float(turuncu)
        mavi=self.maviDeger.text()
        mavi=float(mavi)
        trend=self.trendDegeri.text()
        trend=int(trend)
        if mavi>turuncu:
            if mavi>=70:
                if 2>=trend:
                    aroonPuan+=1
                elif 5>=trend>2:
                    aroonPuan+=2
                elif 10>=trend>5:
                    aroonPuan+=3
                elif trend>10:
                    aroonPuan+=4
            elif 70>mavi>30:
                if 2>=trend:
                    aroonPuan+=2
                elif 5>=trend>2:
                    aroonPuan+=3
                elif 10>=trend>5:
                    aroonPuan+=4
                elif trend>10:
                    aroonPuan+=6
            elif 30>=mavi:
                if 2>=trend:
                    aroonPuan+=4
                elif 5>=trend>2:
                    aroonPuan+=5
                elif 10>=trend>5:
                    aroonPuan+=6
                elif trend>10:
                    aroonPuan+=7
        elif turuncu>mavi:
            if turuncu>=70:
                if 2>=trend:
                    aroonPuan+=10
                elif 5>=trend>2:
                    aroonPuan+=8
                elif 10>=trend>5:
                    aroonPuan+=6
                elif trend>10:
                    aroonPuan+=5
            elif 70>turuncu>30:
                if 2>=trend:
                    aroonPuan+=9
                elif 5>=trend>2:
                    aroonPuan+=6
                elif 10>=trend>5:
                    aroonPuan+=4
                elif trend>10:
                    aroonPuan+=3
            elif 30>=turuncu:
                if 2>=trend:
                    aroonPuan+=6
                elif 5>=trend>2:
                    aroonPuan+=5
                elif 10>=trend>5:
                    aroonPuan+=4
                elif trend>10:
                    aroonPuan+=2
        else:
            aroonPuan+=5
        aroonPuan=str(aroonPuan)
        self.aroonPuani.setText(aroonPuan)
    def macdHesaplama(self):
        macdPuan=0
        son=self.sonDeger.text()
        son=float(son)
        onceki=self.oncekiDeger.text()
        onceki=float(onceki)
        trendSon=self.trendUzunluk.text()
        trendSon=int(trendSon)
        if son>onceki:
            if son<0:
                macdPuan+=9
            elif son==0:
                macdPuan+=5
            elif son>0:
                if 2>=trendSon:
                    macdPuan+=8
                elif 5>=trendSon>2:
                    macdPuan+=7
                elif 10>=trendSon>5:
                    macdPuan+=6
                elif trend>10:
                    macdPuan+=5
        elif onceki>son:
            if son<0:
                macdPuan+=3
            elif son==0:
                macdPuan+=5
            elif son>0:
                macdPuan+=1
        else:
            macdPuan+=5
        macdPuan=str(macdPuan)
        self.macdPuani.setText(macdPuan)
    def sarHesaplama(self):
        sarPuan=0
        sarDeger=self.sarDegeri.text()
        sarDeger=float(sarDeger)
        sarTrend=self.sarTrendi.text()
        sarTrend=float(sarTrend)
        kapanisiki=self.kapanis.text()
        kapanisiki=float(kapanisiki)
        if kapanisiki>sarDeger:
            if 2>=sarTrend:
                sarPuan+=9
            elif 5>=sarTrend>2:
                sarPuan+=7
            elif 10>=sarTrend>5:
                sarPuan+=6
            elif 20>=sarTrend>10:
                sarPuan+=4
            elif sarTrend>20:
                sarPuan+=2
        elif sarDeger>kapanisiki:
            if 2>=sarTrend:
                sarPuan+=2
            elif 5>=sarTrend>2:
                sarPuan+=4
            elif 10>=sarTrend>5:
                sarPuan+=6
            elif 20>=sarTrend>10:
                sarPuan+=8
            elif sarTrend>20:
                sarPuan+=9
        else:
            sarPuan+=5
        sarPuan=str(sarPuan)
        self.sarPuani.setText(sarPuan)
    def sonucHesaplama(self):
        coin=self.coinAdi.text()
        coin=str(coin)
        rsiDegeri=self.rsiDeger.text()
        rsiDegeri=float(rsiDegeri)
        stochRsiDegeri=self.stochrsiDeger.text()
        stochRsiDegeri=float(stochRsiDegeri)
        bollingerDegeri=self.bollingerDeger.text()
        bollingerDegeri=float(bollingerDegeri)
        aroonDegeri=self.aroonDeger.text()
        aroonDegeri=float(aroonDegeri)
        macdDegeri=self.macdDeger.text()
        macdDegeri=float(macdDegeri)
        sarDegeri=self.sarDeger.text()
        sarDegeri=float(sarDegeri)
        ###PİVOT DEĞERLERİ###
        enYuksek=self.enYuksek.text()
        enYuksek=float(enYuksek)
        enDusuk=self.enDusuk.text()
        enDusuk=float(enDusuk)
        kapanis=self.kapanis.text()
        kapanis=float(kapanis)
        pivot=(enYuksek+enDusuk+kapanis)/3
        ilkDestek=(2*pivot)-enYuksek
        ilkDirenc=(2*pivot)-enDusuk
        ikinciDestek=pivot-(ilkDirenc-ilkDestek)
        ikinciDirenc=pivot+(ilkDirenc-ilkDestek)
        ###PİVOT DEĞERLERİ###
        toplama=(rsiDegeri+stochRsiDegeri+bollingerDegeri+aroonDegeri+macdDegeri+sarDegeri)
        yuzde=(100*toplama)/60
        setreicin=float(yuzde)
        yuzde=(str(yuzde))
        sonuclamaBir=(coin,"Biriminin analizlere Göre Yükselme Olasılığı: %",yuzde)
        sonuclamaBir=(str(sonuclamaBir))
        sonuclamaBir=sonuclamaBir.replace("(",'')
        sonuclamaBir=sonuclamaBir.replace(")",'')
        sonuclamaBir=sonuclamaBir.replace("'",'')
        sonuclamaBir=sonuclamaBir.replace(",",'')
        self.sonucBir.setText(sonuclamaBir)
        if 50>setreicin:
            sonuclamaKi=("Verilere Göre Düşme İhtimali Daha Yüksek. Beklemeniz daha iyi olacak.")
            sonuclamaKi=(str(sonuclamaKi))
            sonuclamaKi=sonuclamaKi.replace("(",'')
            sonuclamaKi=sonuclamaKi.replace(")",'')
            sonuclamaKi=sonuclamaKi.replace("'",'')
            sonuclamaKi=sonuclamaKi.replace(",",'')
            self.sonucKi.setText(sonuclamaKi)
            sonuclamaUc=(ilkDestek,"veya",ikinciDestek,"değerlerine yaklaşınca tekrar test yapın.")
            sonuclamaUc=(str(sonuclamaUc))
            sonuclamaUc=sonuclamaUc.replace("(",'')
            sonuclamaUc=sonuclamaUc.replace(")",'')
            sonuclamaUc=sonuclamaUc.replace("'",'')
            sonuclamaUc=sonuclamaUc.replace(",",'')
            self.sonucUc.setText(sonuclamaUc)
            sonuclamaDort=(ilkDirenc,"veya",ikinciDirenc,"değerlerine yaklaşınca trend değişimi olabilir.")
            sonuclamaDort=(str(sonuclamaDort))
            sonuclamaDort=sonuclamaDort.replace("(",'')
            sonuclamaDort=sonuclamaDort.replace(")",'')
            sonuclamaDort=sonuclamaDort.replace("'",'')
            sonuclamaDort=sonuclamaDort.replace(",",'')
            self.sonucDort.setText(sonuclamaDort)
        elif setreicin>50:
            sonuclamaKi=("Verilere Göre Yükselme İhtimali Daha Yüksek. Alım yapmayı düşünebilirsiniz.")
            sonuclamaKi=(str(sonuclamaKi))
            sonuclamaKi=sonuclamaKi.replace("(",'')
            sonuclamaKi=sonuclamaKi.replace(")",'')
            sonuclamaKi=sonuclamaKi.replace("'",'')
            sonuclamaKi=sonuclamaKi.replace(",",'')
            self.sonucKi.setText(sonuclamaKi)
            sonuclamaUc=(ilkDestek,"veya",ikinciDestek,"değerlerine yaklaşınca alım yapmayı düşünebilirsiniz.")
            sonuclamaUc=(str(sonuclamaUc))
            sonuclamaUc=sonuclamaUc.replace("(",'')
            sonuclamaUc=sonuclamaUc.replace(")",'')
            sonuclamaUc=sonuclamaUc.replace("'",'')
            sonuclamaUc=sonuclamaUc.replace(",",'')
            self.sonucUc.setText(sonuclamaUc)
            sonuclamaDort=(ilkDirenc,"veya",ikinciDirenc,"değerlerini geçince pump etkisi olabilir.")
            sonuclamaDort=(str(sonuclamaDort))
            sonuclamaDort=sonuclamaDort.replace("(",'')
            sonuclamaDort=sonuclamaDort.replace(")",'')
            sonuclamaDort=sonuclamaDort.replace("'",'')
            sonuclamaDort=sonuclamaDort.replace(",",'')
            self.sonucDort.setText(sonuclamaDort)
        elif setreicin==50:
            sonuclamaKi=("Verilere Göre analiz durumu Nötr. Analiz hareket tahmini yapamıyor.")
            sonuclamaKi=(str(sonuclamaKi))
            sonuclamaKi=sonuclamaKi.replace("(",'')
            sonuclamaKi=sonuclamaKi.replace(")",'')
            sonuclamaKi=sonuclamaKi.replace("'",'')
            sonuclamaKi=sonuclamaKi.replace(",",'')
            self.sonucKi.setText(sonuclamaKi)
            sonuclamaUc=(ilkDestek,"veya",ilkDirenc,"değerlerine yaklaşınca tekrar test yapın.")
            sonuclamaUc=(str(sonuclamaUc))
            sonuclamaUc=sonuclamaUc.replace("(",'')
            sonuclamaUc=sonuclamaUc.replace(")",'')
            sonuclamaUc=sonuclamaUc.replace("'",'')
            sonuclamaUc=sonuclamaUc.replace(",",'')
            self.sonucUc.setText(sonuclamaUc)
            sonuclamaDort=(ikinciDirenc,"veya",ikinciDestek,"değerleri trend yönünü belirleyecek.")
            sonuclamaDort=(str(sonuclamaDort))
            sonuclamaDort=sonuclamaDort.replace("(",'')
            sonuclamaDort=sonuclamaDort.replace(")",'')
            sonuclamaDort=sonuclamaDort.replace("'",'')
            sonuclamaDort=sonuclamaDort.replace(",",'')
            self.sonucDort.setText(sonuclamaDort)
app=QApplication([])
pencere=borsaAnaliz()
pencere.show()
app.exec_()
