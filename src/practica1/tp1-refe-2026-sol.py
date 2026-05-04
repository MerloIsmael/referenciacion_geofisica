# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] editable=true slideshow={"slide_type": ""}
# # Trabajo Práctico 1 de Referenciación en Geofísica (2026)
#
# Luciano P. O. Mendoza (lmendoza@fcaglp.unlp.edu.ar)

# %% [markdown]
# ## Notas acerca de Jupyter
#
# - Para **ejecutar** una celda hay que seleccionarla y oprimir SHIFT+ENTER.
# - Para agregar una nueva celda abajo oprimir B o usar el botón + del menu superior.
# - Para agregar una nueva celda arriba oprimir A.
# - Para **guardar** el cuaderno oprimir SHIFT+S o usar el botón *floppy disk* del menú superior.
# - Usar el menú desplegable superior para seleccionar entre los tres tipos de celdas posibles
#   - *Code* para calculo (por ejemplo, como calculadora científica)
#   - *Markdown* para texto con formato, ecuaciones matemáticas, imágenes, etc.
#   - *Raw* para texto simple.

# %% [markdown]
# # Ejercicios

# %% [markdown]
# ## Ejercicio 1
#
# ### Enunciado

# %% [markdown]
# Dados la siguiente matriz $A$ y el vector columna $b$
# $$
# \begin{aligned}
# A &=
# \begin{pmatrix}
# 5 & 5 & 7 & 8\\
# 4 & 7 & 1 & 1\\
# 4 & 4 & 2 & 1\\
# 2 & 4 & 0 & 3
# \end{pmatrix}\\
# b &=
# \begin{pmatrix}
# 2\\3\\7\\9
# \end{pmatrix}
# \end{aligned}
# $$
# calcule las siguientes operaciones
# $$
# B =A^{-1}\qquad
# C = A^T\qquad
# a = Ab\qquad
# c = A^T b= C b\qquad
# d = \mathrm{traza}(A)
# $$

# %%
# resolver acá
1 + 1

# %% [markdown]
# ### Resolución

# %%
# primero que nada, importamos el módulo numpy, empleando el "diminutivo" np...
import numpy as np

# e importamos el módulo de algebra lineal linalg...
from scipy import linalg

# %%
# definimos la matriz A (por filas)...
A = np.array([[5,5,7,8],
              [4,7,1,1],
              [4,4,2,1],
              [2,4,0,3]])

# definimos el vector columna b (por filas)...
b = np.array([[2],
              [3],
              [7],
              [9]])

# mostramos A y b...
print(A)
print(b)

# %% [markdown]
# Ahora, con los datos cargados en la memoria (la RAM) de la computadora, podemos realizar las operaciones solicitadas inmediatamente

# %%
B = linalg.inv(A) # esto debe ser una matriz cuadrada
C = A.transpose() # aplicamos el método de transponer
a = A @ b         # este debe ser un vector columna
c = C @ b         # este debe ser un vector columna
d = A.trace()     # esto resultará un escalar

print(B)
print(C)
print(a)
print(c)
print(d)

# %% [markdown]
# ## Ejercicio 2
#
# ### Enunciado
#
# Dados los siguientes dos vectores de $\mathbb{R}^2$
# $$
# \begin{aligned}
# \mathbf{a}&=
# \begin{pmatrix}
# 2\\
# 3
# \end{pmatrix}\\
# \mathbf{b}&=
# \begin{pmatrix}
# -1\\
# \phantom{-}4
# \end{pmatrix}
# \end{aligned}
# $$
# indicar si son o no ortogonales.
#
# ### Notas
#
# * Utilice la función [sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html) de NumPy, el producto __elemento a elemento__ (o sea, *, no @), y la estructura [if](https://docs.python.org/3/tutorial/controlflow.html), de Python.
# * Suponer aquí que Python trabaja con precisión infinita (algo incorrecto) y que, de ser ortogonales, el producto punto será **exactamente** cero. ¡En el siguiente ejercicio habrá que tener más cuidado!

# %%
# resolver acá
1 + 1

# %% [markdown]
# ### Resolución

# %%
a = np.array([[2],
              [3]])
     
b = np.array([[-1],
              [ 4]])

p = np.sum(a * b)

# un método
if p == 0:
    print("¡Son ortogonales!")
else:
    print("¡No son ortogonales!")

# otro método
if p != 0:
    print("¡No son ortogonales!")
else:
    print("¡Son ortogonales!")

