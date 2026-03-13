"""
main.py - Programa principal del Zoologico.
"""

import os
import sys

from helpers import (
    CARACTERISTICAS,
    agregar_animal,
    animales_a_rows,
    cargar_csv,
    clases_dict,
    guardar_csv,
    listar_por_caracteristica,
    listar_por_clase,
    pedir_binario,
    pedir_entero,
    rows_a_animales,
)

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
DATA_DIR   = os.path.join(BASE_DIR, "data")
CLASES_CSV = os.path.join(DATA_DIR, "clases.csv")
ZOO_CSV    = os.path.join(DATA_DIR, "zoo.csv")
ZOO_FIELDS = ["nombre_animal"] + CARACTERISTICAS + ["clase"]

# Pantalla

def separador():
    print("-" * 50)


def imprimir_tabla(animales, clases):
    if not animales:
        print("  No se encontraron animales.")
        return
    col = max(len(a.nombre) for a in animales) + 2
    print(f"\n  {'Animal':<{col}} Clase")
    separador()
    for a in animales:
        print(f"  {a.nombre.capitalize():<{col}} {clases.get(a.clase, str(a.clase))}")
    print(f"\n  Total: {len(animales)} animal(es)")

# Opciones del menu

def opcion_listar_clase(animales, clases):
    print("\nClases disponibles:")
    for cid, nombre in sorted(clases.items()):
        print(f"  {cid}. {nombre}")
    clase_id = pedir_entero("Selecciona la clase", 1, max(clases))
    resultado = listar_por_clase(animales, clase_id)
    print(f"\nAnimales de clase: {clases[clase_id]}")
    imprimir_tabla(resultado, clases)


def opcion_listar_caracteristica(animales, clases):
    print("\nCaracteristicas disponibles:")
    for i, c in enumerate(CARACTERISTICAS, 1):
        print(f"  {i:>2}. {c}")
    idx   = pedir_entero("Selecciona la caracteristica", 1, len(CARACTERISTICAS))
    caract = CARACTERISTICAS[idx - 1]
    resultado = listar_por_caracteristica(animales, caract)
    print(f"\nAnimales con '{caract}':")
    imprimir_tabla(resultado, clases)


def opcion_agregar(animales, clases):
    nombre = input("\n  Nombre del animal: ").strip().lower()
    if not nombre:
        print("  El nombre no puede estar vacio.")
        return

    print("\n  Ingresa las caracteristicas (0 = No, 1 = Si):\n")
    caract = {}
    for c in CARACTERISTICAS:
        if c == "patas":
            caract[c] = pedir_entero("patas", 0, 8)
        else:
            caract[c] = pedir_binario(c)

    print("\n  Clases disponibles:")
    for cid, nombre_clase in sorted(clases.items()):
        print(f"    {cid}. {nombre_clase}")
    clase_id = pedir_entero("Selecciona la clase", 1, max(clases))

    try:
        nuevo = agregar_animal(animales, nombre, caract, clase_id)
        print(f"\n  Animal agregado:\n\n{nuevo}")
    except ValueError as e:
        print(f"\n  Error: {e}")

# Menu principal

def menu(animales, clases):
    while True:
        print("\n" + "=" * 50)
        print("  ZOOLOGICO")
        print("=" * 50)
        print(f"  Animales en el sistema: {len(animales)}\n")
        print("  1. Ver todos los animales")
        print("  2. Listar por clase")
        print("  3. Listar por caracteristica")
        print("  4. Agregar animal")
        print("  5. Salir")
        separador()

        opcion = input("  Opcion: ").strip()

        if opcion == "1":
            imprimir_tabla(animales, clases)

        elif opcion == "2":
            opcion_listar_clase(animales, clases)

        elif opcion == "3":
            opcion_listar_caracteristica(animales, clases)

        elif opcion == "4":
            opcion_agregar(animales, clases)
            while True:
                otro = input("\n  Agregar otro animal? (s/n): ").strip().lower()
                if otro == "s":
                    opcion_agregar(animales, clases)
                else:
                    break

        elif opcion == "5":
            break

        else:
            print("  Opcion invalida.")

        input("\n  Presiona ENTER para continuar...")


# Inicio

def main():
    try:
        clases_rows   = cargar_csv(CLASES_CSV)
        animales_rows = cargar_csv(ZOO_CSV)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    clases   = clases_dict(clases_rows)
    animales = rows_a_animales(animales_rows)

    menu(animales, clases)

    print("\nGuardando cambios...")
    guardar_csv(ZOO_CSV, animales_a_rows(animales), ZOO_FIELDS)
    print("Datos guardados. Hasta luego.")


if __name__ == "__main__":
    main()
