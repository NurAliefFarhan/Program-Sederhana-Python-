from queue import PriorityQueue


print("Menghitung perbandingan nilai")
a = int(input("Masukkan Nilai Pertama : "))
b = int(input("Masukkan Nilai Kedua : "))

if a > b:
    print("A lebih besar dari B")
elif a < b:
    print("a lebih kecil dari b")
elif a >= b:
    print("a lebih besar dari sama dengan dari b")
elif a <= b:
    print("a lebih kecil dari sama dengan dari b")
else:
    print("Invalid Nilai")

