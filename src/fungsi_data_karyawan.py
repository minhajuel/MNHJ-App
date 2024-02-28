from tabulate import tabulate

data_karyawan_minhaj = [
    [2404, 'Hafiz Minhajuel', 'Pria', '082165179911', 'Jl. Mojoarum 7, Gubeng, Kota Surabaya', 20000000, 'Marketing'],
    [2402, 'Firdayanti Zarho', 'Wanita', '082160789880', 'Jl. Srikana Timur no. 31, Kota Surabaya', 10000000, 'Marketing'],
    [2403, 'Risa Laila', 'Wanita', '082167189980', 'Jl. Banyu 7, Gubeng, Kota Surabaya', 6000000, 'Admin'],
    [2405, 'Salam', 'Pria', '08126078990', 'Jl. Banyu Urip Gg. V no. 37, Sawahan, Kota Surabaya', 7000000, 'Operasional'],
    [2406, 'Eka Rani', 'Wanita', '081168967755', 'Jl. Ngagel Jaya Barat no. 61, Gubeng, Kota Surabaya', 6000000, 'Admin'],
    [2401, 'Ichwan Abdillah', 'Pria', '089067865599', 'Jl. Srikana Barat no. 2, Gubeng, Kota Surabaya', 7000000, 'Operasional'],
]

headers = ['NIP', 'Nama', 'Jenis Kelamin', 'No. HP', 'Alamat', 'Gaji', 'Jabatan']

#READ
# Fungsi untuk mengurutkan data berdasarkan NIP
def urutkan_nip(karyawan):
    return karyawan[0]

# Fungsi untuk menampilkan semua data karyawan Minhaj yang telah diurutkan berdasarkan NIP    
def display_data_minhaj():
    if len(data_karyawan_minhaj) == 0:
        print("Afwan, tidak ada data karyawan yang tersedia.")
        print('\n*Kembali ke menu perbarui*')
    else:
        urutkan_data = sorted(data_karyawan_minhaj, key=urutkan_nip)
        print(tabulate(urutkan_data, headers=headers, tablefmt='grid'))

# Fungsi untuk menampilkan data karyawan Minhaj berdasarkan NIP    
def display_data_nip(nip):
    for karyawan in data_karyawan_minhaj:
        if karyawan[0] == nip:
            print(tabulate([karyawan], headers=headers, tablefmt='grid'))
            return
    print("Afwan, data karyawan dengan NIP tersebut tidak ditemukan.")
    print("\n*Kembali ke menu tampilkan*")

# Fungsi untuk mencari karyawan berdasarkan nama    
def cari_nama_karyawan(nama):
    found = False
    for karyawan in data_karyawan_minhaj:
        if karyawan[1].lower().startswith(nama.lower()):
            print(tabulate([karyawan], headers=headers, tablefmt='grid'))
            found = True
    if not found:
        print("Afwan, nama karyawan tidak ditemukan.")
        print("\n*Kembali ke menu tampilkan*")

# Fungsi untuk filter karyawan berdasarkan jabatan    
def filter_jabatan(jabatan):
    filtered_data = [karyawan for karyawan in data_karyawan_minhaj if karyawan[6].lower() == jabatan.lower()]
    if filtered_data:
        print(tabulate(filtered_data, headers=headers, tablefmt='grid'))
    else:
        print(f"Afwan, tidak ada karyawan dengan jabatan '{jabatan}'.")
        print("\n*Kembali ke menu tampilkan*")

# Fungsi mengurutkan data berdasarkan gaji karyawan
def urutkan_gaji_key(karyawan):
    return karyawan[5]

def urutkan_gaji():
    urutkan_data = sorted(data_karyawan_minhaj, key=urutkan_gaji_key, reverse=True)
    print(tabulate(urutkan_data, headers=headers, tablefmt='grid'))

