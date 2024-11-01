# Analisis Estadistico de Señales Biomédicas

> Realizado por: Karol Díaz y Andrea Ramírez

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

![WhatsApp Image 2024-10-31 at 08 24 36](https://github.com/user-attachments/assets/0d57cb6b-4d09-44f1-9088-6f589fbc54ad)

<em><strong>Figura 3.</strong> Grafico de señal ECG descargado.</em>

Dicho ECG presenta las siguientes caracterisricas de Histograma y función de probabilidad respectivamente.

![WhatsApp Image 2024-10-31 at 08 24 42](https://github.com/user-attachments/assets/7c0b83b3-c0b1-4a74-bb16-d144b51ee9d1)

<em><strong>Figura 4.</strong> Grafico de señal con información.</em>

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

![WhatsApp Image 2024-10-31 at 08 24 54](https://github.com/user-attachments/assets/531555ec-06b5-4dc5-8403-89d49134e0c4)

<em><strong>Figura 5.</strong> Visualización de señal contaminada con ruido Gaussiano.</em>

Para la función de probalilidad e histograma, grafiamente se observa un comportamiento de la siguiente forma.
![WhatsApp Image 2024-10-31 at 08 25 05](https://github.com/user-attachments/assets/af1d6aec-72ab-4467-99e5-2b8ac1693ea9)

Como se observa el compatamiento de la contaminación de ruido arroja un SNR positivo, pero tambien puede generar un SNR negativo.
![WhatsApp Image 2024-10-31 at 08 25 19](https://github.com/user-attachments/assets/277f9369-0fca-4ccb-b073-d7aceb8617f4)
![WhatsApp Image 2024-10-31 at 08 25 57](https://github.com/user-attachments/assets/5c42dcc4-309b-4158-8667-96a8c5d708f6)


Mientras que el <strong>ruido de impulso</strong> (ruido de saltos o disparo), consiste en picos esporádicos de alta amplitud. Este tipo de ruido es característico en señales que sufren interferencias esporádicas y de corta duración, que sobresalen significativamente de la señal original y pueden aparecer como picos altos o bajos en la señal.

![WhatsApp Image 2024-10-31 at 08 26 11](https://github.com/user-attachments/assets/6c4dcbe0-998a-46f4-9a8b-8a6110053bcc)

<em><strong>Figura 6.</strong> Visualización de señal contaminada con ruido impulso.</em>

![WhatsApp Image 2024-10-31 at 08 26 27](https://github.com/user-attachments/assets/1fc746ed-69e8-4cfc-ad86-6e18d40ff322)

El SNR negativo de la contaminación por ruido impulso presentara el siguiente comportamnieto.
![WhatsApp Image 2024-10-31 at 08 26 39](https://github.com/user-attachments/assets/797ca569-5e38-40ae-bef7-6c17d12764aa)
![WhatsApp Image 2024-10-31 at 08 26 49](https://github.com/user-attachments/assets/93ff97cd-be2a-473a-a58b-337b5df4a453)

Ahora bien, para añadir ruido de artefacto, se puede simular una señal sinusoidal de una frecuencia específica y superponerla a la señal original:

![image](https://github.com/user-attachments/assets/9cb77554-d510-414b-85c4-5515aa64ba24)

Siendo <em>A</em> la amplitud del artefacto y <em>f</em> la frecuencia correspondientemente.
Entonces, el ruido de artefacto se refiere a las interferencias externas que no forman parte de la señal fisiológica. Algunos ejemplos de artefactos incluyen el ruido muscular (EMG) en un EEG o la interferencia de red eléctrica (por ejemplo, 50/60 Hz). Son artefactos con frecuencia específica o patrones característicos.

![WhatsApp Image 2024-10-31 at 08 26 58](https://github.com/user-attachments/assets/3ece6174-65dc-4fdb-9841-0d2c985f61d7)

Figura 5.</strong> Visualización de señal contaminada con ruido tipo artefacto.</em>

![WhatsApp Image 2024-10-31 at 08 27 12](https://github.com/user-attachments/assets/b71eedad-02ae-4d79-844b-62ef9b89a875)

<em><strong>![WhatsApp Image 2024-10-31 at 08 27 24](https://github.com/user-attachments/assets/38afed79-96fe-4c25-8a00-0b023891092e)

## Resultados

- Ruido Gaussiano: Representa fluctuaciones aleatorias y continuas de baja amplitud, que suelen estar presentes de manera uniforme y afectan la claridad de toda la señal. La señal contaminada con este tipo de ruido puede requerir filtrado de banda estrecha para atenuar el ruido y mejorar la relación señal a ruido (SNR).

- Ruido de Impulso: Se manifiesta como picos de gran amplitud en puntos aleatorios, interrumpiendo bruscamente la señal y pudiendo provocar distorsiones significativas. Este tipo de ruido puede alterar de manera drástica los valores extremos y la continuidad de la señal, por lo que suele ser mitigado mediante técnicas de eliminación de artefactos o detectores de valores atípicos.

- Ruido de Artefacto: Este tipo de ruido, caracterizado por patrones periódicos como el ruido de la red eléctrica (50/60 Hz), introduce oscilaciones constantes que pueden solaparse con componentes fisiológicos importantes. La señal contaminada requiere filtrado específico en la frecuencia del artefacto para evitar su interferencia en el análisis.

Información adquirida a partir de la señal descargada y cada uno de los ruidos aplicados
![WhatsApp Image 2024-10-31 at 08 28 23](https://github.com/user-attachments/assets/f9fdb801-8b65-487e-9e6c-075fb148eb55)
![WhatsApp Image 2024-10-31 at 08 28 50](https://github.com/user-attachments/assets/97e7ac7d-74cc-47ab-af81-31ed1f0e9d7d)


## Conclusiones

La contaminación de una señal biomédica con diferentes tipos de ruido —gaussiano, de impulso y de artefacto— permite simular y comprender los retos del procesamiento de señales fisiológicas en condiciones reales. La contaminación con estos distintos tipos de ruido destaca la necesidad de técnicas específicas de procesamiento y filtrado para cada caso. Con herramientas como filtros de paso bajo, eliminación de artefactos y análisis de valores atípicos, es posible restaurar en gran medida la integridad de la señal y facilitar un análisis biomédico preciso. La capacidad de distinguir y filtrar cada tipo de ruido mejora la calidad del monitoreo de señales y la confiabilidad de las aplicaciones médicas y de diagnóstico basadas en datos fisiológicos.
