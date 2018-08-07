from dxfwrite import DXFEngine as dxf

class Manhole:
    def __init__(self,name,gl,il,x,y):
        self.name=name
        self.gl=gl
        self.il=il
        self.x=x
        self.y=y

    def Height(self):
        return self.gl-self.il
    def Diameter(self):
        if self.gl-self.il<3:
            return 1000
        else:
            return 1500

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

    def temelciz1000(self,dwg, xbase, ybase):
        # Cadtoolsdan alindi.
        points = [(-0.5 + xbase, 0.25 + ybase), (-0.5 + xbase, 1.23 + ybase), (-0.55 + xbase, 1.23 + ybase),
                  (-0.58 + xbase, 1.2 + ybase), (-0.7 + xbase, 1.2 + ybase), (-0.7 + xbase, 0 + ybase),
                  (0.7 + xbase, 0 + ybase), (0.7 + xbase, 1.2 + ybase), (0.58 + xbase, 1.2 + ybase),
                  (0.55 + xbase, 1.23 + ybase), (0.5 + xbase, 1.23 + ybase), (0.5 + xbase, 0.25 + ybase),
                  (-0.5 + xbase, 0.25 + ybase)]
        polyline = dxf.polyline(points)
        dwg.add(polyline)

    def bilezikciz1000(self,dwg, xbase, ybase, h):
        points_sag = [(0.7 + xbase, h + ybase), (0.7 + xbase, 0 + ybase), (0.58 + xbase, 0 + ybase),
                      (0.55 + xbase, 0.03 + ybase), (0.5 + xbase, 0.03 + ybase), (0.5 + xbase, h + 0.03 + ybase),
                      (0.55 + xbase, h + 0.03 + ybase), (0.58 + xbase, h + ybase), (0.7 + xbase, h + ybase)]
        points_sol = [(-0.7 + xbase, h + ybase), (-0.7 + xbase, 0 + ybase), (-0.58 + xbase, 0 + ybase),
                      (-0.55 + xbase, 0.03 + ybase), (-0.5 + xbase, 0.03 + ybase), (-0.5 + xbase, h + 0.03 + ybase),
                      (-0.55 + xbase, h + 0.03 + ybase), (-0.58 + xbase, h + ybase), (-0.7 + xbase, h + ybase)]
        polyline_sag = dxf.polyline(points_sag)
        polyline_sol = dxf.polyline(points_sol)
        dwg.add(polyline_sag)
        dwg.add(polyline_sol)

    def konikciz1000(self,dwg, xbase, ybase):
        points_sag = [(0.7 + xbase, 0.15 + ybase), (0.64 + xbase, 0.15 + ybase), (0.59 + xbase, 0.18 + ybase),
                      (0.33 + xbase, 0.7 + ybase), (0.21 + xbase, 0.7 + ybase), (0.18 + xbase, 0.73 + ybase),
                      (0.13 + xbase, 0.73 + ybase), (0.13 + xbase, 0.7 + ybase), (0.5 + xbase, 0.03 + ybase),
                      (0.55 + xbase, 0.03 + ybase), (0.58 + xbase, 0 + ybase), (0.7 + xbase, 0 + ybase),
                      (0.7 + xbase, 0.15 + ybase)]
        points_sol = [(-0.7 + xbase, 0.7 + ybase), (-0.7 + xbase, 0 + ybase), (-0.58 + xbase, 0 + ybase),
                      (-0.55 + xbase, 0.03 + ybase), (-0.5 + xbase, 0.03 + ybase), (-0.5 + xbase, 0.73 + ybase),
                      (-0.55 + xbase, 0.73 + ybase), (-0.58 + xbase, 0.7 + ybase), (-0.7 + xbase, 0.7 + ybase)]
        polyline_sag = dxf.polyline(points_sag)
        polyline_sol = dxf.polyline(points_sol)
        dwg.add(polyline_sag)
        dwg.add(polyline_sol)

    def ayarbilezikciz(self,dwg, xbase, ybase):
        points_sag = [(0.33 + xbase, 0.1 + ybase), (0.33 + xbase, 0 + ybase), (0.21 + xbase, 0 + ybase),
                      (0.18 + xbase, 0.03 + ybase), (0.13 + xbase, 0.03 + ybase), (0.13 + xbase, 0.13 + ybase),
                      (0.18 + xbase, 0.13 + ybase), (0.21 + xbase, 0.1 + ybase), (0.33 + xbase, 0.1 + ybase)]
        points_sol = [(-0.7 + xbase, 0.1 + ybase), (-0.7 + xbase, 0 + ybase), (-0.58 + xbase, 0 + ybase),
                      (-0.55 + xbase, 0.03 + ybase), (-0.5 + xbase, 0.03 + ybase), (-0.5 + xbase, 0.13 + ybase),
                      (-0.55 + xbase, 0.13 + ybase), (-0.58 + xbase, 0.1 + ybase), (-0.7 + xbase, 0.1 + ybase)]
        polyline_sag = dxf.polyline(points_sag)
        polyline_sol = dxf.polyline(points_sol)
        dwg.add(polyline_sag)
        dwg.add(polyline_sol)

    def kapakciz(self,dwg, xbase, ybase):
        points = [(0.33 + xbase, 0 + ybase), (0.21 + xbase, 0 + ybase), (0.18 + xbase, 0.03 + ybase),
                  (-0.55 + xbase, 0.03 + ybase), (-0.58 + xbase, 0 + ybase), (-0.7 + xbase, 0 + ybase),
                  (-0.7 + xbase, 0.1 + ybase), (0.32 + xbase, 0.1 + ybase), (0.33 + xbase, 0 + ybase)]
        polyline = dxf.polyline(points)
        dwg.add(polyline)

    def Ciz(self):
        if self.Diameter() == 1000:
            if self.Height() < 175:
                print('Hata!!')

            parcalar = self.Parcahesap()
            b60 = parcalar[1][0]
            b40 = parcalar[1][1]
            b25 = parcalar[1][2]
            b10 = parcalar[1][3]
            print("MH={0} Kullanilacak parcalar: Temel+60x{1}+40x{2}+25x{3}+10x{4}+Konik+Kapak".format(self.name, str(b60),
                                                                                                       str(b40),
                                                                                                       str(b25),
                                                                                                       str(b10)))
            dwg = dxf.drawing(self.name + ".dxf")
            xbase = 0
            ybase = 0
            self.temelciz1000(dwg, xbase, ybase)
            ybase += 1.2
            while b60 != 0:  # 60cmlik parca
                self.bilezikciz1000(dwg, xbase, ybase, 0.60)
                ybase += 0.6
                b60 = b60 - 1
            while b40 != 0:  # 40cmlik parca
                self.bilezikciz1000(dwg, xbase, ybase, 0.40)
                ybase += 0.4
                b40 = b40 - 1
            while b25 != 0:  # 40cmlik parca
                self.bilezikciz1000(dwg, xbase, ybase, 0.25)
                ybase += 0.25
                b25 = b25 - 1
            self.konikciz1000(dwg, xbase, ybase)
            ybase += 0.70
            while b10 != 0:  # 10cmlik parca
                self.ayarbilezikciz(dwg, xbase, ybase)
                ybase += 0.1
                b10 = b10 - 1
            self.kapakciz(dwg, xbase, ybase)
            # Yazi
            yazilar = "MH={0} \nKullanilacak parcalar:\nTemel+60x{1}+40x{2}+25x{3}+10x{4}+Konik+Kapak".format(self.name,str(b60),str(b40),str(b25),str(b10))
            mtext = dxf.mtext(yazilar, (xbase - .7, ybase + .6), height=0.07, )
            dwg.add(mtext)
            dwg.save()
        else:
            pass

#mh200=Manhole("100",103,101,423.12,120.00)
#mh200.Ciz()