# CREATE
# Fungsi untuk membuat data karyawan baru
def buat_data_baru():
    #Masukkan NIP karyawan baru
    while True:
        nip = input("Masukkan NIP karyawan (format: 4 digit awalan 24): ")
        if nip.isdigit() and len(nip) == 4 and nip.startswith('24'):
            nip_exists = any(karyawan[0] == int(nip) for karyawan in data_karyawan_minhaj) #Mengecek apakah NIP sudah dipakai karyawan lai
            if not nip_exists:
                break
            else:
                print("Afwan, NIP tersebut sudah dipakai. Silahkan masukkan NIP lain.")
                print("\n*Kembali ke menu tambahkan*")
                return
        else:
            print("Afwan, masukkan NIP dengan format yang benar.")
    #Masukkan Nama karyawan baru
    while True:
        nama = input("Masukkan nama karyawan: ")
        if not nama.strip() or not nama.replace(' ', '').isalpha():
            print("Afwan, harap masukkan nama yang valid.")
        else:
            nama = nama.title()
            break

    #Masukkan Jenis Kelamin karyawan baru
    while True:
        jeniskelamin = f'''
Pilih jenis kelamin:

1. Pria
2. Wanita

Masukkan pilihan (1-2): '''
        
        pilihan_jeniskelamin = input(jeniskelamin)
        if pilihan_jeniskelamin in ['1', '2']:
            jenis_kelamin = 'Pria' if pilihan_jeniskelamin == '1' else 'Wanita'
            break
        else:
            print("Afwan, silahkan pilih 1 atau 2.")
    
    #Masukkan No. HP karyawan baru
    while True:
        no_hp = input("Masukkan No. HP karyawan (diawali dengan 08): ")
        if no_hp.startswith('08') and no_hp[1:].isdigit() and 10 <= len(no_hp) <=13:
            no_hp_exists = any(karyawan[3] == no_hp for karyawan in data_karyawan_minhaj)
            if not no_hp_exists:
                break
            else:
                print("Afwan, No. HP tersebut sudah dipakai. Masukkan No. HP yang berbeda.")
        else:
            print("Afwan, No. HP diawali dengan 08 dan terdiri dari 10-13 digit")
    
    #Masukkan alamat karyawan baru
    while True:
        alamat = input("Masukkan alamat karyawan: ")
        if not alamat.strip():
            print("Alamat tidak boleh kosong.")
        else:
            break
   
    #Masukkan Gaji karyawan baru
    while True:
        gaji = input("Masukkan gaji karyawan: ")
        if gaji.isdigit():
            break
        else:
            print("Afwan, gaji harus berupa angka.")
    
    #Masukkan Jabatan karyawan baru
    while True:
        jabatan = input("Masukkan jabatan karyawan: ")
        if not jabatan.strip() or not jabatan.replace(' ', '').isalpha():
            print("Afwan, masukkan jabatan yang valid")
        else:
            jabatan = jabatan.title()
            break
    
    #Konfirmasi simpan data karyawan baru
    while True:
        konfirmasi = input("Ketik 'SIMPAN' untuk menyimpan: ")
        if konfirmasi.upper() == 'SIMPAN':
            data_karyawan_minhaj.append([int(nip), nama, jenis_kelamin, no_hp, alamat, int(gaji), jabatan])
            print("Data berhasil disimpan!")
            display_data_minhaj()
            print("\n*Kembali ke menu tambahkan*")
            break
        else:
            print("Data tidak disimpan!")
            print("\n*Kembali ke menu tambahkan*")
            break

