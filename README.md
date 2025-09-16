Tugas 2
1. Dimulai dari cara membuat proyek Django baru itu aktifin env nya dulu,lalu jalanin perintah yg ada di tutorial 1 "python manage.py startapp main" kayak gitu. Nah abis tuh mulai edit-edit dibagian settings.py, trus buat main.html buat nanti ngeliat hasilnya pas mencet local.host, lalu ubah isi models.py dan jika kita mengubah models.py maka perlu jalanin ini di terminal "python manage.py makemigrations" dan "python manage.py migrate". Berikutnya pada urls.py kita merouting aplikasinya. Setelah udah memetakan URL nya, maka perlu melakukan deployment ke PWS

2. Diawali dari client/browser mengirimi HTTP request ke urls.py lalu urls.py akan mengonfigurasikan URL dan lanjut ke views.py. Disini views.py akan mengecek dlu logic dari kode nya klo butuh data maka abis itu perlu ke models.py nah di models.py itu untuk mengambil/menyimpan data yg data nya akan disimpan di database, lalu balik lagi ke views.py dan disini views.py berfungsi memanggil template HTML yang ada pada templates. pada template itu tersimpan logic-logic yang akan ditampilkan ke pengguna, selanjutnya yg terakhir dikirim ke client lagi

3. settings.py itu pusat konfigurasi pada proyek django, jadi semua pengaturan aplikasi itu disimpan di settings.py, misalnya bisa simpen aplikasi yg kita buat di INSTALLED_APPS, berhubungan sama database juga biar data-data yg kita update kesimpen juga, terus ada keamanan buat nyimpen host mana aja yg mau kita pake

4. jadi cara kerja migrasi itu kita tulis/ubah models.py lalu kita buat migrasi dan jalanin perintah di terminal "python manage.py makemigrations" lalu migrasi ke database dengan menjalankan perintah ini  di terminal "python manage.py migrate". sudah tersimpan, jika ada update di models.py tinggal di migrasi lagi sesuai dengan langkah yg sudah saya sebutkan

5. Menurut saya sih karena jika melihat dari tutorial dengan baik, saya hanya perlu menjalankan perintah-perintahnya saja dan tidak perlu  mendownload library atau yg lainnya, alur nya mudah dipahami dan nama file yang ada di proyek/aplikasi juga sesuai dengan isinya gitu misal kayak settings.py yg berisi kayak keamanan data, bisa nyimpen aplikasi gitu-gitu jadi lebih jelas ajaa dan cocok untuk dipahami dan dipelajari untuk kita sebagai mahasiswa

6. hmm mungkin bisa lebih fast respons lagi jika ada yg bertanya melalui ticket


