import math


class PersegiPanjang:
    def __init__(self, panjang, lebar):
        try:
            self.panjang = float(panjang)
            self.lebar = float(lebar)
            if self.panjang < 0 or self.lebar < 0:
                raise ValueError("Panjang dan lebar harus lebih besar atau sama dengan nol.")
        except ValueError as e:
            print(f"Error saat menginisialisasi PersegiPanjang: {e}")
            self.panjang = 0
            self.lebar = 0

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    




if __name__ == "__main__":
    try:
        panjang = input ("masukan panjangnya berapa pake CM ?")
        lebar = input ("masukin lebarnya berapa pake CM")

        pp = PersegiPanjang(panjang,lebar)
        print(pp) 
        print(f"Keliling: {pp.hitung_keliling()} cm")  
        print(f"Luas: {pp.hitung_luas()} cm²") 

        # Contoh dengan input yang salah
        pp_invalid = PersegiPanjang('-1', 'a')  
        print(pp_invalid)  
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")