#UPDATE
# Fungsi untuk memperbarui data karyawan
def update_data():
    #Masukkan NIP Karyawan
    nip_update = input("Masukkan NIP karyawan: ")
    found = False
    for i, karyawan in enumerate(data_karyawan_minhaj):
        if str(karyawan[0]) == nip_update:
            found = True
            display_data_nip(int(nip_update))
            while True:
                # Konfirmasi apakah ingin melanjutkan update
                konfirmasi_lanjut = input("\nApakah anda ingin melanjutkan perbaruan? \nKetik 'YA' jika ingin lanjut: ")
                if konfirmasi_lanjut.upper() != 'YA':
                    print("Update dibatalkan.")
                    print("\n*Kembali ke menu perbarui*")
                    return
            
                menu_update_data = f'''
=== Perbarui data karyawan Minhaj ===

1. Nama
2. Jenis Kelamin
3. No. HP
4. Alamat
5. Gaji
6. Jabatan
7. Kembali ke menu perbarui

Masukkan nomor menu (1-7): '''
                update_pilihan = input(menu_update_data)
                if update_pilihan == '1':
                    #Memperbarui nama
                    nama_baru = input("Masukkan nama baru: ")
                    if nama_baru.strip():
                        if nama_baru.strip().replace(' ','').isalpha():
                            konfirmasi = input(f"Apakah anda ingin mengubah nama menjadi '{nama_baru}'? \nKetik 'SIMPAN' untuk menyimpan: ")
                            if konfirmasi.upper() == 'SIMPAN':
                                data_karyawan_minhaj[i][1] = nama_baru.title()
                                print("Nama berhasil di perbarui.")
                                display_data_minhaj()
                                break
                            else:
                                print("Data tidak disimpan")
                                print('\n*Kembali ke menu perbarui*')
                                break
                        else:
                            print("Nama hanya boleh mengandung huruf.")
                    else:
                        print("Nama tidak boleh kosong.")

                elif update_pilihan == '2':
                    #Memperbarui Jenis Kelamin
                    pilihan_gender_baru = input("Masukkan pilihan jenis kelamin (1: Pria, 2: Wanita): ")
                    if pilihan_gender_baru in ['1', '2']:
                        konfirmasi = input(f"Apakah anda ingin mengubah jenis kelamin menjadi '{pilihan_gender_baru}'? \nKetik 'SIMPAN' untuk menyimpan: ")
                        if konfirmasi.upper() == 'SIMPAN':
                            gender_baru = 'Pria' if pilihan_gender_baru == '1' else 'Wanita'
                            data_karyawan_minhaj[i][2] = gender_baru
                            print("Jenis kelamin berhasil diperbarui.")
                            display_data_minhaj()
                            break
                        else:
                            print("Data tidak disimpan.")
                            print('\n*Kembali ke menu perbarui*')
                            break
                    else:
                        print("Afwan, silahkan pilih 1 atau 2")
                elif update_pilihan == '3':
                    # Memperbarui No. HP
                    hp_baru = input("Masukkan No. HP Baru: ")
                    if hp_baru.startswith('08') and hp_baru.isdigit() and 10 <= len(hp_baru) <= 13:
                        hp_tersedia = any(p[3] == hp_baru for p in data_karyawan_minhaj if p[0] != int(nip_update))
                        if not hp_tersedia:
                            konfirmasi = input(f"Apakah anda ingin mengubah No. HP menjadi '{hp_baru}'? \nKetik 'SIMPAN' untuk menyimpan: ")
                            if konfirmasi.upper() == 'SIMPAN':
                                data_karyawan_minhaj[i][3] = hp_baru
                                print("No. HP berhasil diperbarui.")
                                display_data_minhaj()
                                break
                            else:
                                print("Data tidak disimpan.")
                                print('\n*Kembali ke menu perbarui*')
                                break
                        else:
                            print("No. HP sudah digunakan karyawan lain. Silahkan masukkan no. HP lain")
                    else:
                        print("No. HP harus diawali dengan 08 dan terdiri dari 10 hingga 13 digit.")
                elif update_pilihan == '4':
                    #Memperbarui Alamat
                    alamat_baru = input("Masukkan alamat baru: ")
                    if alamat_baru.strip():    #memastikan alamat tidak kosong
                        konfirmasi = input(f"Apakah anda ingin mengubah alamat menjadi '{alamat_baru}'? \nKetik 'SIMPAN' untuk menyimpan: ")
                        if konfirmasi.upper() == 'SIMPAN':
                            data_karyawan_minhaj[i][4] = alamat_baru
                            print("Alamat berhasil diperbarui.")
                            display_data_minhaj()
                            break
                        else:
                            print("Data tidak disimpan")
                            print("\n*Kembali ke menu perbarui")
                            break
                    else:
                        print("Alamat tidak boleh kosong.")

                elif update_pilihan == '5':
                    # Memperbarui Gaji
                    gaji_baru = input("MAsukkan gaji baru: ")
                    if gaji_baru.isdigit() and int(gaji_baru) >=0:
                        konfirmasi = input(f"Apakah anda ingin mengubah gaji menjadi '{gaji_baru}'? \nKetik 'SIMPAN' untuk menyimpan: ")
                        if konfirmasi.upper() == 'SIMPAN':
                            data_karyawan_minhaj[i][5] = int(gaji_baru)
                            print("Gaji berhasil diperbarui.")
                            display_data_minhaj()
                            break
                        else:
                            print("Data tidak disimpan.")
                            print('\n*Kembali ke menu perbarui*')
                            break
                    else:
                        print("Afwan, gaji harus berupa angka.")

                elif update_pilihan == '6':
                    #memperbarui jabatan
                    jabatan_baru = input("Masukkan jabatan baru: ")
                    if jabatan_baru.strip():   #memastikan jabatan tidak kosong
                        if jabatan_baru.strip().replace(' ', '').isalpha():
                            konfirmasi = input(f"Apakah anda ingin mengubah jabatan menjadi '{jabatan_baru}'? \nKetik 'SIMPAN' untuk menyimpan: ")
                            if konfirmasi.upper() == 'SIMPAN':
                                data_karyawan_minhaj[i][6] = jabatan_baru.title()
                                print("Jabatan berhasil diperbarui.")
                                display_data_minhaj()
                                break
                            else:
                                print("Data tidak disimpan.")
                                print('\n*Kembali ke menu perbarui*')
                                break
                        else:
                            print("Jabatan tidak boleh mengandung angka")
                    else:
                        print("Jabatan tidak boleh kosong.")

                elif update_pilihan == '7':
                    break
                else:
                    print("Afwan, silahkan masukkan angka antara 1-7.")
                    continue
            break

    if not found:
        print("Afwan, data karyawan dengan NIP tersebut tidak ditemukan.")
        print('\n*Kembali ke menu perbarui*')

