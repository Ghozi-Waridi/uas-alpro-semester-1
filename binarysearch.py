# import library padas jika dengan alias pd
# jika belum menginstall pandas silahkan install degan menggunakn (pip install pandas pada terminal kalian)
import pandas as pd

#menggunaan library pandas untuk membaca dataset degan fomal csv, silahkan sesuaikan dengan path(jalur) dari file kalian di simpan dimana
data = pd.read_csv('dataset/DataAngkatan.csv') #dibagian dataset ini  masih kotor ya teman" masih ada beberapa cplumn yang tidak digunakan jadi menging di bersihkan saja 

# membuat sebuah method atau function untuk meringkas code supaya tidak membingungkan
''' melakukan operasi dari binary search '''
def binary_search(df, nim):
    low = 0
    high = len(df)
    while low <= high:
        mid = (low + high) // 2
        if df.loc[mid, "NIM"] == int(nim):
            return df.loc[mid]
        elif df.loc[mid, "NIM"] < int(nim):
            low = mid + 1
        else:
            high = mid - 1
    return None


''' menampilakan data '''
print("="*14)
print("Data Mahasiswa")
print("="*14,"\n")

# meminta inptu user nim mahaisswa yang ingin dicari contoh 230605110083 => ahmad ghozi waridi
nim = input("Masukkan NIM : ")

# memangil function binary searc dengan parameter dari data (dataset) nim (inputan) dan di masukan kedalamm variabel
data_mahasiswa = binary_search(data, nim)

# melakukan pengecekan apakah data  tersebut berada di dalam dataset atau tidak
if data_mahasiswa is not None:
    TTL = data_mahasiswa["Tempat"] + ", " + data_mahasiswa["Tangga Lahir"]
    print("\nData mahasiswa yang ditemukan: ")
    print("\nNama\t : ", data_mahasiswa["Nama Lengkap"])
    print("NIM\t : ", data_mahasiswa["NIM"])
    print("TTL\t : ", TTL)
    
else:
    print("Data tidak ditemukan.")