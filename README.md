# Analisis Estadistico de Señales Biomédicas

Las señales biomédicas o fisiológicas son datos que se generan en el cuerpo humano como resultado de funciones y procesos biológicos. Estas señales reflejan la actividad y el estado de diversos sistemas y órganos en el cuerpo, como el corazón, los pulmones, el cerebro, los músculos y la piel. Su análisis es fundamental en la medicina y la ingeniería biomédica, ya que permiten monitorizar y diagnosticar condiciones de salud, estudiar el comportamiento fisiológico y desarrollar dispositivos médicos avanzados.

<p>
  Las señales biomédicas más comunes incluyen:
</p>

1. **Electrocardiograma (ECG)**: Registra la actividad eléctrica del corazón.
2. **Electroencefalograma (EEG)**: Mide la actividad eléctrica del cerebro.
3. **Electromiograma (EMG)**: Detecta la actividad eléctrica en los músculos.
4. **Impedancia de la piel/conductancia (GSR)**: Evalúa la respuesta galvánica de la piel.
5. **Señales de respiración**: Involucran tanto el flujo de aire como la oxigenación.


![image](https://github.com/user-attachments/assets/bccb7b3a-7f13-41f0-a7e1-9b8efdb0a9be) 

<em><strong>Figura 1.</strong> Visualización de señales fisiológicas.</em>

Estas señales, una vez capturadas por medio de sensores especializados, se procesan y analizan mediante técnicas de procesamiento de señales y modelos matemáticos. El estudio de estas señales es crucial para la creación de sistemas de diagnóstico, dispositivos de monitoreo continuo y herramientas de intervención que mejoran la calidad de vida y la precisión de los tratamientos médicos.

A partir de dicho análisis, se pueden extraer diversas variables estadísticas que brindan información detallada sobre los patrones y características de estas señales. Relevantes para la interpretación de datos fisiológicos, ya que ayudan a detectar anomalías y a establecer umbrales y parámetros para el diagnóstico clínico. 

Las variables estadísticas más comunes incluyen:

1. **Media**
2. **Desviación estándar (SD)**
3. **Varianza**
4. **Función de probabilidad**
5. **Mediana**
6. **Máximo y mínimo**
7. **Coeficiente de variación (CV)**
8. **Energía de la señal**
9. **Histogramas**

Estas variables estadísticas permite profundizar en la interpretación de las señales biomédicas, facilitando la comparación entre diferentes estados fisiológicos, poblaciones o condiciones de salud, siendo fundamental en el diagnóstico, monitoreo y en la toma de decisiones clínicas.

## Desarrollo de la práctica
Para el desarrollo de la práctica se extrae de la base de datos de <Strong>PHYSIONET</Strong> una señal fisiológica que se importará y codificará en <em>Python</em>, a la cual, posteriormente se calculara sus respectivos estadísticos y se contaminara la señal con ciertos tipos de ruido.

Sin embargo, antes de comenzar con el procedimento es necesario tener en cuenta el concepto de SNR (Relación Señal a Ruido), ya que es una medida que cuantifica la proporción entre la potencia de una señal significativa y la potencia del ruido presente en esa misma señal. Es un indicador clave en el análisis de señales, ya que determina la claridad o calidad de una señal en presencia de interferencias o ruido indeseado.

<p>Matemáticamente el SNR se calcula:</p>

![image](https://github.com/user-attachments/assets/44f17c85-7b11-4d56-85cb-87b500681f38)

Donde:
- La potencia de la señal representa la magnitud de la señal que contiene la información de interés.
- La potencia del ruido se refiere a la energía de los componentes no deseados que interfieren en la señal.

En el contexto de las señales biomédicas, el SNR es de suma importancia, ya que estas señales suelen ser débiles y fácilmente afectadas por el ruido, como el generado por el movimiento del cuerpo, interferencias eléctricas y artefactos ambientales. Un buen SNR es esencial para obtener mediciones precisas y fiables en aplicaciones como el electrocardiograma (ECG), electroencefalograma (EEG) y electromiograma (EMG), entre otras. Técnicas de procesamiento de señales, como filtrado y separación de fuentes, son empleadas para mejorar el SNR y permitir una interpretación clínica más confiable de los datos biomédicos.

![image](https://github.com/user-attachments/assets/e31d1068-c2e2-4f6a-83af-1def8c198560)

La ecuación posterior corresponde al comportamiento matemático de la contaminación de una señal con ruido Gaussiano e Impulso.

Done el <strong>ruido Gaussiano</strong> (ruido blanco), se caracteriza por su distribución normal de amplitudes y por ser uno de los tipos de ruido más comunes en sistemas de señal. Se puede agregar a la señal original como un vector de ruido con media cero y desviación estándar configurable, de manera que imite fluctuaciones pequeñas y continuas alrededor de la señal. 
Mientras que el <strong>ruido de impulso</strong> (ruido de saltos o disparo), consiste en picos esporádicos de alta amplitud. Este tipo de ruido es característico en señales que sufren interferencias esporádicas y de corta duración, que sobresalen significativamente de la señal original y pueden aparecer como picos altos o bajos en la señal.
Ahora bien, para añadir ruido de artefacto, se puede simular una señal sinusoidal de una frecuencia específica y superponerla a la señal original:

![image](https://github.com/user-attachments/assets/9cb77554-d510-414b-85c4-5515aa64ba24)

Siendo <em>A</em> la amplitud del artefacto y <em>f</em> la frecuencia correspondientemente.
Entonces, el ruido de artefacto se refiere a las interferencias externas que no forman parte de la señal fisiológica. Algunos ejemplos de artefactos incluyen el ruido muscular (EMG) en un EEG o la interferencia de red eléctrica (por ejemplo, 50/60 Hz). Son artefactos con frecuencia específica o patrones característicos.

![image](https://github.com/user-attachments/assets/8f3a4f4e-b1b0-4dbf-b02a-e02916f488a6)

<em><strong>Figura 2.</strong> Grafico de señal contaminada con ruido.</em>


## Resultados

<em><strong>Figura 3.</strong> Visualización de señal contaminada con ruido Gaussiano.</em>

<em><strong>Figura 4.</strong> Visualización de señal contaminada con ruido impulso.</em>

<em><strong>Figura 5.</strong> Visualización de señal contaminada con ruido tipo artefacto.</em>

## Conclusiones
