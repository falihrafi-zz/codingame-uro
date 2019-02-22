# codingame-uro
Tugas URO Day 3

Nama Anggota :
1. Rafi Falih Mulia 16518343
2. Desylionie Onggani Winata 16718022
3. Cynthia Athena 16518159
4. Cindy Masrya 16018020


# STRATEGI
pertama, kami mengidentifikasi semua zona yang ada dalam permainan dan zona yang terdapat di sekitar POD. setelah kami mengetahui semua zona yang ada dan semua zona yang ada di sekitar POD, kita membuat zona-zona yang berhubungan. selain mengidentifikasi zona yang ada, kami juga mengidentifikasi jumlah POD yang kami miliki dan juga lokasi dari base kami dan base musuh. 

Langkah selanjutnya, kami membuat sebuah fungsi bernama 'gerak'. Kegunaan dari fungsi ini adalah jika POD tersebut berlokasi di salah satu zona, maka POD tersebut akan bergerak ke zona yang berhubungan. 

Setelah itu, program akan masuk ke dalam game loop. Kami membuat array kosong bernama 'd', 'e', dan 'f'. array 'd' berguna sebagai tempat untuk menyimpan zona yang terlihat (tidak tertutup kabut). array 'e' berguna untuk menaruh data posisi dan jumlah PODs. array 'f' berguna sebagai tempat untuk mengetahui pemilik zona. 

program pada permainan ini kami buat suoaya PODs bergerak secara random/sporadis. PODs akan bergerak berdasarkan perintah print(str(m) + str(n) + str(o)). 'm' adalah jumlah PODs yang akan digerakkan. 'n' adalah letak zona awal dari PODs. 'o' adalah zona yang akan dituju oleh PODs.
