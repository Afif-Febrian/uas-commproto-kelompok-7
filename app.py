from flask import Flask, request, jsonify
import pandas as pd
import os
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

CSV_FILE = "data/students.csv"

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "API Ingestion Dataset Running"
    })


@app.route("/ingest", methods=["POST"])
def ingest():

    data = request.get_json()

    # Validasi
    required_fields = ["id", "nama", "umur", "jurusan"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"{field} wajib diisi"
            }), 400

    new_data = pd.DataFrame([data])

    if os.path.exists(CSV_FILE) and os.path.getsize(CSV_FILE) > 0:
        old_data = pd.read_csv(CSV_FILE)
        new_data = pd.concat([old_data, new_data], ignore_index=True)

    new_data.to_csv(CSV_FILE, index=False)

    return jsonify({
        "status": "success",
        "message": "Data berhasil disimpan"
    })

@app.route("/students", methods=["GET"])
def get_students():

    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        return jsonify({
            "status": "success",
            "data": []
        })

    df = pd.read_csv(CSV_FILE)

    return jsonify({
        "status": "success",
        "data": df.to_dict(orient="records")
    })

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        return jsonify({
            "status": "error",
            "message": "Data tidak ditemukan"
        }), 404

    df = pd.read_csv(CSV_FILE)

    # Ubah kolom id menjadi integer
    df["id"] = pd.to_numeric(df["id"], errors="coerce")

    if id not in df["id"].tolist():
        return jsonify({
            "status": "error",
            "message": f"Data dengan ID {id} tidak ditemukan"
        }), 404

    df = df[df["id"] != id]

    df.to_csv(CSV_FILE, index=False)

    logging.info(f"DELETE /students/{id} - Data berhasil dihapus")

    return jsonify({
        "status": "success",
        "message": f"Data dengan ID {id} berhasil dihapus"
    })

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        return jsonify({
            "status": "error",
            "message": "Data tidak ditemukan"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Body JSON tidak boleh kosong"
        }), 400

    df = pd.read_csv(CSV_FILE)

    df["id"] = pd.to_numeric(df["id"])

    if id not in df["id"].values:
        return jsonify({
            "status": "error",
            "message": f"Data dengan ID {id} tidak ditemukan"
        }), 404

    if "nama" in data:
        df.loc[df["id"] == id, "nama"] = data["nama"]

    if "umur" in data:
        df.loc[df["id"] == id, "umur"] = data["umur"]

    if "jurusan" in data:
        df.loc[df["id"] == id, "jurusan"] = data["jurusan"]

    df.to_csv(CSV_FILE, index=False)

    logging.info(f"PUT /students/{id} - Data berhasil diperbarui")

    return jsonify({
        "status": "success",
        "message": f"Data dengan ID {id} berhasil diperbarui"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "API Ingestion Dataset"
    })

@app.route("/students", methods=["DELETE"])
def delete_all_students():

    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)

        return jsonify({
            "status": "success",
            "message": "Semua data berhasil dihapus"
        })

    return jsonify({
        "status": "success",
        "message": "Tidak ada data untuk dihapus"
    })

if __name__ == "__main__":
    app.run(debug=True)