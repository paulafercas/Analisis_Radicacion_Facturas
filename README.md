# Proyecto Análisis De Datos Integrador 
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
## Descripción

Este proyecto consiste en aplicar los conocimientos adquiridos durante el bootcamp de Talento Tech centrado en el análisis de datos aplicado en la recepción y radicación de facturas de proveedores.

## Justificación

Las empresas día a día reciben grandes volúmenes de facturas provenientes de diversos proveedores, esto limita la toma de decisiones oportunas basadas en la información de este volumen masivo de datos. En consecuencia, estos datos se tornan subutilizados y olvidados en el tiempo.

En este contexto, surge la necesidad de aplicar técnicas de análisis de datos que permitan transformar la información en conocimiento útil. Para ello, se emplean herramientas como MySQL para la gestión y consulta estructurada de los datos, Python para su procesamiento y análisis, y Streamlit para la visualización e interpretación interactiva de los resultados.

De esta manera, el proyecto busca facilitar la comprensión del comportamiento de la facturación en la empresa, aportando insumos clave para la optimización de recursos y la toma de decisiones estratégicas.

## Objetivo General

Analizar el comportamiento de las facturas en una empresa en los últimos 4 años

## Objetivos Específicos

* Depurar y estandarizar la información contenida en las tablas de facturación, proveedores y pedidos, corrigiendo inconsistencias de codificación y formato en variables como categoría y producto, con el fin de garantizar la calidad de los datos para su posterior análisis.

* Describir el comportamiento de las facturas de la empresa durante los últimos 3 años, mediante consultas de selección, agrupación y agregación sobre variables como categoría, valor total, cantidad de productos y proveedores, para identificar tendencias, frecuencias y distribución de los registros.

* Comparar los valores de facturación y precios registrados con sus respectivos promedios generales, utilizando subconsultas y funciones en SQL, con el propósito de detectar facturas y productos que presenten comportamientos superiores al promedio dentro del periodo analizado.

![Diagrama entidad-relación que muestra el proceso de recepción de facturación y pago a proveedores. En la parte superior, la entidad Proveedores se conecta a los atributos NIT_Proveedor, Nombre_proveedor, Ubicación y Categoría. Desde Proveedores fluye hacia el proceso Radicar, que se conecta a la entidad Facturación. La entidad Facturación contiene los atributos ID_Registro, NIT_Proveedor, Número_pedido, Fecha_ingresa en el lado izquierdo, y Categoría, Sociedad, Estado_factura, Tipo_factura en el lado derecho. Desde Facturación se continúa al proceso Detallar, que se conecta a la entidad Pedidos. La entidad Pedidos presenta los atributos Número_pedido, Producto, Cantidad y Valor. El diagrama utiliza símbolos de entidades en óvalos azules, procesos en rectángulos azules y conectores de líneas. La estructura general muestra el flujo de datos desde proveedores hasta los detalles de pedidos.](Data/Diagrama_MER.jpg)

## Características del Dashboard

### 📊 Módulos Principales

1. **Inicio**: Panel de bienvenida con métricas generales y escala de salud de la empresa
2. **Productos**: Análisis de productos más/menos vendidos con valor facturado
3. **Proveedores**: Evaluación de proveedores principales y su impacto en el negocio
4. **Facturas Pendientes**: Seguimiento de cartera, detectando riesgos de incobrables
5. **Facturas**: Análisis temporal de facturación agregada por mes y año
6. **🤖 Chatbot Financiero**: Chatbot inteligente con análisis estratégicos

### 🤖 Chabot Financiero - Nuevo

El Chatbot es un asistente IA que proporciona análisis inteligentes sobre 7 aspectos clave del negocio:

✅ **7 Análisis Estratégicos:**
1. **Productos Más Vendidos** - Concentración y diversificación de ventas
2. **Productos Menos Vendidos** - Identificación de oportunidades o riesgos
3. **Proveedores Principales** - Análisis de dependencia y alianzas estratégicas
4. **Facturas Pendientes** - Salud de cartera y riesgos crediticios
5. **Categorías Principales** - Distribución de ingresos y diversificación
6. **Promedios de Facturación** - Tendencias, ticket promedio, velocidad operativa
7. **Salud Integral** - Estado general y recomendaciones prioritarias

🎯 **Cada respuesta incluye:**
- Datos específicos y comparativas
- Análisis de impacto empresarial
- 5 Recomendaciones estratégicas focalizadas en:
  - Salud financiera de la empresa
  - Fortalecimiento de relaciones comerciales
  - Optimización de productos y categorías

📝 **Cómo usar:**
- Escribe preguntas naturales en el chatbot
- O selecciona una de las preguntas sugeridas con un clic
- El copiloto analiza y proporciona insights accionables

*Más detalles en [COPILOTO_GUIA.md](COPILOTO_GUIA.md)*

## Instalación y Ejecución

### Requisitos
- Python 3.8+
- pip (gestor de paquetes)

### Instalación de dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar la aplicación
```bash
streamlit run appStreamlit.py
```

La aplicación se abrirá en `http://localhost:8501`
