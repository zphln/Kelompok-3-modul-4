def watermark():
    print("Program menentukan jenis akar akar persamaan kuadrat dari Kelompok 3")

class menentukan_akar:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def watermark1(self, nama_kelompok):
        return f"{nama_kelompok}"

    def diskriminan(self):
        return (self.b * self.b) - (4 * self.a * self.c)

    def jenis_akar(self):
        d = self.diskriminan()
        if d > 0:
            return f"Akar-akar persamaan kuadrat dari {self.a}x^2 + {self.b}x + {self.c} = 0 adalah real berbeda."
        elif d == 0:
            return f"Akar-akar persamaan kuadrat dari {self.a}x^2 + {self.b}x + {self.c} = 0 adalah real sama."
        else:
            return f"Akar-akar persamaan kuadrat dari {self.a}x^2 + {self.b}x + {self.c} = 0 adalah imajiner."

watermark()

while True:
    print("Masukkan nilai koefisien")
         
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = float(input("Masukkan nilai c: "))

    if a == 0:
        print(" A tidak boleh sama dengan 0")
        continue
 
    print("-" * 20)
    obj = menentukan_akar(a, b, c)
    print(f"Program oleh {obj.watermark1('Kelompok 3')}")
    print(f"Nilai diskriminan: {obj.diskriminan()}")
    print(obj.jenis_akar())
    print("-" * 20)
  
    konfirmasi = input("Apakah anda ingin menentukan jenis persamaan akar kuadrat lagi y/n? ").strip().lower()

    if konfirmasi.lower() != 'y':
        print("Terimakasih telah menggunakan program kelompok 3")
        break
