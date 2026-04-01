# 🚀 Guía Rápida - Copiloto Financiero

## Iniciando la Aplicación

### 1. Instalar dependencias (primera vez):
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación:
```bash
streamlit run appStreamlit.py
```

### 3. Seleccionar "Copiloto" en el menú lateral

---

## Ejemplos de Uso Inmediato

### 📌 Escenario 1: "Quiero saber nuestros productos principales"
1. Ve a **Copiloto**
2. Haz clic en el botón **🏆 Productos Top**
3. Verás:
   - Producto con mayor facturación
   - Cantidad vendida
   - Concentración en el negocio (%)
   - Análisis de riesgos
   - 5 recomendaciones estratégicas

### 📌 Escenario 2: "Necesito saber cuánto dinero nos deben"
1. Ve a **Copiloto**
2. Haz clic en **⏳ Cartera Pendiente**
3. Obtendrás:
   - Total pendiente de cobro
   - Número de facturas sin pagar
   - Proveedores que más deben
   - Responsables asignados
   - Salud financiera (🟢/🟡/🔴)
   - Plan de cobranza

### 📌 Escenario 3: "¿Cómo está nuestra empresa financieramente?"
1. Ve a **Copiloto**
2. Haz clic en **📊 Salud General**
3. Verás KPIs consolidados y prioridades estratégicas

---

## Escribir Preguntas Personalizadas

### ✏️ Ejemplos de preguntas que entiende:

**Sobre Productos:**
- "¿Cuáles son nuestros productos más vendidos?"
- "¿Productos con menor facturación?"
- "¿Qué productos vende más la empresa?"

**Sobre Proveedores:**
- "¿Quiénes son los proveedores principales?"
- "¿Principales proveedores por valor?"
- "¿De cuántos proveedores dependo?"

**Sobre Cartera Pendiente:**
- "¿Cómo está nuestra cartera pendiente?"
- "¿Cuánto dinero nos deben?"
- "¿Facturas sin pagar?"
- "¿Estado de pagos pendientes?"

**Sobre Categorías:**
- "¿Cómo se distribuye nuestro negocio por categorías?"
- "¿Categorías principales?"
- "¿Qué categoría genera más ingresos?"

**Sobre Promedios:**
- "¿Cuál es el promedio de facturación?"
- "¿Cuántas facturas hacemos por mes?"
- "¿Tendencia de crecimiento?"

---

## Estructura de las Respuestas

Cada respuesta del copiloto te dará:

### 1️⃣ **Datos Clave**
Números específicos, valores totales, rankings

Ejemplo:
```
El producto líder es SERVICIO X con:
• Cantidad vendida: 150,000 unidades
• Valor facturado: $45,300,000
• Concentración: 23.5% del valor total
```

### 2️⃣ **Análisis Estratégico**
Interpretación de los datos y cómo afecta a tu empresa

Ejemplo:
```
La concentración del 23.5% en un solo producto sugiere que 
tu empresa depende significativamente del mercado de SERVICIO X.
Esto puede ser positivo si el mercado es estable, pero riesgoso 
si hay disrupciones en la demanda.
```

### 3️⃣ **5 Recomendaciones Accionables**
Acciones concretas que puedes implementar

Ejemplo:
```
💡 Recomendaciones:
1. Diversificación: Desarrolla 3 nuevos productos en H2 2024
2. Marketing: Invierte en promoción de SERVICIO Y (sub-performer)
3. Partnerships: Negocia descuentos de volumen con PROVEEDOR A
4. Automatización: Implementa sistemas para reducir cobranza manual
5. Proyección: Haz cash flow forecast considerando cartera pendiente
```

---

## Historial de Conversaciones

Todas tus preguntas y respuestas del copiloto se guardan en la sesión.
- Puedes revisar análisis anteriores
- Las conversaciones persisten mientras mantengas abierta la app
- Si recargas, inicia una nueva sesión

---

## Tips para Sacar el Máximo Provecho

### ✅ Haz Preguntas Específicas
**Bueno:** ¿Cuáles son los productos top 3 por valor?
**Mejor:** ¿Cuáles son mis 5 productos principales, cuánto facturan y qué porcentaje del total representan?

### ✅ Combina Análisis
1. Primero pregunta por **Productos Top**
2. Luego por **Proveedores**
3. Finalmente por **Cartera Pendiente**
... esto te da visión 360° del negocio

### ✅ Revisa la Escala de Salud
En la parte superior de cada página verás un indicador:
- 🟢 **Saludable**: Cartera <30%, todo en control
- 🟡 **Moderado**: Cartera 30-70%, requiere acción
- 🔴 **Alto Riesgo**: Cartera >70%, crítico

### ✅ Frecuencia de Uso
- **Diaria**: Revisa cartera pendiente y facturas
- **Semanal**: Analiza proveedores y productos principales
- **Mensual**: Evalúa salud general y tendencias

---

## Solucionar Problemas

### ❌ El copiloto no responde
→ Recarga la página con F5

### ❌ No entiendo una respuesta
→ Haz clic en **📊 Salud General** para visión integral

### ❌ Quiero más detalles
→ Cada sección del Dashboard (Productos, Proveedores, Facturas)
  tiene gráficos y tablas interactivas con más información

---

## Archivos de Referencia

- **COPILOTO_GUIA.md** - Documentación completa del copiloto
- **README.md** - Información general del proyecto
- **appStreamlit.py** - Código fuente de la aplicación

---

**¡Ahora estás listo para usar el Copiloto Financiero! 🚀**

*Pro tip: El copiloto mejora con el uso. Experimenta haciendo diferentes preguntas.*
