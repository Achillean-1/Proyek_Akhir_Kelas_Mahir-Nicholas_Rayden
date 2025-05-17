## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang berkomitmen untuk memberikan pendidikan berkualitas dan mendukung keberhasilan akademik mahasiswanya. Namun, seperti banyak institusi pendidikan lainnya, Jaya Jaya Institut menghadapi tantangan tingkat dropout yang signifikan, yang dapat memengaruhi reputasi institusi, pendanaan, dan keberhasilan mahasiswa. Dropout mahasiswa tidak hanya merugikan secara finansial, tetapi juga berdampak pada misi institusi untuk menghasilkan lulusan yang kompeten dan siap berkontribusi di masyarakat. Oleh karena itu, Jaya Jaya Institut membutuhkan solusi berbasis data untuk mengidentifikasi mahasiswa yang berisiko dropout, memahami faktor-faktor yang memengaruhi, dan mengimplementasikan intervensi yang tepat waktu untuk meningkatkan tingkat retensi dan kelulusan.

## Permasalahan Bisnis
Permasalahan bisnis yang dihadapi Jaya Jaya Institut meliputi:
1. **Tingkat Dropout yang Tinggi**: Sejumlah mahasiswa tidak menyelesaikan studi mereka, yang berdampak pada efisiensi institusi dan keberhasilan mahasiswa.
2. **Kurangnya Identifikasi Dini**: Institusi belum memiliki sistem yang efektif untuk mendeteksi mahasiswa yang berisiko dropout sejak dini, sehingga intervensi sering terlambat.
3. **Faktor Risiko yang Kompleks**: Dropout dipengaruhi oleh berbagai faktor, termasuk performa akademik (misalnya, jumlah unit kurikuler yang diselesaikan), status keuangan (misalnya, tunggakan biaya kuliah), dan karakteristik demografis (misalnya, usia saat pendaftaran), yang sulit dianalisis tanpa alat prediktif.
4. **Ambiguitas Status Enrolled**: Status `Enrolled` (mahasiswa yang masih aktif tetapi belum lulus) menciptakan ketidakpastian dalam analisis, karena outcome akhir mereka (lulus atau dropout) belum jelas, yang dapat mengurangi akurasi prediksi.
5. **Keterbatasan Intervensi Berbasis Data**: Institusi belum memanfaatkan data untuk merancang strategi intervensi yang ditargetkan, seperti konseling akademik atau bantuan keuangan.

## Cakupan Proyek
Proyek ini bertujuan untuk mengembangkan sistem prediksi berbasis machine learning untuk mengidentifikasi risiko dropout mahasiswa di Jaya Jaya Institut. Cakupan proyek meliputi:
1. **Analisis Data**: Mengeksplorasi dataset mahasiswa (`data.csv`) untuk memahami distribusi status (`Graduate`, `Enrolled`, `Dropout`), korelasi antar variabel, dan faktor utama yang memengaruhi dropout.
2. **Preprocessing Data**: Melakukan pembersihan data, penanganan outlier (misalnya, capping `Admission_grade`), encoding variabel kategorikal, dan menghapus status `Enrolled` untuk fokus pada klasifikasi biner (`Graduate` vs. `Dropout`).
3. **Pembangunan Model**: Mengembangkan model RandomForestClassifier dengan SMOTE untuk menangani ketidakseimbangan kelas, dilatih pada data yang telah diproses.
4. **Evaluasi Model**: Mengevaluasi performa model menggunakan metrik seperti akurasi, precision, recall, F1-score, dan AUC-ROC untuk memastikan kemampuan prediksi yang andal.
5. **Deployment**: Menerapkan model dalam aplikasi Streamlit untuk memungkinkan prediksi risiko dropout secara real-time berdasarkan input data mahasiswa.
6. **Output**: Menyimpan hasil prediksi test set ke `predictions.csv` untuk analisis lebih lanjut, termasuk status aktual, prediksi, dan probabilitas.
7. **Rekomendasi**: Memberikan wawasan dan rekomendasi berbasis data untuk intervensi institusi guna mengurangi tingkat dropout.

## Persiapan
### Sumber data
Data yang digunakan dalam proyek ini berasal dari file data.csv, yang berisi informasi akademik dan demografis mahasiswa Jaya Jaya Institut. Dataset mencakup fitur-fitur seperti:
- Admission_grade: Nilai saat masuk kuliah
- Age_at_enrollment: Usia saat pendaftaran
- Curricular_units_1st_sem_approved: Jumlah SKS yang disetujui di semester pertama
- Curricular_units_1st_sem_enrolled: Jumlah SKS yang diambil
- Status: Status akhir mahasiswa (Graduate, Dropout, Enrolled), yang menjadi label prediksi

