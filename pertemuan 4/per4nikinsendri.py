class PersegiPanjang:
    def __init__(self, panjang, lebar):
       self.panjang = panjang
       self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"


if __name__ == "__main__":
    try:
        panjang = float (input ("masukin panjangnya berapa ??"))
        lebar = float (input ("masukin lebarnya berapaaa ??"))

        if panjang <= 0 or lebar <= 0:
                raise ValueError("Panjang dan lebar harus lebih besar dari nol / 0 kaga boleh minus.")
 
      

        p = PersegiPanjang(panjang , lebar)
        print(p)  
        print("Kelilingnya = ", p.hitung_keliling())  
        print("Luasnya = ", p.hitung_luas())  
        
        
    except Exception as e:
        print(f"Terdapat kesalahan saat membuat objek: {e}")
