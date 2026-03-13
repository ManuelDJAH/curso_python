## Autor

**Manuel de Jesus Arvayo Heraldez**  

---

# Zoologico

Programa en Python para gestionar un catalogo de animales.
Permite consultar y filtrar animales por clase o caracteristica, y agregar nuevos animales.
Los cambios se guardan automaticamente al salir.

## Estructura

```
zoologico/
├── data/
│   ├── clases.csv
│   └── zoo.csv
├── helpers.py
├── main.py
└── README.md
```

## Como iniciar

```bash
cd zoologico
python main.py
```

## Menu

```
==================================================
  ZOOLOGICO
==================================================
  Animales en el sistema: 93

  1. Ver todos los animales
  2. Listar por clase
  3. Listar por caracteristica
  4. Agregar animal
  5. Salir
```

- **Opcion 1**: Muestra todos los animales con su clase.
- **Opcion 2**: Pide seleccionar una clase y muestra los animales de esa clase.
- **Opcion 3**: Pide seleccionar una caracteristica y muestra los animales que la tienen.
- **Opcion 4**: Guia para ingresar un nuevo animal paso a paso. Puede agregar varios seguidos.
- **Opcion 5**: Guarda los cambios en `data/zoo.csv` y termina el programa.

## Agregar un animal

El programa pide:
1. Nombre del animal
2. Cada caracteristica: ingresar 0 (No) o 1 (Si). Para patas, ingresar el numero (0-8).
3. La clase a la que pertenece (1-7)

## Clases

| ID | Clase        |
|----|--------------|
| 1  | Mamifero     |
| 2  | Ave          |
| 3  | Reptil       |
| 4  | Pez          |
| 5  | Anfibio      |
| 6  | Insecto      |
| 7  | Invertebrado |
