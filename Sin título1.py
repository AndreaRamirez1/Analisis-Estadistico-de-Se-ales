# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:39:27 2024

@author: Karol Diaz
"""

# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
# Cargar librerías
import wfdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar la información (señal)
# Para cargar la información se debe de tener ambos archivos: .dat y .hea
# Guardar los datos y código en la misma carpeta
senal = wfdb.rdrecord('a02')  # cargar la señal

# Verificación de la calidad de la señal
print("Número de señales:", senal.n_sig)

# Visualizar valores de la señal
print("Valores de la señal:\n", senal.p_signal)

# Visualizar longitud de la señal
print("Longitud de la señal:", senal.sig_len)

# Almacenar los valores en una variable para poderlos manipular
valores = senal.p_signal

# Graficar la señal
plt.plot(valores)
plt.title('Señal')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()

# Calcular la media, desviación estándar y coeficiente de variación para cada señal
mean_values = np.mean(valores, axis=0) #Es para calcular la media de la señal con los datos que se guardaron anteriormente 
std_devs = np.std(valores, axis=0)#Es para calcular la desviacion estandar de la señal 
coef_vars = std_devs / mean_values# dividimos la desviacion y la media para asi obtener el coeficiente de variación 

# Imprimir los resultados
for i in range(senal.n_sig):
    print(f"Señal {i+1}:")
    print(f"  Media: {mean_values[i]}")
    print(f"  Desviación estándar: {std_devs[i]}")
    print(f"  Coeficiente de variación: {coef_vars[i]}")

# Exportar los datos de la señal a un archivo CSV con un nombre diferente
df = pd.DataFrame(valores, columns=[f'Señal {i+1}' for i in range(valores.shape[1])])
df.to_csv('senal_exportada.csv', index=False)

print("Los datos de la señal se han exportado a 'senal_exportada.csv'.")



