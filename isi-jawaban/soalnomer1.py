# 1.	Andi mempunyai celengan berbentuk balok dan tabung. Celengan yang berbentuk balok
#  memiliki ukuran panjang 20cm dan lebar 13cm, Sedangkan celengan yang berbentuk tabung memiliki diameter 14cm dan luas selimutnya 440cm2.
#  Bantulah Andi dengan membuat program untuk menghitung volume dari kedua celengan miliknya tersebut !



# balok
panjang = 20 
lebar = 13 
tinggi = 10  
volumebalok = panjang * lebar * tinggi


# tabung
diameter = 14  # cm
jarijari = diameter / 2
luasselimut = 440  # cm²
pi = 22 / 7
tingbung = luasselimut / (2 * pi * jarijari)
volbung = pi * jarijari**2 * tingbung


print("volume celengan balokmu kae sakmene:", volumebalok, "cm³")
print("nek volume seng tabung sakmene iki:", volbung, "cm³")
print("wes paham rong saiki??")