### Setup environment
Proyek ini dikembangkan menggunakan bahasa pemrograman Python, dengan library-library berikut untuk mendukung eksplorasi data, pemodelan machine learning, dan visualisasi:

Untuk memastikan semua dependensi proyek terinstal secara konsisten dan lingkungan kerja tetap terisolasi, disarankan menggunakan virtual environment. Berikut adalah panduan langkah demi langkah untuk membuat dan mengaktifkan environment di sistem operasi Windows menggunakan PowerShell:

⚠️ Catatan Penting: Jika Anda menggunakan PowerShell, pastikan Anda membukanya sebagai Administrator, terutama untuk menghindari masalah pada saat membuat environment atau menjalankan perintah instalasi.

Langkah-langkah Setup:
1. Buka PowerShell sebagai Administrator:
- Klik kanan pada ikon PowerShell
- Pilih “Run as Administrator”
- atau eksekusi command: "**Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned**" jika di terminal powershell Visual Code Studio

2. Navigasi ke folder proyek:
- **cd "C:\path\to\your\project"**
- contoh: "C:\Users\<nama-laptop>\Downloads\Proyek_Akhir_Kelas_Mahir-Nicholas_Rayden"

3. Membuat virtual environment:
- **python -m venv Jaya_Jaya_Institut**

4. Aktivasi environment:
- **.\Jaya_Jaya_Institut\Scripts\Activate**
- (Jika berhasil, Anda akan melihat nama environment ((Jaya_Jaya_Institut)) muncul di awal baris prompt Anda)

5. Instal semua dependensi dari file requirements.txt:
- **pip install -r requirements.txt**

Dependensi:
- pandas==2.2.3: manipulasi dan analisis data
- numpy==2.2.5: operasi numerik
- matplotlib==3.10.3: visualisasi statis
- seaborn==0.13.2: visualisasi statistik berbasis matplotlib
- scikit-learn==1.6.1: algoritma machine learning dan preprocessing
- imbalanced-learn==0.13.0: penanganan ketidakseimbangan kelas dengan SMOTE
- scipy==1.15.3: operasi ilmiah dan statistik
- joblib==1.5.0: serialisasi model dan pipeline
- sqlalchemy==2.0.40: ORM untuk menghubungkan aplikasi Python dengan database
- psycopg==3.2.9: driver PostgreSQL untuk Python, memungkinkan koneksi dan eksekusi query ke PostgreSQL

Jika Anda bekerja di sistem operasi lain seperti Linux atau macOS, perintah aktivasi environment sedikit berbeda:
- **Linux/macOS (bash/zsh)**:
- source Jaya_Jaya_Institut/bin/activate

Dengan virtual environment ini, proyek Anda akan lebih stabil, portabel, dan mudah dikembangkan ke lingkungan lain seperti server atau cloud.

### Preprocessing Awal
- Cleansing Data: Menghapus nilai null, duplikat, dan data tidak valid.
- Feature Engineering: Menghapus label Enrolled dari target karena belum merepresentasikan outcome akhir mahasiswa.
- Handling Outliers: Melakukan capping nilai Admission_grade untuk menjaga kestabilan model terhadap nilai ekstrem.
- Encoding: Variabel kategorikal diubah menjadi representasi numerik (one-hot atau label encoding).

### Akses Dashboard Metabase
Untuk mendukung eksplorasi data dan pelaporan visual, digunakan platform Metabase sebagai business intelligence tool.

Detail Login Metabase:

**Username**: root@mail.com

**Password**: root123


## Business Dashboard
Business dashboard yang dikembangkan dalam proyek ini bertujuan untuk membantu pihak manajemen Jaya Jaya Institut dalam memantau, memahami, dan mengambil keputusan berbasis data terkait risiko dropout mahasiswa. Dashboard ini menyajikan visualisasi interaktif yang dirancang agar mudah digunakan oleh pengguna non-teknis, khususnya pihak akademik dan pengambil kebijakan.

Fitur Utama Dashboard:
1. Distribusi Status Mahasiswa
Visualisasi pie chart atau bar chart yang menampilkan proporsi mahasiswa dengan status Graduate, Dropout, dan Enrolled. Ini memberikan gambaran umum seberapa besar tantangan dropout yang dihadapi institusi.
2. Visualisasi Korelasi Faktor Risiko
Heatmap korelasi antar variabel untuk mengidentifikasi faktor yang paling memengaruhi risiko dropout, seperti Admission_grade, Age_at_enrollment, dan Curricular_units_1st_sem_approved.
3. Perbandingan Fitur Mahasiswa Dropout vs Graduate
Boxplot atau histogram yang menunjukkan perbandingan nilai rata-rata berbagai fitur antara mahasiswa yang dropout dan yang berhasil lulus, membantu dalam menyoroti pola yang mencolok.
4. Hasil Prediksi Model
Tabel atau grafik yang menampilkan hasil prediksi dari model machine learning terhadap test set, termasuk status aktual, status prediksi, dan probabilitas prediksi. Ini membantu mengevaluasi performa model dan ketepatan identifikasi risiko.
5. Pengujian Input Interaktif
Dashboard menyediakan form input di mana pengguna dapat mengisi data seorang mahasiswa (seperti nilai masuk, jumlah SKS yang disetujui, usia saat masuk, dsb), lalu mendapatkan prediksi status secara real-time (Graduate, Dropout, atau Enrolled) dengan confidence score.

