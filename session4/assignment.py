def hitung_keuntungan(harga_barang):
    # Menghitung keuntungan 10% dari harga barang
    keuntungan = harga_barang * 0.1
    return keuntungan

def main():
    list_barang = []

    while True:
        # Meminta input dari pengguna
        nama_barang = input("Masukkan nama barang: ")
        
        # Melakukan validasi input harga barang
        while True:
            try:
                harga_barang = float(input("Masukkan harga barang: "))
                break
            except ValueError:
                print("Harga barang harus berupa angka. Silakan coba lagi.")
        
        # Memanggil fungsi untuk menghitung keuntungan
        keuntungan = hitung_keuntungan(harga_barang)

        # Menyimpan barang dan keuntungannya dalam list
        list_barang.append((nama_barang, harga_barang, keuntungan))

        # Menanyakan apakah ingin input barang lain atau tidak
        input_lagi = input("\nApakah ingin menginput barang lain? (y/n): ")
        if input_lagi.lower() != 'y':
            break

    # Menampilkan semua barang dan keuntungannya
    print("\nDaftar Barang:")
    for nama_barang, harga_barang, keuntungan in list_barang:
        print(f"\n- {nama_barang}: \nHarga Rp.{harga_barang:,}\nKeuntungan Rp.{keuntungan:,}\nHarga Jual Rp.{harga_barang+keuntungan:,}")
        print("\nMakasih.")
if __name__ == "__main__":
    main()
