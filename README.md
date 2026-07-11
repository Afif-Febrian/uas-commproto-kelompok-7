# UAS Communication Protocol Kelompok 7
## API Ingestion Dataset Service

## Deskripsi Project
Project ini merupakan implementasi REST API menggunakan Flask untuk melakukan proses ingestion, penyimpanan, dan pengelolaan data mahasiswa menggunakan format JSON/CSV. Selain implementasi API, project ini juga mencakup analisis komunikasi jaringan menggunakan Wireshark serta penerapan reliability dan observability melalui logging, health check, dan error handling.

---

## Tujuan Project

- Mengimplementasikan REST API menggunakan framework Flask.
- Melakukan pengelolaan data menggunakan metode CRUD (Create, Read, Update, Delete).
- Menerapkan konsep API ingestion pada dataset mahasiswa.
- Menganalisis komunikasi jaringan HTTP menggunakan Wireshark.
- Mengimplementasikan logging, monitoring, dan health check pada layanan API.
- Menyusun dokumentasi dan presentasi hasil implementasi project.

---

## Teknologi yang Digunakan

- Python
- Flask
- JSON
- CSV
- Postman
- Wireshark
- Git
- GitHub

---

## Cara Instalasi

Clone repository:

```bash
git clone https://github.com/Afif-Febrian/uas-commproto-kelompok-7.git
```

Masuk ke folder project:

```bash
cd uas-commproto-kelompok-7
```

Install dependency yang diperlukan:

```bash
pip install -r requirements.txt
```

---

## Cara Menjalankan Project

Jalankan aplikasi menggunakan perintah berikut:

```bash
python app.py
```

Server akan berjalan pada alamat:

```text
http://127.0.0.1:5000
```
## Postman Collection

Untuk mempermudah pengujian API, import file collection berikut ke Postman:

```text
Postman/collection.json




## Daftar Endpoint API

| Method | Endpoint | Fungsi |
|--------|----------|--------|
| GET | `/` | Menampilkan halaman utama API |
| POST | `/ingest` | Menambahkan data mahasiswa baru |
| GET | `/students` | Menampilkan seluruh data mahasiswa |
| PUT | `/students/<id>` | Memperbarui data mahasiswa berdasarkan ID |
| DELETE | `/students/<id>` | Menghapus data mahasiswa berdasarkan ID |
| GET | `/health` | Mengecek status layanan API |

---

Pengujian API dilakukan menggunakan Postman untuk memastikan seluruh endpoint berjalan dengan baik dan menghasilkan response yang sesuai.

Analisis komunikasi jaringan dilakukan menggunakan Wireshark untuk mengamati proses request dan response HTTP yang terjadi antara client dan server.

---

## Repository

Repository ini digunakan sebagai media penyimpanan source code, dokumentasi, hasil pengujian, dan kebutuhan presentasi project UAS Communication Protocol Kelompok 7.
