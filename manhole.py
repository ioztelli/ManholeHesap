import ezdxf
import sys

class Manhole:
    def __init__(self,name,gl,il,x,y):
        self.name=name
        self.gl=gl
        self.il=il
        self.x=x
        self.y=y

    def Height(self):
        return round(self.gl-self.il,2)
    def Diameter(self):
        return 1000
        # if self.gl-self.il<=3:
        #     return 1000
        # else:
        #     return 1500

    def Parcahesap(self):
        if self.Diameter()==1000:
            # Sabit Parcalar
            Taban = .95
            Konik = .70
            Kapak = .10
            # Degisken Parcalar
            B1 = .60
            B2 = .40
            B3 = .25
            B4 = .10
            # Maksimum Parcalar
            MB1 = 10
            MB2 = 10
            MB3 = 10
            MB4 = 2  # Ayar Bilezigi
            height=self.Height()
            result = {}
            for x1 in range(MB1):
                for x2 in range(MB2):
                    for x3 in range(MB3):
                        for x4 in range(MB4):
                            kalan = height - Taban - Konik - Kapak - x1 * B1 - x2 * B2 - x3 * B3 - x4 * B4
                            kalan=round(kalan,2)
                            if abs(kalan) < B4:
                                result[kalan] = (x1, x2, x3, x4)
                                #print(str(kalan)+":"+str(result[kalan]))

            closest = min(result, key=lambda x: abs(x - 0))
            return (closest, result[closest])
        else:
            #1500 malzeme icin yazilacak.
            pass

    def bilezikciz1000(self,dwg, msp, xbase, ybase, h):
        isim = "B" + str(h)
        if dwg.blocks.get(isim) == None:
            points_sag = [(0.7, h), (0.7, 0), (0.58, 0),
                          (0.55, 0.03), (0.5, 0.03), (0.5, h + 0.03),
                          (0.55, h + 0.03), (0.58, h), (0.7, h)]
            points_sol = [(-0.7, h), (-0.7, 0), (-0.58, 0),
                          (-0.55, 0.03), (-0.5, 0.03), (-0.5, h + 0.03),
                          (-0.55, h + 0.03), (-0.58, h), (-0.7, h)]

            bilezikblok = dwg.blocks.new(name=isim)
            bilezikblok.add_polyline2d(points_sag)
            bilezikblok.add_polyline2d(points_sol)
        msp.add_blockref(isim, (xbase, ybase))

    def temelciz1000(self,dwg, msp, xbase, ybase):
        isim = 'temel000'
        if dwg.blocks.get(isim) == None:
            points = [(-0.5, 0.25), (-0.5, 1.23), (-0.55, 1.23),
                      (-0.58, 1.2), (-0.7, 1.2), (-0.7, 0),
                      (0.7, 0), (0.7, 1.2), (0.58, 1.2),
                      (0.55, 1.23), (0.5, 1.23), (0.5, 0.25),
                      (-0.5, 0.25)]
            temelblok = dwg.blocks.new(name=isim)
            temelblok.add_polyline2d(points)
        msp.add_blockref(isim, (xbase, ybase))

    def konikciz1000(self,dwg, msp, xbase, ybase):
        isim = 'konik1000'
        if dwg.blocks.get(isim) == None:
            points_sag = [(0.7, 0.15), (0.64, 0.15), (0.59, 0.18),
                          (0.33, 0.7), (0.21, 0.7), (0.18, 0.73),
                          (0.13, 0.73), (0.13, 0.7), (0.5, 0.03),
                          (0.55, 0.03), (0.58, 0), (0.7, 0),
                          (0.7, 0.15)]
            points_sol = [(-0.7, 0.7), (-0.7, 0), (-0.58, 0),
                          (-0.55, 0.03), (-0.5, 0.03), (-0.5, 0.73),
                          (-0.55, 0.73), (-0.58, 0.7), (-0.7, 0.7)]
            konikblok = dwg.blocks.new(name=isim)
            konikblok.add_polyline2d(points_sag)
            konikblok.add_polyline2d(points_sol)
        msp.add_blockref(isim, (xbase, ybase))

    def ayarbilezikciz(self,dwg, msp, xbase, ybase):
        isim = 'ayarbilezik'
        if dwg.blocks.get(isim) == None:
            points_sag = [(0.33, 0.1), (0.33, 0), (0.21, 0),
                          (0.18, 0.03), (0.13, 0.03), (0.13, 0.13),
                          (0.18, 0.13), (0.21, 0.1), (0.33, 0.1)]
            points_sol = [(-0.7, 0.1), (-0.7, 0), (-0.58, 0),
                          (-0.55, 0.03), (-0.5, 0.03), (-0.5, 0.13),
                          (-0.55, 0.13), (-0.58, 0.1), (-0.7, 0.1)]
            ayarblok = dwg.blocks.new(name=isim)
            ayarblok.add_polyline2d(points_sag)
            ayarblok.add_polyline2d(points_sol)
        msp.add_blockref(isim, (xbase, ybase))

    def kapakciz(self,dwg, msp, xbase, ybase):
        isim = 'kapak'
        if dwg.blocks.get(isim) == None:
            points = [(0.33, 0), (0.21, 0), (0.18, 0.03),
                      (-0.55, 0.03), (-0.58, 0), (-0.7, 0),
                      (-0.7, 0.1), (0.32, 0.1), (0.33, 0)]
            kapakblok = dwg.blocks.new(name=isim)
            kapakblok.add_polyline2d(points)
        msp.add_blockref(isim, (xbase, ybase))

    def Ciz(self):
        dwg = ezdxf.new('R2010')
        msp = dwg.modelspace()
        if self.Diameter() == 1000:
            if self.Height() < 1.75:
                print('Hata:Manhole 1.75 den kisadir.')

            parcalar = self.Parcahesap()
            b60 = parcalar[1][0]
            b40 = parcalar[1][1]
            b25 = parcalar[1][2]
            b10 = parcalar[1][3]
            print("MH={0} Kullanilacak parcalar: Temel+60x{1}+40x{2}+25x{3}+10x{4}+Konik+Kapak".format(self.name, str(b60),
                                                                                                       str(b40),
                                                                                                       str(b25),
                                                                                                       str(b10)))
            xbase = 0
            ybase = 0
            self.temelciz1000(dwg,msp, xbase, ybase)
            ybase += 1.2
            while b60 != 0:  # 60cmlik parca
                self.bilezikciz1000(dwg,msp, xbase, ybase, 0.60)
                ybase += 0.6
                b60 = b60 - 1
            while b40 != 0:  # 40cmlik parca
                self.bilezikciz1000(dwg,msp, xbase, ybase, 0.40)
                ybase += 0.4
                b40 = b40 - 1
            while b25 != 0:  # 40cmlik parca
                self.bilezikciz1000(dwg,msp, xbase, ybase, 0.25)
                ybase += 0.25
                b25 = b25 - 1
            self.konikciz1000(dwg,msp, xbase, ybase)
            ybase += 0.70
            while b10 != 0:  # 10cmlik parca
                self.ayarbilezikciz(dwg,msp, xbase, ybase)
                ybase += 0.1
                b10 = b10 - 1
            self.kapakciz(dwg,msp, xbase, ybase)
            # Yazi
            #yazilar = "MH={0} \nKullanilacak parcalar:\nTemel+60x{1}+40x{2}+25x{3}+10x{4}+Konik+Kapak".format(self.name,str(b60),str(b40),str(b25),str(b10))
            dwg.styles.new('custom',dxfattribs={'font': 'times.ttf', 'width': 0.8})  # Arial, default width factor of 0.8
            msp.add_text("MH="+self.name, dxfattribs={'style': 'custom', 'height': 0.14}).set_pos((xbase, ybase+.6), align='CENTER')
            dwg.saveas(sys.path[0]+"/dxf/"+self.name + ".dxf")
        else:
            pass

#mh200=Manhole("100",103,101,423.12,120.00)
#mh200.Ciz()
