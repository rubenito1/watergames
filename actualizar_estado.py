from datetime import datetime

# Opciones de estado
opciones = {
    "1": {
        "titulo": "✅ Funcionando",
        "texto": "El servidor está funcionando",
        "clase": "funcionando"
    },
    "2": {
        "titulo": "⚠️ Error",
        "texto": "",  # Se pide al usuario más abajo
        "clase": "error"
    },
    "3": {
        "titulo": "❌ Apagado",
        "texto": "Servidor apagado",
        "clase": "apagado"
    }
}

print("Elige un tipo de informe:")
print("1. Funcionando")
print("2. Error")
print("3. Apagado")
opcion = input("Opción: ").strip()

if opcion not in opciones:
    print("Opción inválida.")
    exit()

estado = opciones[opcion]

# Solo si es error, pedimos el texto personalizado
if opcion == "2":
    estado["texto"] = input("Escribe el texto del informe de error: ").strip()

# Obtener fecha/hora
ahora = datetime.now().strftime("%d/%m/%Y %H:%M")

# Generar HTML
html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Estado del Sistema</title>
  <style>
    body {{ font-family: sans-serif; text-align: center; padding: 2rem; }}
    .funcionando {{ color: green; font-weight: bold; }}
    .error {{ color: orange; font-weight: bold; }}
    .apagado {{ color: red; font-weight: bold; }}
  </style>
</head>
<body>
  <h1>Estado del Sistema</h1>
  <p class="{estado['clase']}">{estado['titulo']} {estado['texto']}</p>
  <p>Última actualización: {ahora}</p>
</body>
</html>"""

# Guardar archivo
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Archivo 'index.html' actualizado correctamente.")