# %% [markdown]
# ## Ejercicio 3
#
# ### Enunciado
#
# Dados dos vectores $\mathbf{a},\mathbf{b}$ cualesquiera, pertenecientes a $\mathbb{R}^n$, escribir funciones que indiquen si son paralelos/antiparalelos, ortogonales o ninguno de las dos anteriores.
#
# ### Notas
#
# * Tenner en cuenta que Python, por defecto, trabaja con precisión finita, por lo que comparaciones **exactas** de resultados no son seguras (por ejemplo, $=0$ o $\ne 0$ o $= 1$ o $\ne 1$). Es recomendable entonces comparar contra un **número muy pero muy pequeño**, utilizando la función [abs](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html).
# * En Python, la _norma 2_ (i.e., $|\quad|$) de un vector o matriz se calcula con las funciones de Numpy/SciPy [linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html).
# * Definir subprogramas, subrutinas o funciones, en Python o en cualquier lenguaje, ayuda a hacer el código más claro, menos propenso a errores y más fácil de corregir o mejorar.
# * ¡Recuerde que una función puede *llamar* o utilizar otras funciones ya definidas!
# * ¡Es **muy importante** nunca nombrar variables o funciones utilizando nombres de constantes o funciones de Python! Está es una muy común fuente de error. Por ejemplo, nunca definir constantes que se llamen sin, cos, min, max, pi, e, tan, atan, etc.
# * Recordar que existen constantes especiales "True" y "False" para indicar el resultado de las comparaciones. Por ejemplo

# %%
1 > 0

# %%
1 < 0

# %%
2 + 2 == 4

# %%
2 + 2 != 4

# %%
1.5 > -6

# %%
# resolver acá
1 + 1

# %% [markdown]
# ### Resolución
#
# Primero, definiremos una **función** que indique simplemente si dos vectores son ortogonales o no. Para eso utilizamos el *producto punto* o *producto interno* entre dos vectores de $\mathbb{R}^n$
# $$
# r = \mathbf{a}\cdot \mathbf{b} = \sum_{i=1}^n a_i b_i
# $$
# que indicará que $\mathbf{a}$ y $\mathbf{b}$ son ortogonales si y solo si $r=0$.
#
# Pero, como por defecto Python representa los números reales con precisión finita (como la mayoría de los lenguajes: Fortran, Octave, C, etc.) debemos reemplazar está condición por $|r| \le$ *un número muy pequeño*.
#
# Como esto es tan común en programación Python ya tiene definido ese *número pequeño*, se llama *eps* (este número puede variar de computadora a computadora...). Python, además, define automáticamente otras constantes útiles

# %%
np.finfo(float).eps

# %%
np.e

# %%
np.pi


# %% [markdown]
# Entonces, definimos nuestra primer función en Python

# %%
# Función para comprobar si dos vectores son o no ortogonales.
# si r = 1 entonces SÍ son ortogonales
# si r = 0 entonces NO son ortogonales
# utilizamos el producto punto
# utilizamos la "precisión" de la computadora "eps"
def sonortogonales(a,b):
    p = np.sum(a*b)
    return np.abs(p) <= np.finfo(float).eps # True o False...    


# %% [markdown]
# Podemos probar inmediatamente la función ¡notando que es independiente de la dimensión del espacio donde viven los vectores!

# %%
# estos sí son ortogonales
sonortogonales(np.array([1,0]),np.array([0,1]))

# %%
# estos no son ortogonales
sonortogonales(np.array([1,0]),np.array([1,1]))

# %%
# estos son "casi" ortogonales...
sonortogonales(np.array([1,0,0,0,0,0]),np.array([1,0,0,0,0,0.000000001]))

# %%
# estos no son ortogonales
sonortogonales(np.array([1,0,0,0,0,0]),np.array([1,0,0,0,0,1]))

# %%
# el vector "nulo" es ortogonal a todos los demás...
sonortogonales(np.array([1,2,3]),np.array([0,0,0]))


# %% [markdown]
# De manera similar podemos ahora escribir una función que indique si dos vectores son o no son paralelos (o antiparalelos) usando el coseno del ángulo $\theta$ *subtendido* por los vectores
# $$
# \cos\theta = \frac{\mathbf{a}\cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}
# $$
# Donde $\cos\theta = 1$ indica paralelismo y $\cos\theta = -1$ indica antiparalelismo. Estás dos condiciones pueden *representarse* juntas como $|\cos\theta| - 1 = 0$.

