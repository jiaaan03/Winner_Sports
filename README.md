Tugas 2
1. Dimulai dari cara membuat proyek Django baru itu aktifin env nya dulu,lalu jalanin perintah yg ada di tutorial 1 "python manage.py startapp main" kayak gitu. Nah abis tuh mulai edit-edit dibagian settings.py, trus buat main.html buat nanti ngeliat hasilnya pas mencet local.host, lalu ubah isi models.py dan jika kita mengubah models.py maka perlu jalanin ini di terminal "python manage.py makemigrations" dan "python manage.py migrate". Berikutnya pada urls.py kita merouting aplikasinya. Setelah udah memetakan URL nya, maka perlu melakukan deployment ke PWS

2. Diawali dari client/browser mengirimi HTTP request ke urls.py lalu urls.py akan mengonfigurasikan URL dan lanjut ke views.py. Disini views.py akan mengecek dlu logic dari kode nya klo butuh data maka abis itu perlu ke models.py nah di models.py itu untuk mengambil/menyimpan data yg data nya akan disimpan di database, lalu balik lagi ke views.py dan disini views.py berfungsi memanggil template HTML yang ada pada templates. pada template itu tersimpan logic-logic yang akan ditampilkan ke pengguna, selanjutnya yg terakhir dikirim ke client lagi

3. settings.py itu pusat konfigurasi pada proyek django, jadi semua pengaturan aplikasi itu disimpan di settings.py, misalnya bisa simpen aplikasi yg kita buat di INSTALLED_APPS, berhubungan sama database juga biar data-data yg kita update kesimpen juga, terus ada keamanan buat nyimpen host mana aja yg mau kita pake

4. jadi cara kerja migrasi itu kita tulis/ubah models.py lalu kita buat migrasi dan jalanin perintah di terminal "python manage.py makemigrations" lalu migrasi ke database dengan menjalankan perintah ini  di terminal "python manage.py migrate". sudah tersimpan, jika ada update di models.py tinggal di migrasi lagi sesuai dengan langkah yg sudah saya sebutkan

5. Menurut saya sih karena jika melihat dari tutorial dengan baik, saya hanya perlu menjalankan perintah-perintahnya saja dan tidak perlu  mendownload library atau yg lainnya, alur nya mudah dipahami dan nama file yang ada di proyek/aplikasi juga sesuai dengan isinya gitu misal kayak settings.py yg berisi kayak keamanan data, bisa nyimpen aplikasi gitu-gitu jadi lebih jelas ajaa dan cocok untuk dipahami dan dipelajari untuk kita sebagai mahasiswa

6. hmm mungkin bisa lebih fast respons lagi jika ada yg bertanya melalui ticket

tugas 3
1. kita perlu data delivery buat implementasiin sebuah platform itu untuk menghubungkan antara sumber data dan user, tanpa adanya mekanisme delivery maka data cuman kesimpen di database dan user gak akan bisa tau datanya soalnya gak pernah sampe ke user, terus ada konsistensi data yaitu memastikan tiap user bisa nerima data yg sama atau konsisten, trus ada efisiensi yaitu jika kita menggunakan data delivery maka pendistribusian data bisa diatur lebih efisien.

2. kalo menurut saya sih yg lebih baik ya json karena lebih mudah dibaca aja oleh kita, sedangkan klo xml itu kan mirip2 sama html dan buat saya agak susah sih dibacanya dan alasan mengapa json bisa lebih populer dripada xml adalah karena lebih mudah dipahami oleh manusia/developer, dan juga cocok buat web development

3. fungsi dari is_valid() itu sesuai namanya yaitu melakukan validasi data form misalnya kayak cek apakah semua fields udah sesuai aturan atau belum, klo formnya valid, django bakal simpan data yg udah dibersihin trus kalo gak valid nanti error bakal dimasukin ke form.errors biar bisa ditampilih di halaman user. alasan kita membutuhkan is_valid() adalah untuk menjamin data yg masuk aman atau tidak, memberi feedback ke user, dan lebih simpel dalam pengecekan misal kayak Integerfield

4. csrf itu token unik yg disertakan di form biasanya input tersembunyi, saat form diikirim, django akan memeriksa apakah token yg dikirim cocok dgn yg disimpan, lalu karena penyerang gak bisa membaca token ini maka mereka gak bisa buat request valid yg lolos pemeriksaan csrf. makanya csrf_token itu buat cegah request palu yg di buat dari situs penyerang. yang akan terjadi jika form ga menyertakan csrf_token yaitu django secara default akan menolak request POST, misal kita mau hapus token tpi ttp punya middleware nanti requestnya bakalan error 404. gimana penyerang bisa memanfaatkan ini? jadi kayak korban udah login itu ke url  tertentu trus korban mengunjungi situs penyerang 


5. diawali dari membuat folder templates yg berisi base html yg berguna jadi template dasar sbg kerangka umum, lalu update settings.py buat nambahin DIRS nya. abis tu buat file forms.py buat form sederhana untuk input data data trus update views.py nya juga dan sesuaikan sama yg kita mau, update urls.py nya sesuai dgn fungsi yg ada di views.py nya trus update lgi main.html nya dan sesuaikan lgi logicnya. setelah itu buat fungsi baru buat xml sama json trus di urls.py nya di update lgii untuk importnya nah nanti bisa dicek ke postman juga abis tuh di ss dan di deploy ke pws serta github deh klo udah

