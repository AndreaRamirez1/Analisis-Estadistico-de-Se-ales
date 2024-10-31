# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# Importación de librerías necesarias
import wfdb  # Librería para cargar y manipular registros de señales fisiológicas
import numpy as np  # Librería para operaciones matemáticas y manejo de matrices
import pandas as pd  # Librería para manipulación y análisis de datos
import matplotlib.pyplot as plt  # Librería para graficar datos
from scipy.stats import norm  # Librería para ajustar distribuciones normales y funciones de probabilidad

# Cargar la señal desde archivos locales (.dat y .hea)
senal = wfdb.rdrecord('a02')  # Se carga la señal fisiológica

# Verificación del número de señales en el archivo
print("Número de señales:", senal.n_sig)  # Imprime cuántas señales hay en el archivo

# Visualizar los valores de la señal
print("Valores de la señal:\n", senal.p_signal)  # Muestra los valores de la señal cargada

# Visualizar la longitud de la señal (número de muestras)
print("Longitud de la señal:", senal.sig_len)  # Imprime la cantidad de muestras de la señal

# Almacenar los valores de la señal en una variable para su manipulación posterior
valores = senal.p_signal  # Se almacena la señal en la variable 'valores'

# Graficar la señal para visualización
plt.figure(figsize=(12, 4))  # Define el tamaño de la figura
plt.plot(valores)  # Grafica los valores de la señal
plt.title('Señal')  # Título del gráfico
plt.xlabel('Muestras')  # Etiqueta para el eje X
plt.ylabel('Amplitud')  # Etiqueta para el eje Y
plt.show()  # Muestra el gráfico

# Calcular la media, desviación estándar y coeficiente de variación para cada canal de la señal
mean_values = np.mean(valores, axis=0)  # Calcula la media de la señal
std_devs = np.std(valores, axis=0)  # Calcula la desviación estándar de la señal
coef_vars = std_devs / mean_values  # Calcula el coeficiente de variación

# Imprimir los resultados calculados para cada canal de la señal
for i in range(senal.n_sig):
    print(f"Señal {i+1}:")
    print(f"  Media: {mean_values[i]}")  # Muestra la media
    print(f"  Desviación estándar: {std_devs[i]}")  # Muestra la desviación estándar
    print(f"  Coeficiente de variación: {coef_vars[i]}")  # Muestra el coeficiente de variación

# Exportar los valores de la señal a un archivo CSV
df = pd.DataFrame(valores, columns=[f'Señal {i+1}' for i in range(valores.shape[1])])  # Crea un DataFrame con los valores de la señal
df.to_csv('senal_exportada.csv', index=False)  # Guarda los datos en un archivo CSV
print("Los datos de la señal se han exportado a 'senal_exportada.csv'.")  # Notifica que los datos se han exportado

# Graficar un histograma de la señal y ajustar una función de probabilidad normal
plt.figure(figsize=(12, 4))  # Define el tamaño de la figura
plt.hist(valores[:, 0], bins=50, density=True, alpha=0.6, color='g')  # Grafica un histograma de la señal

# Ajustar una distribución normal a los datos del primer canal de la señal
mu, std = norm.fit(valores[:, 0])  # Ajusta la distribución normal y obtiene la media (mu) y desviación estándar (std)
xmin, xmax = plt.xlim()  # Obtiene los límites del eje X del gráfico
x = np.linspace(xmin, xmax, 100)  # Genera un conjunto de puntos para la distribución normal
p = norm.pdf(x, mu, std)  # Calcula la función de densidad de probabilidad para la distribución ajustada
plt.plot(x, p, 'k', linewidth=2)  # Grafica la función de densidad de probabilidad
plt.title('Histograma y función de probabilidad')  # Título del gráfico
plt.xlabel('Amplitud')  # Etiqueta para el eje X
plt.ylabel('Densidad de probabilidad')  # Etiqueta para el eje Y
plt.show()  # Muestra el gráfico

# Calcular estadísticos descriptivos usando funciones predefinidas de Python
mean_signal_builtin = np.mean(valores)  # Calcula la media usando una función predefinida
std_signal_builtin = np.std(valores)  # Calcula la desviación estándar usando una función predefinida
cv_signal_builtin = std_signal_builtin / mean_signal_builtin  # Calcula el coeficiente de variación

