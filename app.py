from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import joblib

app = Flask(__name__)

# cargar modelo y scaler
model = tf.keras.models.load_model("modelo/modelo.h5")
scaler = joblib.load("modelo/scaler.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    tipo = None 

    if request.method == "POST":
        duration = float(request.form["duration"])
        protocol = float(request.form["protocol"])
        src_bytes = float(request.form["src_bytes"])
        dst_bytes = float(request.form["dst_bytes"])
        count = float(request.form["count"])

        data = np.array([[duration, protocol, src_bytes, dst_bytes, count]])

        # normalizar
        data_scaled = scaler.transform(data)

        pred = model.predict(data_scaled)
        prob = pred[0][0]

        if prob > 0.4:
            resultado = f"🚨 ATAQUE DETECTADO ({prob*100:.2f}%)"
            tipo = "ataque"
        else:
            resultado = f"✅ TRÁFICO NORMAL ({(1-prob)*100:.2f}%)"
            tipo = "normal"

    probabilidad = prob * 100 if resultado else 0
    return render_template("index.html", resultado=resultado, tipo=tipo, prob=probabilidad)

if __name__ == "__main__":
    app.run(debug=True)