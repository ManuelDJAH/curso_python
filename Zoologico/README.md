# 🦁 Sistema Zoológico

Programa de consola en Python para gestionar un catálogo de animales.  
Permite consultar, filtrar y agregar animales, con persistencia automática en archivos CSV.

---

## 📁 Estructura del proyecto

```
zoologico/
├── data/
│   ├── clases.csv        # Catálogo de clases (Mamífero, Ave, Reptil…)
│   └── zoo.csv           # Catálogo de animales con características
├── helpers.py            # Funciones auxiliares + clase Animal
├── main.py               # Lógica principal y menú interactivo
└── README.md             # Este archivo
```

---

## ▶️ Requisitos

- Python **3.10** o superior (se usan type hints modernos).
- No se requieren librerías externas; solo módulos de la biblioteca estándar (`csv`, `os`, `sys`).

---

## 🚀 Cómo iniciar el programa

1. Abre una terminal y navega a la carpeta del proyecto:

   ```bash
   cd zoologico
   ```

2. Ejecuta el programa:

   ```bash
   python main.py
   ```

   > En sistemas donde coexisten Python 2 y Python 3 usa `python3 main.py`.

---

## 🕹️ Cómo interactuar

Al arrancar verás el **menú principal**:

```
══════════════════════════════════════════════════════
  🦁  SISTEMA ZOOLÓGICO
══════════════════════════════════════════════════════

  Total de animales cargados: 93

  1. Ver todos los animales
  2. Listar animales por clase
  3. Listar animales por característica
  4. Agregar nuevo(s) animal(es)
  5. Salir
```

| Opción | Acción |
|--------|--------|
| **1** | Muestra la tabla completa de animales con su clase. |
| **2** | Pide elegir una clase (Mamífero, Ave, Reptil, etc.) y lista solo esos animales. |
| **3** | Pide elegir una característica (pelo, plumas, vuela, etc.) y lista los animales que la poseen. |
| **4** | Guía paso a paso para ingresar un nuevo animal: nombre, características (0/1 para cada rasgo, número de patas) y clase. Puede agregar varios animales seguidos. |
| **5** | **Guarda** automáticamente los cambios en `data/zoo.csv` y termina el programa. |

### ➕ Agregar un animal (opción 4)

El programa solicitará:

1. **Nombre** del animal.
2. **Cada característica** de forma individual:
   - Para rasgos binarios (pelo, plumas, vuela…): ingresa `0` (No) o `1` (Sí).
   - Para **patas**: ingresa el número exacto (0–8).
   - Para **tamanio_gato**: ingresa `0` si es más pequeño que un gato, `1` si es igual o más grande.
3. **Clase** a la que pertenece (número del 1 al 7).

Al terminar se preguntará si deseas agregar otro animal.

### 💾 Persistencia

Al seleccionar **Salir (5)**, los datos se graban en `data/zoo.csv`.  
La próxima vez que inicies el programa, los nuevos animales estarán disponibles automáticamente.

---

## 📋 Clases disponibles

| ID | Clase |
|----|-------|
| 1 | Mamífero |
| 2 | Ave |
| 3 | Reptil |
| 4 | Pez |
| 5 | Anfibio |
| 6 | Insecto |
| 7 | Invertebrado |

---

## 🔬 Características disponibles

`pelo` · `plumas` · `huevos` · `leche` · `vuela` · `acuatico` · `depredador` · `dientes` · `espinazo` · `respira` · `venenoso` · `aletas` · `patas` · `cola` · `domestico` · `tamanio_gato`

---

## 👤 Autor

**[Tu nombre completo aquí]**  
Proyecto: **Zoológico**