## Menjalankan Sistem Machine Learning
Prototype ini dikembangkan untuk memprediksi status mahasiswa—apakah Dropout, Enrolled, atau Graduated—dengan memanfaatkan algoritma RandomForestClassifier. Model dibangun berdasarkan sejumlah variabel yang merepresentasikan karakteristik akademik dan demografis mahasiswa.

Dalam penggunaannya, user diminta untuk menginput nilai dari setiap variabel yang telah ditentukan. Nilai-nilai tersebut kemudian diproses oleh model machine learning untuk menghasilkan prediksi status mahasiswa secara otomatis.

Tujuan dari prototype ini adalah untuk memberikan insight kepada institusi pendidikan dalam mengidentifikasi potensi risiko mahasiswa, sehingga dapat dilakukan intervensi yang tepat waktu dan berbasis data.

Prototype dapat diakses melalui tautan berikut:
🔗 https://jaya-jaya-institut-prediction.streamlit.app/

## Conclusion
Proyek ini berhasil mengembangkan sistem prediksi risiko dropout mahasiswa di Jaya Jaya Institut dengan memanfaatkan pendekatan machine learning berbasis RandomForestClassifier. Melalui analisis data akademik dan demografis, model mampu membedakan antara mahasiswa yang berpotensi lulus dan yang berisiko dropout dengan performa evaluasi yang memuaskan.

Hasil eksplorasi data menunjukkan bahwa faktor-faktor seperti nilai saat masuk (Admission_grade), jumlah SKS yang disetujui di semester pertama (Curricular_units_1st_sem_approved), dan usia saat pendaftaran (Age_at_enrollment) memiliki peran penting dalam menentukan keberhasilan studi mahasiswa. Dengan menghapus data Enrolled untuk fokus pada klasifikasi biner (Graduate vs Dropout), akurasi dan interpretasi model dapat ditingkatkan.

Model ini telah diintegrasikan dalam aplikasi Streamlit interaktif yang memungkinkan pengguna untuk memprediksi status mahasiswa secara real-time berdasarkan input data. Selain itu, dashboard yang dikembangkan memberikan insight mendalam mengenai distribusi status mahasiswa dan karakteristik yang memengaruhi risiko dropout.

Secara keseluruhan, sistem ini memberikan fondasi kuat bagi institusi untuk melakukan intervensi yang lebih tepat sasaran dan berbasis data, guna meningkatkan retensi dan keberhasilan akademik mahasiswa. Ke depan, sistem ini dapat dikembangkan lebih lanjut dengan mengintegrasikan data longitudinal dan feedback intervensi untuk perbaikan berkelanjutan.

## Rekomendasi Action Items
1. Intervensi Akademik Dini
- Terapkan program remedial sejak semester pertama bagi mahasiswa dengan nilai rendah.
- Sediakan bimbingan akademik khusus secara berkala bagi mahasiswa dengan evaluasi akademik rendah.

2. Pendampingan Perencanaan Studi
- Wajibkan konsultasi akademik sebelum registrasi mata kuliah setiap semester.
- Perkuat peran dosen wali dalam membimbing penyusunan rencana studi (KRS).
- Pantau jumlah SKS yang diselesaikan sebagai indikator kemajuan studi.

3. Seleksi Masuk dan Pembinaan Awal
- Tingkatkan kriteria seleksi masuk untuk menjaring mahasiswa yang lebih siap akademik.
- Sediakan program matrikulasi atau pembinaan akademik awal untuk mahasiswa dengan nilai masuk rendah.

4. Pendekatan Berdasarkan Usia Mahasiswa
- Tawarkan program studi yang fleksibel (jadwal, metode belajar) untuk mahasiswa berusia lebih tua.
- Berikan mentoring personal atau kelompok untuk mendukung mahasiswa dengan tantangan usia atau pekerjaan.

5. Dukungan untuk Mahasiswa dari Daerah Rentan
- Prioritaskan beasiswa bagi mahasiswa dari daerah dengan tingkat pengangguran tinggi.
- Kembangkan program pelatihan karir dan pengembangan soft skill untuk meningkatkan motivasi belajar.
- Lakukan pendekatan individual untuk memahami hambatan non-akademik mereka.
