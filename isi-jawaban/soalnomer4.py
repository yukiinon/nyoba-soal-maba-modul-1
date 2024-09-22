# 1.	Darsono merupakan seorang mandor yang ingin menyusun tim dari beberapa orang, 
# ia memiliki total 7 orang dan ingin memilih 4 orang untuk masuk kedalam timnya. Buatlah program yang dapat membantu 
# Darsono menghitung berapa banyak cara untuk membentuk tim tersebut !


n = 7
r = 4

faktorial7 = 7 * 6 * 5 * 4 * 3 * 2 * 1
faktorial4 = 4 * 3 * 2 * 1
faktorial3 = 3 * 2 * 1       
# dapat dari 7 dikurangi 4
hitung = faktorial7 // (faktorial4 * faktorial3)

print("total cara seng iso darsono gawe waktu nggawe tim iku sakmene cak:", hitung)
print("ANJAYYYYY MENYUSUIIII")