# %%
# Función para comprobar si dos vectores son o no paralelos o antiparalelos.
# si r = 1 entonces SÍ son paralelos o antiparalelos
# si r = 0 entonces NO son paralelos ni antiparalelos
# utilizamos el producto punto y el ángulo subtendido
# utilizamos la "precisión" de la computadora "eps"
def sonparalelos(a,b):
    p = np.sum(a*b)
    costheta = p/(linalg.norm(a)*linalg.norm(b))
    return np.abs(np.abs(costheta) - 1) <= np.finfo(float).eps


# %%
# estos sí son paralelos
sonparalelos(np.array([1,1]),np.array([2,2]))

# %%
# estos sí son paralelos
sonparalelos(np.array([0,0,1,0]),44*np.array([0,0,1,0]))

# %%
# estos sí son antiparalelos
sonparalelos(np.array([1,0]),np.array([-2,0]))

# %%
# esto no son paralelos ni antiparalelos
sonparalelos(np.array([1,0,0]),np.array([0,1,1]))

# %%
# el vector nulo no tiene definido un paralelismo
# y nuestra función fallará...
sonparalelos(np.array([1,0]),np.array([0,0]))


# %% [markdown]
# Ahora podemos escribir una última función que de respuesta al enunciado del ejercicio. En este caso, no queremos que regrese ningún resultado, sino que **escriba** alguna de las tres respuestas: *ortogonales*, *paralelos/antiparalelos* o *ni ortogonales ni paralelos/antiparalelos*. ¡Notar que nuestra función **utilizará** las dos funciones anteriores!

# %%
# función que escribe la respuesta correcta
def f(a,b):
    if sonortogonales(a,b):
        print("ortogonales")
        return
    
    if sonparalelos(a,b):
        print("paralelos/antiparalelos")
        return
    
    print("ni ortogonales ni paralelos/antiparalelos")


# %% [markdown]
# Ahora probamos la función *f*

# %%
# definimos varios vectores de prueba
a = np.array([1,2])
b = -3*a
c = np.array([-2,1])
d = np.array([1,3])

# %%
# comprobemos que a y b son antiparalelos
f(a,b)

# %%
# comprobemos que a y c son ortogonales
f(a,c)

# %%
# comprobemos que b y c son ortogonales
f(b,c)

# %%
# comprobemos que c y d no son ni ortogonales ni paralelos
f(c,d)

# %% [markdown]
# ## Ejercicio 4
#
# ### Enunciado
#
# El archivo [sismos.txt](sismos.txt) contiene la época (año, mes, día, hora, minuto y
# segundo), la posición del hipocentro (latitud, longitud y profundidad) y la magnitud de
# sismos ocurridos en todo el mundo.
#
# De este archivo extraer, utilizando Python, la siguiente información:
#
# 1. Cuándo y donde se produjo el terremoto de mayor magnitud.
# 2. Cuando y donde se produjeron los terremotos de mayor y menor profundidad.
# 3. El año en qué se produjeron la mayor cantidad de sismos en el mundo.
# 4. Filtrar el archivo original y generar una tabla (i.e., una matriz) con los terremotos en Sudamérica (aproximar los límites del continente con un rectángulo, buscando los vértices en una mapa o con el _software_ [GoogleEarth](https://earth.google.com/web/)).
# 5. Buscar el terremoto de mayor magnitud ocurrido en Sudamérica, y decir cuándo y dónde se produjo.
# 6. Salvar en un archivo de texto la tabla con los sismos en Sudamérica obtenida en el inciso 4.

# %% [markdown]
# ### Notas
#
# * Python permite *leer* (es decir, cargar en la memoria RAM) archivos de datos, tanto en formato texto como en formato binario. Así mismo, Python permite *salvar* (es decir, guardar) resultados o datos en archivos, tanto de texto como binarios.
# * Pueden utilizarse diversas funciones para leer o escribir acrhivos de datos.
# * La función más sencilla para *cargar* datos, aunque algo limitada, es [loadtxt](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html).
# * La función más sencilla para *guardar* el valor de las variables o los resultados es [savetxt](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html).

# %%
# resolver acá
1 + 1

