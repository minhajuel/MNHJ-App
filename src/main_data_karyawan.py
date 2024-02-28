# Capstone Project Modul 1
# Nama: Hafiz Minhajuel
# Studi Kasus: Data Karyawan

import fungsi_data_karyawan as fdk

#Tampilan Program
main_menu = f'''

*** Minhaj Indonesia ***
Assalamu'alaikum
Selamat datang di Data Karyawan
Silahkan memilih menu yang diinginkan

1. Tampilkan data karyawan
2. Tambahkan data karyawan
3. Perbarui data karyawan
4. Hapus data karyawan
5. Keluar

Masukkan nomor menu (1-5): '''

#fungsi read menu
def read_menu():
    while True:
        menu_read = f'''
=== Tampilkan data karyawan Minhaj ===

1. Semua data karyawan 
2. Data karyawan berdasarkan NIP
3. Data karyawan berdasarkan jabatan
4. Cari nama karyawan
5. Urutkan karyawan berdasarkan gaji
6. Kembali ke halaman utama

Masukkan nomor menu (1-6): '''
        
        pilihan = input(menu_read)

        if pilihan == '1':
            print("\nData Karyawan Minhaj")
            fdk.display_data_minhaj()
        elif pilihan == '2':
            while True:
                input_nip = input("Masukkan NIP karyawan (format: 4 digit awalan 24): ")
                if input_nip.isdigit() and len(input_nip) == 4 and input_nip.startswith('24'):
                    fdk.display_data_nip(int(input_nip))
                    break
                else:
                    print("Afwan, masukkan NIP dengan format yang benar.")
        elif pilihan == '3':
            input_jabatan = input("Masukkan jabatan yang ingin dicari: ")
            fdk.filter_jabatan(input_jabatan)
        elif pilihan == '4':
            input_nama = input("Masukkan nama karyawan: ")
            fdk.cari_nama_karyawan(input_nama)
        elif pilihan == '5':
            fdk.urutkan_gaji()
        elif pilihan == '6':
            print("\nKembali ke halaman utama.")
            break
        else:
            print("Afwan, silahkan pilih opsi yang benar.")

#fungsi create menu
def create_menu():
    while True:
        menu_create = f'''
=== Tambahkan data karyawan Minhaj ===

1. Tambahkan data karyawan 
2. Kembali ke halaman utama

Masukkan nomor menu (1-2): '''
        
        pilihan = input(menu_create)

        if pilihan == '1':
            fdk.buat_data_baru()
        elif pilihan == '2':
            break
        else:
            print("Afwan, silahkan pilih opsi yang benar.")

# Fungsi update menu
def update_menu():
    while True:
        menu_update = f'''
=== Perbarui data karyawan Minhaj ===

1. Perbarui data karyawan
2. Kembali ke halaman utama

Masukkan nomor menu (1-2): '''
        
        pilihan = input(menu_update)

        if pilihan == '1':
            fdk.update_data()
        elif pilihan == '2':
            break
        else:
            print("Afwan, silahkan pilih opsi yang benar.")
    
# Fungsi delete menu
def delete_menu():
    while True:
        menu_delete = f'''
=== Hapus data karyawan Minhaj ===

1. Hapus semua data
2. Hapus berdasarkan NIP
3. Kembali ke halaman utama

Masukkan nomor menu (1-3): '''
        
        pilihan = input(menu_delete)

        if pilihan == '1':
            fdk.delete_semua_data()
        elif pilihan == '2':
            fdk.delete_nip()
        elif pilihan == '3':
            break
        else:
            print("Afwan, silahkan pilih opsi yang benar.")

#Fungsi main menu
def main():
    while True:
        pilihan = input(main_menu)
        if pilihan == '1':
            read_menu()
        elif pilihan == '2':
            create_menu()
        elif pilihan == '3':
            update_menu()
        elif pilihan == '4':
            delete_menu()
        elif pilihan == '5':
            print("\nSyukron! \nSampai Jumpa!")
            break
        else:
            print('Afwan, masukkan angka sesuai pilihan.')
            continue

main()