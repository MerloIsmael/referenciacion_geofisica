import numpy as np
from numpy.typing import NDArray
from scipy import linalg

# %% Ejercicio 1
# definimos la matriz A (por filas)
A = np.array([[5, 5, 7, 8], [4, 7, 1, 1], [4, 4, 2, 1], [2, 4, 0, 3]])

# definimos la matrix b (por filas)
b = np.array([[2], [3], [7], [9]])

print(A)
print(b)

# %%
B = linalg.inv(A)
C = A.T
a = A @ b
c = C @ b
d = A.trace()

print(B)
print(C)
print(a)
print(c)
print(d)


# %% Ejercicio 2
a = np.array([[2], [3]])
b = np.array([[-1], [4]])

p = np.sum(a * b)

if p == 0:
    print("Son ortogonales")
else:
    print("No son ortogonales")


# %% Ejercicio 3


def sonortogonales(a: NDArray, b: NDArray) -> bool:
    p = np.sum(a * b)
    return np.abs(p) <= np.finfo(float).eps


def sonparalelos(a: NDArray, b: NDArray) -> bool:
    p = np.sum(a * b)
    costheta = p / (linalg.norm(a) * linalg.norm(b))
    return np.abs(np.abs(costheta) - 1) <= np.finfo(float).eps


def identificar_vectores(a: NDArray, b: NDArray) -> None:
    if sonortogonales(a, b):
        print("Son ortogonales")
        return

    if sonparalelos(a, b):
        print("Son paralelos/antiparalelos")
        return

    print("No son ni ortogonales ni paralelos/antiparalelos")


a = np.array([1, 2])
b = -3 * a
c = np.array([-2, 1])
d = np.array([1, 3])

identificar_vectores(a, b)
identificar_vectores(a, c)
identificar_vectores(b, c)
identificar_vectores(c, d)


# %% Ejercicio 4

# 1
text = np.loadtxt("./sismos.txt")
nsismos = np.shape(text)[0]

magmax = np.max(text[:, -1])
imagmax = np.argmax(text[:, -1])

print(magmax, imagmax)
print(text[imagmax, :])

# 2
# Mayor profundidad
profmax = np.max(text[:, 8])
iprofmax = np.argmax(text[:, 8])
print(profmax, iprofmax)
print(text[iprofmax, :])
# Menor profundidad
profmin = np.min(text[:, 8])
iprofmin = np.argmin(text[:, 8])
print(profmin, iprofmin)
print(text[iprofmin, :])

# 3

[ListaAnios, CantidadPorAnio] = np.unique(text[:, 0], return_counts=True)
print(ListaAnios)
print(CantidadPorAnio)
CantidadMax = np.max(CantidadPorAnio)
iCantidadMax = np.argmax(CantidadPorAnio)

AnioConMas = ListaAnios[iCantidadMax]
print(CantidadMax, iCantidadMax, AnioConMas)

# 4
lonmin = -82.5
lonmax = -33.0
latmin = -56.5
latmax = +13.0

ilat = 6
ilon = 7
i = (
    (lonmin <= text[:, ilon])
    & (lonmax >= text[:, ilon])
    & (latmin <= text[:, ilat])
    & (latmax >= text[:, ilat])
)
print(np.count_nonzero(i))
print(100 * np.count_nonzero(i) / nsismos)
AenSA = text[i, :]
print(AenSA)

# 5
i = 9
magmax = np.max(AenSA[:, i])
imagmax = np.argmax(AenSA[:, i])
print(AenSA[imagmax, :])

# 6
np.savetxt("sismosenSA.txt", AenSA)
