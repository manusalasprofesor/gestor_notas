# 📘 Gestor de notas
# Autor: [Tu nombre]
# Fecha: [fecha actual]

alumnos = {
    "Ana": 8.5,
    "Luis": 7.0,
    "Clara": 9.2
}

def calcular_media(diccionario):
    return sum(diccionario.values()) / len(diccionario)


print("📋 Listado de alumnos y notas:")
for nombre, nota in alumnos.items():
    print(f"{nombre}: {nota}")

print(f"\n📊 Nota media del grupo: {calcular_media(alumnos):.2f}")