# Imprimir los resultados usando las funciones predefinidas
print(f'Media de la señal (predefinido): {mean_signal_builtin}')
print(f'Desviación estándar (predefinido): {std_signal_builtin}')
print(f'Coeficiente de variación (predefinido): {cv_signal_builtin}')

# Función para añadir ruido gaussiano a la señal
def add_gaussian_noise(signal, snr):
    noise = np.random.normal(0, np.std(signal) / snr, signal.shape)  # Genera ruido gaussiano
    noise_scaled = noise * (6 / np.max(np.abs(noise)))  # Escala el ruido para que su máximo sea 6 veces el valor absoluto máximo del ruido
    return signal + noise_scaled  # Retorna la señal con el ruido añadido

# Función para añadir ruido de impulsos a la señal
def add_impulse_noise(signal, snr):
    noise = np.zeros(signal.shape)  # Inicializa un array de ceros del mismo tamaño que la señal
    num_impulses = int(len(signal) / snr)  # Calcula el número de impulsos a añadir según el SNR
    impulse_positions = np.random.choice(len(signal), num_impulses)  # Selecciona posiciones aleatorias para los impulsos
    noise[impulse_positions] = 6 * np.max(signal)  # Añade impulsos en las posiciones seleccionadas
    return signal + noise  # Retorna la señal con el ruido de impulsos añadido

# Función para añadir ruido de artefactos a la señal
def add_artifact_noise(signal, snr):
    noise = np.sin(np.linspace(0, 2 * np.pi * 10, len(signal))) * np.std(signal) / snr  # Genera ruido de artefactos basado en una señal sinusoidal
    noise_scaled = noise * (6 / np.max(np.abs(noise)))  # Escala el ruido para que su máximo sea 6 veces el valor absoluto máximo del ruido
    return signal + noise_scaled  # Retorna la señal con el ruido de artefactos añadido

# Función para calcular la relación señal-ruido (SNR)
def calculate_snr(signal, noise_signal):
    signal_power = np.mean(signal ** 2)  # Calcula la potencia de la señal original
    noise_power = np.mean((signal - noise_signal) ** 2)  # Calcula la potencia del ruido
    snr = 10 * np.log10(signal_power / noise_power)  # Calcula el SNR en decibelios
    return snr  # Retorna el SNR, puede ser positivo o negativo

# Añadir ruido a la señal y calcular el SNR para cada tipo de ruido
gaussian_noise_signal = add_gaussian_noise(valores[:, 0], 5)  # Añadir ruido gaussiano
impulse_noise_signal = add_impulse_noise(valores[:, 0], 5)  # Añadir ruido de impulsos
artifact_noise_signal = add_artifact_noise(valores[:, 0], 5)  # Añadir ruido de artefactos

# Calcular y mostrar el SNR para cada señal con ruido
snr_gaussian = calculate_snr(valores[:, 0], gaussian_noise_signal)  # SNR para ruido gaussiano
snr_impulse = calculate_snr(valores[:, 0], impulse_noise_signal)  # SNR para ruido de impulsos
snr_artifact = calculate_snr(valores[:, 0], artifact_noise_signal)  # SNR para ruido de artefactos

print(f'SNR con ruido gaussiano: {snr_gaussian} dB')  # Imprimir el SNR para ruido gaussiano
print(f'SNR con ruido impulso: {snr_impulse} dB')  # Imprimir el SNR para ruido de impulsos
print(f'SNR con ruido artefacto: {snr_artifact} dB')  # Imprimir el SNR para ruido de artefactos

# Graficar las señales con ruido añadido para visualización
plt.figure(figsize=(12, 4))
plt.plot(gaussian_noise_signal)
plt.title('Señal ECG con ruido gaussiano')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()  # Mostrar la gráfica de la señal con ruido gaussiano

plt.figure(figsize=(12, 4))
plt.plot(impulse_noise_signal)
plt.title('Señal ECG con ruido de impulsos')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()  # Mostrar la gráfica de la señal con ruido de impulsos

plt.figure(figsize=(12, 4))
plt.plot(artifact_noise_signal)
plt.title('Señal ECG con ruido de artefactos')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()  # Mostrar la gráfica de la señal con ruido de artefactos
