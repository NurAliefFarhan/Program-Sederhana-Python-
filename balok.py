print("Program menghitung luas, volume, dan keliling pada balok")
panjang = int(input("Panjang : "))
lebar = int(input("Lebar : "))
tinggi = int(input("Tinggi : "))

#def mendefinisikan method atau fungsi 
def Luas_permukaan(panjang,lebar,tinggi):
    Luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    return Luas 

def Volume(panjang,lebar,tinggi):
    Volume = panjang * lebar * tinggi 
    return Volume

def Keliling(panjang,lebar,tinggi):
    Keliling = 4 * (panjang + lebar + tinggi)
    return Keliling 

print('Jadi balok dengan ukuran panjang:{}, Lebar:{}, Tinggi:{} \nMempunyai Luas:{}, Volume:{}, Keliling:{}' .format(panjang,lebar,tinggi, Luas_permukaan(panjang,lebar,tinggi), Volume(panjang,lebar,tinggi), Keliling(panjang,lebar,tinggi)))

