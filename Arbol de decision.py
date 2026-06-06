import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Cargar los datos del archivo CSV
print("Cargando los datos del proyecto...")
datos = pd.read_csv("datos_transporte.csv.csv")  # Asegúrate de que el archivo esté en la misma carpeta que este script
# Ver los datos en la consola para el reporte
print("\nPrimeras filas del dataset:")
print(datos.head())

# 2. Separar las variables de entrada (X) de la variable que queremos predecir (y)
# X son las características del viaje
X = datos[['hora_pico', 'clima_lluvioso', 'accidente_via']]
# y es el resultado (si se retrasó o no)
y = datos['retrasado']

# 3. Dividir los datos: 80% para entrenar el modelo y 20% para hacer pruebas
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Crear el modelo de Árbol de Decisión
print("\nEntrenando el modelo de Inteligencia Artificial...")
modelo = DecisionTreeClassifier(max_depth=3) 
modelo.fit(X_entrenamiento, y_entrenamiento)

# 5. Hacer predicciones con los datos de prueba para verificar si funciona
predicciones = modelo.predict(X_prueba)

# 6. Calcular la precisión del modelo (Accuracy)
precision = accuracy_score(y_prueba, predicciones)

print("\n--- RESULTADOS DE LAS PRUEBAS ---")
print(True if precision > 0.7 else False) # Un chequeo rápido
print(f"La precisión del modelo es del: {precision * 100}%")

# 7. Prueba interactiva: El usuario ingresa los datos por consola
print("\n=============================================")
print("  NUEVA PREDICCIÓN CON EL ÁRBOL DE DECISIÓN  ")
print("=============================================\n")

# Pedimos los datos al usuario (se escribe 1 para SÍ y 0 para NO)
v_hora = int(input("¿Es hora pico? (Escribe 1 para SÍ / 0 para NO): "))
v_clima = int(input("¿Está lloviendo? (Escribe 1 para SÍ / 0 para NO): "))
v_accidente = int(input("¿Hay algún accidente en la vía? (Escribe 1 para SÍ / 0 para NO): "))

# Convertimos las respuestas en el formato que entiende el modelo
viaje_usuario = pd.DataFrame([[v_hora, v_clima, v_accidente]], columns=['hora_pico', 'clima_lluvioso', 'accidente_via'])

# El modelo hace la predicción en base a lo que escribiste
resultado_prediccion = modelo.predict(viaje_usuario)

print("\n---------------------------------------------")
if resultado_prediccion[0] == 1:
    print("PREDICCIÓN: El autobús se va a RETRASAR. 🔴")
else:
    print("PREDICCIÓN: El autobús llegará A TIEMPO. 🟢")
print("---------------------------------------------")