![alt text](<Screenshot 2025-09-16 003339.png>)

![alt text](<Screenshot 2025-09-16 003408.png>)

Tugas 4:
1. Django AuthenticationForm itu sebagai formulir bawaan dari djangoo dan dibuat untuk memvalidasi username dan password yang diinput oleh user. Kelebihannya yaitu keamanannya sudah terjaga dan cara menggunakannya juga mudah. Kekurangannya yaitu fungsi nya terbatas jadi hanya untuk proses login saja dan formulir ini juga di default harus memerlukan username ketika login

2. Autentikasi adalah proses memverifikasi seorang oengguna, biasanya melalui username dan password. Otorisasi adalah proses menentukan apa yang bisa user lakukan setelah user masuk, misal jika user masuk sebagai admin maka bisa menghapus data, klo masuk sebagai user basa ya cuman bisa liat aja dan gabisa hapus data. Implememtasi nya yaitu django memeriksa session cookie buat melihat apakah user udah login, jka belum nanti user akan diarahkan ke halaman login. Lalu setelah user diautentikasi, django memeriksa apakah user memiliki izin untuk melihat halaman admin, jika tidak  django akan menolak akses

3. kelebihannya session yaitu data disimpan disisi server bukan di browser pengguna dan tidak ada batasan ukuran data yang disimpan. Kekurangannya yaitu tiap session aktif menggunakan memori server jika banyak yg menggunakan maka akan memperlambat kinerja dan karena session bergantung pada koneksi ke server, data tidak bisa diakses jika user sedang offline

kelebihannya cookies yaitu data cookie disimpan dibrowser pengguna makanya tidak membebani server dan juga dapat diakses ketika offline. Kekurangannya yaitu cookies mudah diakses, dimodifikasi, dan dicuri oleh penyerang siber dan sebagian besar browser membatasi ukuran cookie biasanya hanya sekitar 4KB

4. by default penggunaan cookies tidak sepenuhnya aman karena memiliki risiko potensial yanng harus diwaspadai seperti pencurian cookies, manipulasi data, dan CSRF. Cara menanganinya yaitu django menyediakan mekanisme perlindungan CSRF yang terintegrasi memalalui token unik dan juga django mengkonfigurasi cookie sesi dengan httpOnly dan juga Secure

5. pertama membuat fungsi dan form registrasi, lalu jgn lupa update urls.py ny, berikutnya membuat  fungsi login dan fungsi logout. berikutnya yaitu merestriksi akses halaman main dan products detail. lalu buat cookie supaya data bisa digunakan lalu hubungkan model products dengan user 

Tugas 45
1. urutan prioritas pengambilan CSS selector yang pertama adalah inline style yaitu style yg ditulis di atribut elemen mengalahkan semua selector dari file CSS eksternal maupun internal. yang kedua ID selector, ID memiliki prioritas lebih tinggi daripada class atau tag selector. yang ketiga class, atribute, dan pseudo-class selector. yang keempat elemen dan pseudo-element selector. dan yang terakhir ada !important 

2. reponsive design itu pendekatan desain web supaya tampilan aplikasi menyesuaikan ukuran layar perangkat. konsep ini penting karena aksesibilitas dan fleksibilitas, User Experience, dan Search Engine Optimize. contoh aplikasi yg menerapkan konsep ini ada tokopedia, shopee, dan twitter, misalnya klo dibuka di desktop rapi dan jika dibuka di hp juga rapi. contoh yang belum menerapkan konsep ini seperti website pemerintahan yang lama, misalnya klo di desktop itu keliatan rapi tpi waktu di coba di hp ternyata teksnya terlalu kecil 

3. margin itu ruang kosong diluar batas elemen yg berfungsi untuk beri jarak gitu antar elemen biar gak terlalu deket, border itu  garis pembatas di sekitar elemen yang membungkus area konten yg fungsinya buat negesin batas elemen, padding itu ruang kosong didalam elemen yang berfungsi untuk memberi jarak antara isi

4. konsep flexbox yaitu mengatur elemen dalam satu dimensi baris atau kolom dan fokus ke perataan dan distribusi ruang antar elemen di satu arah kegunaannya buat nyusun menu navigasi horizontal atau vertikal dan membuat layout responsif secara cepat tanpa menghitung ukuran manual. konsep grid layout yaitu mengatur elemen dalam dua dimensi baris dan kolom, bisa membuat layout kompleks seperti dashboard dan galeri. kegunaannya membuat tata letak multi-kolom tanpa float atau positioning manual dan mengatur ukuran kolom dan baris secara proporsional atau tetap.

5. jadi step yang prtama itu tambahin bootstrap css dan js (disini aku pakai tailwind) lalu tambahin fitur edit di views.py trs update path di urls.py nya di bagian main.html di update si buttonnya biar bisa dipencet sama juga buat fitur hapus yang stepnya sama seperti yang step edit. lalu buat navigation bar dengan membuat navbar.html lalu buat global.css yang dihubungkan ke base.html dan tinggal di styling sesuai yg diinginkan lalu styling halaman login, register, home, detail products, create products, edit products 