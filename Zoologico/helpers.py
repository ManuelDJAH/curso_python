"""
helpers.py - Funciones auxiliares del programa Zoologico.
"""

import csv
import os

CARACTERISTICAS = [
    "pelo", "plumas", "huevos", "leche", "vuela", "acuatico",
    "depredador", "dientes", "espinazo", "respira", "venenoso",
    "aletas", "patas", "cola", "domestico", "tamanio_gato",
]

# Clase Animal

class Animal:
    def __init__(self, nombre: str, caracteristicas: dict, clase: int):
        self.nombre = nombre
        self.caracteristicas = {k: int(v) for k, v in caracteristicas.items()}
        self.clase = int(clase)

    def __str__(self):
        rasgos = [k for k, v in self.caracteristicas.items() if v > 0]
        return (
            f"Nombre : {self.nombre.capitalize()}\n"
            f"Clase  : {self.clase}\n"
            f"Rasgos : {', '.join(rasgos) if rasgos else 'ninguno'}"
        )

    def __repr__(self):
        return f"Animal(nombre={self.nombre!r}, clase={self.clase})"

    def to_dict(self):
        row = {"nombre_animal": self.nombre}
        row.update(self.caracteristicas)
        row["clase"] = self.clase
        return row

# Carga y escritura de CSV

def cargar_csv(filepath: str) -> list:
    """Carga cualquier archivo CSV y devuelve una lista de diccionarios."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No se encontro el archivo: {filepath}")
    registros = []
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        for fila in csv.DictReader(f):
            registros.append({k.strip(): v.strip() for k, v in fila.items()})
    return registros


def guardar_csv(filepath: str, registros: list, fieldnames: list) -> None:
    """Escribe una lista de diccionarios en un archivo CSV."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(registros)

# Conversion entre filas CSV y objetos Animal

def rows_a_animales(rows: list) -> list:
    animales = []
    for row in rows:
        nombre = row.get("nombre_animal", "").strip('"')
        clase  = row.get("clase", 0)
        caract = {k: row[k] for k in CARACTERISTICAS if k in row}
        animales.append(Animal(nombre, caract, clase))
    return animales


def animales_a_rows(animales: list) -> list:
    return [a.to_dict() for a in animales]

# Funciones de negocio

def clases_dict(rows: list) -> dict:
    return {int(r["Clase_id"]): r["Clase_tipo"] for r in rows}


def listar_por_clase(animales: list, clase_id: int) -> list:
    """Devuelve todos los animales que pertenecen a clase_id."""
    return [a for a in animales if a.clase == clase_id]


def listar_por_caracteristica(animales: list, caracteristica: str) -> list:
    """Devuelve todos los animales que tienen la caracteristica activa (> 0)."""
    if caracteristica not in CARACTERISTICAS:
        return []
    return [a for a in animales if a.caracteristicas.get(caracteristica, 0) > 0]


def agregar_animal(animales: list, nombre: str,
                   caracteristicas: dict, clase: int) -> Animal:
    """Agrega un nuevo Animal a la lista. Lanza ValueError si ya existe."""
    if nombre.lower() in {a.nombre.lower() for a in animales}:
        raise ValueError(f"El animal '{nombre}' ya existe.")
    nuevo = Animal(nombre, caracteristicas, clase)
    animales.append(nuevo)
    return nuevo


# Entradas

def pedir_binario(etiqueta: str) -> int:
    while True:
        v = input(f"  {etiqueta} (0/1): ").strip()
        if v in ("0", "1"):
            return int(v)
        print("  Ingresa 0 o 1.")


def pedir_entero(mensaje: str, minimo: int, maximo: int) -> int:
    while True:
        v = input(f"  {mensaje} ({minimo}-{maximo}): ").strip()
        if v.isdigit() and minimo <= int(v) <= maximo:
            return int(v)
        print(f"  Ingresa un numero entre {minimo} y {maximo}.")
