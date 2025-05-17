## Detail Login Metabase
**Username**: root@mail.com

**Password**: root123

## Detail Link Streamlit
https://jaya-jaya-institut-prediction.streamlit.app/

## Setup Environment
Langkah-langkah Setup:
1. Buka PowerShell sebagai Administrator:
- Klik kanan pada ikon PowerShell
- Pilih “Run as Administrator”
- atau eksekusi command: "**Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned**"

2. Navigasi ke folder proyek:
- **cd "C:\path\to\your\project"**
- contoh: "C:\Users\<nama-laptop>\Downloads\Proyek_Akhir_Kelas_Mahir-Nicholas_Rayden"

3. Membuat virtual environment:
- **python -m venv Jaya_Jaya_Institut**

4. Aktivasi environment:
- **.\Jaya_Jaya_Institut\Scripts\Activate**
- (Jika berhasil, Anda akan melihat nama environment ((env)) muncul di awal baris prompt Anda)

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

## Akses Streamlit App melalui local
setelah aktivasi environment dan memastikan berada di lokasi direktori yang benar, maka jalankan command:

**streamlit run app.py**
