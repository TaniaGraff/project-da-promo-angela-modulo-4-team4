# Gestión de Reservas

Proyecto de análisis y optimización de las cancelaciones de las reservas de una cadena hotelera.

*Equipo Desarrollo* Tania Graff, Sandra Moreno, Raquel Pedraza, Mónica Valencia
*Herramienta visualización:* Power BI Desktop

La cadena hotelera ha notado un aumento en el número de cancelaciones de sus reservas en los últimos meses y nos ha encargado realizar un análisis preliminar para comprender las causas y patrones que se esconden tras esas cancelaciones, con tal de que la gerencia del hotel pueda identificar áreas de mejora y tomar decisiones informadas para reducir la tasa de cancelación.

![imagen_portada_modulo](portada.png)

## **FASE 1: Exploración, Limpieza y Transformación el Conjunto de Datos**
Se ha automatizado la primera fase de exploración, transformación y limpieza de datos.

### **Ejecución de la Limpieza y Transformación de Datos**
El proceso de limpieza y transformación de datos está automatizado mediante un script en Python. Sigue estos pasos para ejecutar el script:

**1. Clona el Repositorio:**

```python
git clone https://github.com/TaniaGraff/project-da-promo-angela-modulo4-team4
```
**2. Ejecuta el Script de Limpieza y Transformación:**
Navega a la carpeta `ETL_Equipo#1` y ejecuta el script `main.py`:

```python
python scripts/main.py
```

Este script procesará los datos descargados y generará archivos limpios y transformados en la carpeta `ETL_Equipo#1`.

**3. Verifica los Archivos Procesados:**
Revisa la carpeta para asegurarte de que los archivos procesados se han generado correctamente. Estos archivos estarán listos para ser utilizados en Power BI para la creación del dashboard.

## **FASE 2: Identificación de Objetivos**

### **Objetivos**

**1. Identificación de las Cancelaciones:** Entender qué patrones se esconden detrás de las cancelaciones, planteándose las siguientes preguntas clave:

**2. Preguntas Clave** 
- ¿Cuántos hoteles tiene la cadena? 
- ¿Tienen el mismo número de cancelaciones?
- ¿Ha cambiado la tasa de cancelación con el tiempo?
- ¿Se cancelan más las reservas de verano que de invierno?
- ¿Se cancelan más las reservas de entre semana que las de los fines de semana?
- Los clientes que cancelan, ¿presentan algún tipo de característica demográfica?
- Las reservas que se hacen con mayor anticipación, ¿tienen mucho riesgo de cancelarse?
- Las reservas que incluyen hijos, ¿tienen menor riesgo de cancelación?
- Los usuarios que realizaron algún cambio en su reserva, ¿tienen menor riesgo de cancelación?
- Cuándo el usuario ha realizado una solicitud especial, ¿el riesgo de cancelación es menor?
- Las reservas que tienen un tarifa baja, ¿tienen un riesgo menor de cancelación?.


## **FASE 3: Visualización Resultados**

**Visualización de Datos:** Proporcionar visualizaciones claras y comprensibles para facilitar la toma de decisiones informadas con gestionar las cancelaciones.

Para ver el dashboard de las cancelaciones del hotel, ejecutar en Power BI el archivo **cancelaciones_hoteles.pbix**