# %% [markdown]
# ### Resolución
#
# Primero, debemos *leer* las columnas del archivo [sismos.txt](sismos.txt).
#
# **Siempre** tenemos que abrir el archivo de datos con un visor de texto **antes** de cargarlo en Python, y constatar visualmente los datos, mirando, por ejemplo
# * ¿de qué tipo son (enteros, reales, texto)?
# * ¿En qué unidades están (metros, kilómetros, grados, radianes, etc.)?
# * ¿Hay coordenadas geográficas, o geodésicas, o cartesianas, o proyectadas, etc.?
# * ¿Tiene *agujeros* (renglones en blanco)?
# * ¿Todas las columnas tienen la misma extensión? Es decir, ¿todas las filas de datos están *completas*?) 
#
# Entonces, podemos cargar el archivo así

# %%
A = np.loadtxt("sismos.txt")

# %% [markdown]
# Lo primero que podemos hacer es averiguar cuantos sismos componenen la lista

# %%
nsismos = np.shape(A)[0] # cuantas filas tiene A?
print(nsismos)

# %% [markdown]
# Ahora podemos ver, por ejemplo, los datos del primer sismo listado

# %%
i = 0
print(A[i,:])

# %% [markdown]
# O podemos ver, por ejemplo, los datos de los sismos 100 al 102 (tres sismos)

# %%
i = range(99,102)
print(A[i,:])

# %% [markdown]
# O podemos ver, por ejemplo, los datos del  último sismo listado

# %%
i = nsismos - 1 # los índice empiezan en 0!!!
print(A[i,:])

# %% [markdown]
# Ahora estamos listos para resolver inciso a inciso.
#
# ##### Inciso 1

# %%
# sismo de mayor magnitud
i = 9 # índice de la columan de magnitudes...
magmax = np.max(A[:,i])
imagmax = np.argmax(A[:,i])

print(magmax,imagmax)

# %% [markdown]
# Esto nos indica que el sismo de máxima magnitud está listado en la fila 436 (¡los índices comienzan en 0!), y que su magnitud fue 9.
#
# Con esta información podemos inmediatamente responder al donde y el cuando

# %%
j = imagmax
print(A[j,:])

# %% [markdown]
# #### Inciso 2

# %%
# sismo a mayor profundidad
i = 8 # índice de la columna de profundidades...
profmax = np.max(A[:,i])
iprofmax = np.argmax(A[:,i])
print(profmax,iprofmax)

j = iprofmax
print(A[j,:])

# %%
# sismo a menor profundidad
i = 8 # índice de la columna de profundidades...
profmin = np.min(A[:,i])
iprofmin = np.argmin(A[:,i])
print(profmin,iprofmin)

j = iprofmin
print(A[j,:])

# %% [markdown]
# #### Inciso 3
#
# Primero debemos obtener una lista de todos los años incluidos en el archivo, con la función *unique*

# %%
i = 0 # índice de la columna de años...
[ListaAnios,CantidadPorAnio] = np.unique(A[:,i], return_counts = True)
print(ListaAnios)
print(CantidadPorAnio)

# %% [markdown]
# Donde vemos que hay datos de seis años (de 2002 a 2007, inlcuido), y obtenemos el número de sismos (es decir, filas) a lo largo de los años.
#
# Por ejemplo, ahora sabemos que en 2002 ocurrieron 139 sismos.

# %% [markdown]
# Ahora ya podemos resolver el inciso

# %%
# en que año ocurrieron más sismos
CantidadMax = np.max(CantidadPorAnio)
iCantidadMax = np.argmax(CantidadPorAnio)

AnioConMas = ListaAnios[iCantidadMax]
print(CantidadMax,iCantidadMax,AnioConMas) # los índices arrancan en cero!!!

# %% [markdown]
# #### Inciso 4
#
# Primero debemos definir los límites Oeste/Este y Sur/Norte de Sudamérica, buscando en un mapa, Wikipedia o Googleearth. Por ejemplo, podrían ser así

# %%
# límites de Sudamérica
lonmin = -82.5 # grados
lonmax = -33.0 # grados
latmin = -56.5 # grados
latmax = +13.0 # grados
print(lonmin,lonmax,latmin,latmax)

# %% [markdown]
# Ahora **buscamos o filtramos** todos los sismos (es decir, todas las filas) que cumplan **sumultáneamente** las siguientes condiciones
# $$
# \lambda_\textrm{min} \le \lambda \le \lambda_\textrm{max}\qquad\varphi_\textrm{min} \le \varphi \le \varphi_\textrm{max}
# $$

