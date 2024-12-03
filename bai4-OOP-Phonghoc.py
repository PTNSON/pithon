class phong:
    def __init__(self,ma,day,dientich,sobd):
        self.ma=ma
        self.day=day
        self.dientich=dientich
        self.sobd=sobd

    def NhapPhong(self):
       
        self.day=input('Nhap day phong:')
        self.dientich=float(input('Nhap dien tich:'))
        self.sobd = int(input('Nhap so bong den:'))

    def stringp(self):
        return f'Ma:{self.ma}, Day:{self.day}, S={self.dientich}, So bong den:{self.sobd}'
    def getma(self):
        return self.ma
    def setma(self,x):
        self.ma=x


class Phonglt(phong):
    def __init__(self,maychieu,ma,day,dientich,sobd):
        phong.__init__(self,ma,day,dientich,sobd)
        self.maychieu=maychieu
    

    def Nhapplt(self):
        phong.NhapPhong(self)
        self.maychieu=input('Co may chieu hay khong (Y/N):')
    
    def stringp(self):
        return phong.stringp(self) + f', May chieu:{self.maychieu}'

    def DatChuan(self):
        return self.maychieu =='Y' and self.sobd*10>=self.dientich

class Phongmt(phong):
    def __init__(self,somt,ma,day,dientich,sobd):
        phong.__init__(self,ma,day,dientich,sobd)
        self.somt=somt

    def Nhappmt(self):
        phong.NhapPhong(self)
        self.somt=input('Nhap so may tinh:')

    def stringp(self):
        return phong.stringp(self) + f',So may tinh:{self.somt}'
    
    def DatChuan(self):
        return self.dientich/self.somt >=1.5 and self.sobd*10>=self.dientich
    def getmt(self):
        return self.somt

class Phongtn(phong):
    def __init__(self,chuyen,succhua,bonrua,ma,day,dientich,sobd):
        phong.__init__(self,ma,day,dientich,sobd)
        self.chuyen=chuyen
        self.succhua=succhua
        self.bonrua=bonrua

    def Nhapptn(self):
        phong.NhapPhong(self)
        self.chuyen=input('Nhap chuyen nganh:')
        self.succhua=input('Nhap suc chua')
        self.bonrua=input('Co bon rua hay khong(Y/N):')
    def stringp(self):
        return phong.stringp(self) + f',Bon rua:{self.bonrua}'
    
    def DatChuan(self):
        return self.bonrua=='Y' and self.sobd*10>=self.dientich



class QuanLy:
    def __init__(self,ds):
        self.ds=ds
    
    def Them(self):
        chon =int(input('Nhap loai phong muon them (1.PLT | 2.PMT | 3.PTN):'))
        maphong=''
        while(True):
            maphong=input('Nhap ma phong:')
            unique = True
            for i in range(len(self.ds)):
                if self.ds[i].getma() == maphong:
                    print('Ma phong da ton tai')
                    unique = False
                    break
            if unique:
                break
        if chon ==1:
            plt = Phonglt('','','',0,0)
            plt.setma(maphong)
            plt.Nhapplt()
            self.ds.append(plt)
        elif chon == 2:
            pmt = Phongmt(0, '', '', 0, 0)
            pmt.setma(maphong)
            pmt.Nhappmt()
            self.ds.append(pmt)
        elif chon == 3:
            ptn = Phongtn('', 0, '', '', '', 0, 0)
            ptn.setma(maphong)
            ptn.Nhapptn()
            self.ds.append(ptn)

    def Timkiem(self):
        chon =input('Nhap ma phong can tim:')
        for i in range(len(self.ds)):
            if self.ds[i].getma()==chon:
                print('Da tim thay')
                print(self.ds[i].stringp())
                break
            else:
                print('Khong tim thay')
    
    def Inds(self):
        print('Danh sach toan bo phong hoc')
        for i in range(len(self.ds)):
            print(self.ds[i].stringp())
    def Dsdatchuan(self):
        print('Danh sach cac phong dat chuan')
        for i in range(len(self.ds)):
            if self.ds[i].DatChuan():
                print(self.ds[i].stringp())
    
    def Update(self):
        chon=input('Nhap ma phong may can sua:')

        for i in range(len(self.ds)):
            if self.ds[i].getma()==chon:
                tmp=input('Nhap ma phong moi:')
                self.ds[i].setma(tmp)
                break
    
    def Xoa(self):
        chon=input('Nhap ma phong may can xoa:')
        for i in range(len(self.ds)):
            if self.ds[i].getma() == chon:
                res = input('Ban co chac chan muon xoa khong (Y/N):')
                if res == 'Y':
                    del self.ds[i]
                    break
    def Tongsophong(self):
        print(f'Tong so phong hoc la:{len(self.ds)}')
                
    def Phong60(self):
        for x in ds:
            if isinstance(x,Phongmt):
                if x.getmt()==60:
                    print(x.stringp())
    
                
ds=[]
ql =QuanLy(ds)

while(True):
    print('---------Menu---------')
    print('1. Them phong hoc')
    print('2. Tim kiem phong hoc')
    print('3. In toan bo phong hoc')
    print('4. In cac phong dat chuan')
    print('5. Cap nhat phong hoc')
    print('6. Xoa phong hoc')
    print('7. In ra tong so phong hoc')
    print('8. In ra cac phong co 60 may')
    print('0. Thoat')
    chon = int(input('Vui long nhap lua chon:'))
    if chon ==1:
        ql.Them()
    elif chon ==2:
        ql.Timkiem()
    elif chon ==3:
        ql.Inds()
    elif chon == 4:
        ql.Dsdatchuan()
    elif chon ==5:
        ql.Update()
    elif chon ==6:
        ql.Xoa()
    elif chon ==7:
        ql.Tongsophong()
    elif chon ==8:
        ql.Phong60()
    else: break






    
      

 
        


