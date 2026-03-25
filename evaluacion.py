import pandas as pd
import tensorflow as tf
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


df = pd.read_csv("data/datos_limpios.csv")
X = df.drop("label", axis=1)
y = df["label"]



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



scaler = joblib.load("modelo/scaler.pkl")

X_test = scaler.transform(X_test)

#carga modelo
model = tf.keras.models.load_model("modelo/modelo.h5")

#predecir
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.4).astype(int)



cm = confusion_matrix(y_test, y_pred)

print("Matriz de confusión:")
print(cm)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")

plt.title("Matriz de Confusión - Detección de Intrusos")
plt.show()