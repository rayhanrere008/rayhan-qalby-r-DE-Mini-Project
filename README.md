# ETL Pipeline and Visualization

## About Project
Project ini memiliki tujuan untuk melakukan ETL (Extract, Transform, Load). Dengan melakukan proses pengekstrakan data dari berbagai sumber kemudian digabungkan menjadi satu dataset. Dataset tersebut dilakukan proses Cleaning dan Tranformasi. Kemudian hasilnya akan diupload ke data warehouse (Cloud Storage dan Database). Setelah itu dialukasn proses Visualisasi Data dari data tersebut untuk mendapatkan insight dari model prediksi biaya total proyek Bank Dunia.

## Tech Stacks
Daftar tools dan framework yang digunakan dalam project ini:
- Python
- Library in Python: Pandas, sqlite3, requests, json, numpy, re, seaborn, matplotlib.pyplot, plotly.express, Levenshtein, BeautifulSoup, sklearn, google cloud, sqlalchemy
- Jupyter Notebook
- Google Cloud Storage
- MySQL
- API World Bank
- XML
- JSON 
- CSV
- DB
- other

## Architecture Diagram
 ![ETL Diagram](https://github.com/rayhanrere008/rayhan-qalby-r-DE-Mini-Project/blob/main/image/ETL_Architecture_Diagram.png?raw=true)

## Setup 
### Langkah 1: Persiapan Lingkungan
Pastikan Anda telah menginstal Tools dan Library yang diperlukan:
- Python
- Pandas (untuk melakukan ETL)
- Matplotlib, Plotly.express, Seaborn (untuk visualisasi)
- Google Cloud dan Sqlalchemy (untuk load to warehouse)
- Others (yang telah disebutkan pada bagian 'Tech Stacks')

### Langkah 2: Ekstraksi Data
1. Unduh file data yang diberikan dari [sumber](https://github.com/yudhaislamisulistya/mini-project-de-alta) yang ditentukan.
2. Simpan file data yang berupa csv, json, db, xml, dll di direktori proyek Anda.
3. Buka lingkungan pengembangan Python (seperti Jupyter Notebook atau IDE Python).
4. Import Library yang diperlukan
5. Buat skrip Python untuk membaca atau ekstraksi file data yang diunduh menggunakan Pandas.

### Langkah 3: Transformasi Data
1. Buat skrip Python untuk melakukan transformasi data sesuai kebutuhan proyek, seperti pembersihan data, penggabungan data, penyesuaian tipe data, Menguraikan Tanggal (Parsing Dates), Menangani Encoding File (Handling File Encodings), Menghapus Outliers (Removing Outliers), Penskalaan Fitur (Scaling Features), Membuat Variabel Dummy (Creating Dummy Variables), Rekayasa Fitur (Engineering Features), dsb.

### Langkah 4: Load Data to Warehouse
1. Buat skrip Python untuk menyimpan data yang telah diolah ke dalam format yang sesuai (misalnya, file CSV).
2. Buat Bucket di Google Cloud Storage (implementasikan IAM dan Service Accountnya)
3. Buat Database di MySQL (misal menggunakan RDBMS : Dbeaver)
4. Buatlah skrip untuk melakukan proses load ke Google Cloud Storage dan Database

### Langkah 5: Visualisasi Data
1. Gunakan Pandas untuk membaca data yang telah diolah
2. Gunakan Matplotlib, Plotly.express, Seaborn  untuk membuat visualisasi data yang relevan berupa analisis statistik deskriptif, analisis korelasi, analisis distribusi, analisis tren, analisis perbandingan, atau analisis lain yang informatif. Diagram bisa berupa diagram batang, diagram lingkaran, atau plot garis.
3. Sertakan judul yang jelas dan label sumbu untuk memperjelas visualisasi.

### Kesimpulan
Dengan mengikuti langkah-langkah di atas, Anda dapat melakukan proyek ETL dan visualisasi data secara lokal menggunakan Python dan tools yang sesuai. Pastikan untuk menyesuaikan langkah-langkah ini sesuai dengan kebutuhan dan karakteristik proyek Anda.

Selamat mengerjakan proyek!