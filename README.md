# Verificador de Tipo de Triángulo

## Ubicación del programa

El script se encuentra en:

```
prueba1/triangulo.py
```

## Requisitos

- Tener instalado **Python 3 o superior** 
- Verificar la instalación ejecutando en la terminal:

  ```
  python --version
  ```

  o, según el sistema:

  ```
  python3 --version
  ```

## Cómo ejecutar el programa

1. Abrir una terminal (PowerShell, CMD, Bash, etc.).
2. Ubicarse en la carpeta `prueba1`:

   ```
   cd ruta\hacia\prueba1
   ```

3. Ejecutar el script:

   ```
   python triangulo.py
   ```

4. El programa pedirá los 3 lados del triángulo, uno por uno:

   ```
   INGRESE EL LADO A DEL TRIANGULO:
   INGRESE EL LADO B DEL TRIANGULO:
   INGRESE EL LADO C DEL TRIANGULO:
   ```

5. Ingresar un número (entero o decimal) para cada lado y presionar `Enter`.

## Cómo funciona

El programa sigue estos pasos:

1. **Solicitud de datos**: pide los valores de los lados A, B y C mediante la
   función `pedir_lado()`. Esta función valida que:
   - El valor ingresado sea un número (si no lo es, muestra
     `"Valor invalido. Ingrese un numero."` y vuelve a pedirlo).
   - El número sea positivo (si es cero o negativo, muestra
     `"El lado debe ser un numero positivo."` y vuelve a pedirlo).

2. **Validación de triángulo**: antes de clasificar, el programa comprueba la
   **desigualdad triangular** (la suma de dos lados siempre debe ser mayor
   que el tercero). Si no se cumple, no es un triángulo válido y se muestra:

   ```
   LOS VALORES INGRESADOS NO FORMAN UN TRIANGULO
   ```

3. **Clasificación**: si los lados forman un triángulo válido, se comparan
   entre sí:
   - Si **A = B = C** (los 3 lados iguales) → `EL TRIANGULO ES EQUILATERO`
   - Si exactamente **2 lados son iguales** → `EL TRIANGULO ES ISOSCELES`
   - Si **los 3 lados son diferentes** → `EL TRIANGULO ES ESCALENO`

## Ejemplos de uso

**Triángulo equilátero:**

```
INGRESE EL LADO A DEL TRIANGULO: 3
INGRESE EL LADO B DEL TRIANGULO: 3
INGRESE EL LADO C DEL TRIANGULO: 3
EL TRIANGULO ES EQUILATERO
```

**Triángulo isósceles:**

```
INGRESE EL LADO A DEL TRIANGULO: 5
INGRESE EL LADO B DEL TRIANGULO: 5
INGRESE EL LADO C DEL TRIANGULO: 8
EL TRIANGULO ES ISOSCELES
```

**Triángulo escaleno:**

```
INGRESE EL LADO A DEL TRIANGULO: 3
INGRESE EL LADO B DEL TRIANGULO: 4
INGRESE EL LADO C DEL TRIANGULO: 5
EL TRIANGULO ES ESCALENO
```

**Valores que no forman un triángulo:**

```
INGRESE EL LADO A DEL TRIANGULO: 1
INGRESE EL LADO B DEL TRIANGULO: 1
INGRESE EL LADO C DEL TRIANGULO: 10
LOS VALORES INGRESADOS NO FORMAN UN TRIANGULO
```
