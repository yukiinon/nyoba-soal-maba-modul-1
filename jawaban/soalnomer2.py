# 2.	Darmaji ingin mengetahui jumlah nilai dari 8 suku pertama dari sebuah deret aritmatika dengan keadaan suku ke-5 dari 
# deret tersebut bernilai 11 dan jumlah nilai suku ke-8 dan suku ke-12 nya adalah 52.
#  Buatlah program untuk membantu Darmaji untuk menyelesaikan masalah tersebut !


sukuke5 = 11
u8samau12 = 52

# rumus u5 = a + 4b
a = sukuke5 - 4 * ((u8samau12 - 2 * sukuke5) / 18)
b = (sukuke5 - a) / 4


# jumlah 8 suku pertama, sn = n/2 * (2a + (n-1)b)
n = 8
delapansukupertama = n / 2 * (2 * a + (n - 1) * b)

print("Jumlah 8 suku pertama:", delapansukupertama)
print("gampang kannn???")
print("gausah digawe pusing")