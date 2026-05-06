import matplotlib.pyplot as plt
import numpy as np

sismos = np.loadtxt("sismos.txt")

# %% jercicio 1

nsismos = np.shape(sismos)[0]

mayor_magnitud = [95.98, 3.29]
mayor_profundidad = [-179.31, -19.41]

# graficamos los epicentros, con la longitud en las absisas
plt.subplot(211)
plt.plot(
    sismos[:, 7], sismos[:, 6], marker="*", linestyle="", color="red", label="epicentro"
)
plt.plot(mayor_magnitud[0], mayor_magnitud[1], marker="o", color="black")
plt.plot(mayor_profundidad[0], mayor_profundidad[1], marker="o", color="blue")

# profundidad en funcion de la longitud
plt.subplot(212)
plt.scatter(sismos[:, 7], sismos[:, 8], label="profundidad")
plt.legend()


# %% Ejercicio 2
datos = np.loadtxt("./datos.txt")

tiempo = datos[:, 0]
amplitud = datos[:, 1]

nd = np.size(tiempo)
print(nd)

plt.figure()
plt.plot(tiempo, amplitud, label="Observaciones en datos.txt")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [mm]")
plt.legend()
plt.savefig("ejercicio.png")


# %% Ejercicio 3
plt.figure()
plt.scatter(
    tiempo, amplitud, label="Observaciones en datos.txt", marker="o", color="red"
)
plt.ylabel("Amplitud [mm]")
plt.xlabel("Tiempo [s]")
plt.legend()
plt.axis([8, 24, -25, 25])
plt.title("Superposicion de ondas")
plt.savefig("ejercicio2.pdf")


# Ejercicio 4

# %% carga de datos

# series temporales estimadas con GNSS
datosGNSS = np.loadtxt("./igmgps2008.txt")

doyGNSS = datosGNSS[:, 0]  # [doy]
ztdGNSS = datosGNSS[:, 1]  # [mm]
iwvGNSS = datosGNSS[:, 2]  # [kg/m^2]

# serie temporal estimada con RS
datosRS = np.loadtxt("./igmrs2008.txt")

doyRS = datosRS[:, 0]  # [doy]
iwvRS = datosRS[:, 1]  # [kg/m^2]

# longitud de las series temporales
nGNSS = np.size(doyGNSS)
nRS = np.size(doyRS)


# %% inciso 1
doyMAX = np.max([np.max(doyGNSS), np.max(doyRS)])
doyMIN = np.min([np.min(doyGNSS), np.min(doyRS)])

plt.subplot(3, 1, 1)
plt.plot(doyGNSS, ztdGNSS, marker="o", color="blue")
plt.title("TP7 - E6")
plt.ylabel("ZTD [mm]")
plt.axis([doyMIN, doyMAX, None, None])

# %% inciso 2

[doyCOMUN, i, j] = np.intersect1d(doyGNSS, doyRS, return_indices=True)
n = np.size(i)  # 244 epocas comunes

iwvR = iwvGNSS[i] - iwvRS[j]

plt.subplot(3, 1, 1)
plt.plot(doyGNSS, ztdGNSS, marker="o", color="blue")
plt.title("TP7 - E6")
plt.ylabel("ZTD [mm]")
plt.axis([doyMIN, doyMAX, None, None])

plt.subplot(3, 1, 2)
plt.plot(doyCOMUN, iwvR, marker="o", color="red")
plt.axis([doyMIN, doyMAX, None, None])
plt.xlabel("t [doy]")
plt.ylabel("dif. IWV [kg/m^2]")


# %% Inciso 3

# agregamos el último gráfico
plt.subplot(3, 1, 1)
plt.plot(doyGNSS, ztdGNSS, marker="o", color="blue")
plt.title("TP7 - E6")
plt.ylabel("ZTD [mm]")
plt.axis([doyMIN, doyMAX, None, None])

# haremos tres gráficos, uno abajo del otro
plt.subplot(3, 1, 2)
plt.plot(doyCOMUN, iwvR, marker="o", color="red")
plt.axis([doyMIN, doyMAX, None, None])
plt.xlabel("t [doy]")
plt.ylabel("dif. IWV [kg/m^2]")

plt.subplot(3, 1, 3)
plt.hist(iwvR, color="green")
plt.xlabel("IWV (GNSS) - IWV (RS) [kg/m^2]")