# %%
# ¿qué filas satisfacen simultáneamente las CUATRO condiciones?
# acá usamos que True*True = True, pero True*False = False y False*False = False
# es decir, & es el AND lógico, pero aplicado elemento a elemento...
ilat = 6 # índice de la columna de latitudes...
ilon = 7 # índice de la columna de longitudes...
i = (lonmin <= A[:,ilon]) & (lonmax >= A[:,ilon]) & (latmin <= A[:,ilat]) & (latmax >= A[:,ilat])

# ¿cuantas filas cunplen las condiciones, es decir, son True?
# acá usamos que False equivale a 0, y True equivale a no cero...
print(np.count_nonzero(i))

# ¿que porcentaje del total son?
print(100*np.count_nonzero(i)/nsismos)

# %% [markdown]
# Ahora estamos en condiciones de definir un nuevo conjunto de datos, que solo contenga las filas que encontramos

# %%
AenSA = A[i,:]

# %% [markdown]
# #### Inciso 5

# %%
# sismo de mayor magnitud en Sudamérica
i = 9 # índice de la columna de magnitudes...
magmax = np.max(AenSA[:,i])
imagmax = np.argmax(AenSA[:,i])

print(AenSA[imagmax,:])

# %% [markdown]
# #### Inciso 6
#
# Ahora podemos *salvar* (es decir, guardar) el resultado del filtrado o búsqueda de datos en Sudamérica en un archivo de texto.

# %%
np.savetxt("sismosenSA.txt",AenSA)

# %% [markdown]
# Naturalmente, **debemos** verificar el éxito de la operación abriendo el archivo *sismosenSA.txt* y verificando visualmente que es correcto.
#
# ### Resolución completa
#
# Al fin, el ejercicio completo podría ser resuelto así

# %%
A = np.loadtxt("sismos.txt")

nsismos = np.shape(A)[0] # cuantas filas tiene A?
print(nsismos)

# inciso 1

# sismo de mayor magnitud
i = 9 # índice de la columan de magnitudes...
magmax = np.max(A[:,i])
imagmax = np.argmax(A[:,i])
print(magmax,imagmax)

j = imagmax
print(A[j,:])

# inciso 2

# sismo a mayor profundidad
i = 8 # índice de la columna de profundidades...
profmax = np.max(A[:,i])
iprofmax = np.argmax(A[:,i])
print(profmax,iprofmax)

j = iprofmax
print(A[j,:])

# sismo a menor profundidad
i = 8 # índice de la columna de profundidades...
profmin = np.min(A[:,i])
iprofmin = np.argmin(A[:,i])
print(profmin,iprofmin)

j = iprofmin
print(A[j,:])

# inciso 3

i = 0 # índice de la columna de años...
[ListaAnios,CantidadPorAnio] = np.unique(A[:,i], return_counts = True)
print(ListaAnios)
print(CantidadPorAnio)

# en que año ocurrieron más sismos
CantidadMax = np.max(CantidadPorAnio)
iCantidadMax = np.argmax(CantidadPorAnio)

AnioConMas = ListaAnios[iCantidadMax]
print(CantidadMax,iCantidadMax,AnioConMas) # los índices arrancan en cero!!!

# inciso 4

# límites de Sudamérica
lonmin = -82.5 # grados
lonmax = -33.0 # grados
latmin = -56.5 # grados
latmax = +13.0 # grados
print(lonmin,lonmax,latmin,latmax)

# ¿qué filas satisfacen simultáneamente las CUATRO condiciones?
# acá usamos que True*True = True, pero True*False = False y False*False = False
# es decir, & es el AND lógico, pero aplicado elemento a elemento...
ilat = 6 # índice de la columna de latitudes...
ilon = 7 # índice de la columna de longitudes...
i = (lonmin <= A[:,ilon]) & (lonmax >= A[:,ilon]) & (latmin <= A[:,ilat]) & (latmax >= A[:,ilat])

# ¿cuantas filas cunplen las condiciones, es decir, son True?
# acá usamos que False equivale a 0, y True equivale a no cero...
print(np.count_nonzero(i))

# ¿que porcentaje del total son?
print(100*np.count_nonzero(i)/nsismos)

AenSA = A[i,:]

# inciso 5

# sismo de mayor magnitud en Sudamérica
i = 9 # índice de la columna de magnitudes...
magmax = np.max(AenSA[:,i])
imagmax = np.argmax(AenSA[:,i])

print(AenSA[imagmax,:])

# inciso 6

np.savetxt("sismosenSA.txt",AenSA)
print("¡Datos salvados!")

# %%