#DELETE
# Fungsi untuk menghapus semua data karyawan
def delete_semua_data():
    konfirmasi = input("Apakah anda yakin ingin menghapus semua data karyawan? \nKetik 'HAPUS' untuk menghapus: ")
    if konfirmasi.upper() == "HAPUS":
        data_karyawan_minhaj.clear()
        print("Semua data karyawan telah dihapus.")
    else:
        print("Operasi penghapusan dibatalkan.")

# Fungsi untuk menghapus data karyawan berdasarkan NIP
def delete_nip():
    nip_delete = input("Masukkan NIP karyawan yang ingin dihapus: ")
    found = False

    for karyawan in data_karyawan_minhaj:
        if str(karyawan[0]) == nip_delete:
            display_data_nip(int(nip_delete))
            konfirmasi = input(f"Apakah anda yakin ingin menghapus '{nip_delete}' karyawan? \nKetik 'HAPUS' untuk menghapus: ")
            if konfirmasi.upper() == 'HAPUS':
                data_karyawan_minhaj.remove(karyawan)
                print("Data karyawan berhasil di hapus.")
            else:
                print("Operasi penghapusan dibatalkan.")
            found = True
            break

    if not found:
        print("Afwan, data karyawan dengan NIP tersebut tidak ditemukan.")
    print("\n*Kembali ke menu hapus*")