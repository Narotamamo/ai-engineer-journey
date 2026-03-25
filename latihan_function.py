# Function dasar
# def — kata kunci untuk bikin function
# iphone_type — nama resepnya
# iphone_series — bahan yang dimasukkan
# return — hasil akhir yang dikeluarkan




def iphone_type(iphone_series):
    return f'Ini iphone: {iphone_series} !'

print(iphone_type('13 Pro'))
print(iphone_type('15'))
print(iphone_type('17 Promax'))
                  
#2. Function dengan proses di dalam
def double(angka):
    hasil = angka * 2 #   <--variabel
    return hasil
print(double(5))
print(double(3))
print(double(10))

def tambah(a,b):
    return a + b
print(tambah(3,5))
print(tambah(10,20))

def kurang(a,b):
    return a - b
print(kurang(10,5))
print(kurang(8,3))

#3. Function yg terima data list
def hitung_total(angka_list):
    total = sum(angka_list)
    return total
scores = [23,34,54,32,34]
print(hitung_total(scores))