# 🤖 Guía del Copiloto Financiero v2.1 - COMPRAS Y GASTOS

## ⚠️ ACLARACIÓN IMPORTANTE

**Este copiloto analiza ÓRDENES DE COMPRA Y GASTOS, no ventas.**

- Las "facturas" son órdenes de compra que la empresa realiza A sus proveedores
- El "valor facturado" es lo que la empresa GASTA/INVIERTE
- Los "productos" son los artículos que la empresa COMPRA (no vende)
- El enfoque es en **gestión de compras, control de gastos y relaciones con proveedores**

---

## Descripción

El **Copiloto Financiero** es un chatbot inteligente que analiza **7 aspectos clave de la gestión de compras y gastos** de tu empresa.

## 7 Análisis Disponibles

### 1. **🛒 Productos Más Comprados (Mayor Inversión)**
- Identifica productos donde más dinero se invierte
- Muestra concentración de gasto en cada producto
- Analiza riesgos de dependencia de productos específicos
- Recomienda negociación y consolidación de compras

**Preguntas que activan este análisis:**
- "¿Cuáles son nuestros productos más comprados?"
- "¿En qué productos gastamos más dinero?"
- "¿Productos con mayor inversión?"

---

### 2. **📦 Productos Menos Comprados (Menor Inversión)**
- Identifica productos con compras ocasionales o bajas
- Analiza si son críticos para la operación
- Sugiere si consolidar, eliminar o automatizar órdenes
- Recomienda acciones para optimizar

**Preguntas que activan este análisis:**
- "¿Cuáles son nuestros productos menos comprados?"
- "¿Productos con menor gasto?"
- "¿Qué compramos ocasionalmente?"

---

### 3. **🏭 Proveedores Principales (Mayor Dependencia)**
- Identifica de quién compramos más (mayor inversión)
- Muestra número de órdenes y valor total
- Analiza riesgo de dependencia y oportunidades de negociación
- Recomienda diversificación y alianzas

**Preguntas que activan este análisis:**
- "¿Quiénes son nuestros proveedores principales?"
- "¿De dónde compramos más dinero?"
- "¿Proveedores con mayor volumen?"

---

### 4. **⏳ Pagos Pendientes a Proveedores**
- Visualiza cartera pendiente (lo que debemos)
- Desglosa por proveedor y responsable de cada área
- Evalúa impacto en relaciones y cashflow
- Sugiere políticas de pago efectivas

**Preguntas que activan este análisis:**
- "¿Cómo está nuestra cartera pendiente?"
- "¿Cuánto dinero debemos a proveedores?"
- "¿Órdenes sin pagar?"

---

### 5. **📂 Gastos por Categorías**
- Distribuye gasto total por categoría de compra
- Calcula % que representa cada categoría
- Analiza si hay concentración de gastos
- Recomienda auditoría y optimización

**Preguntas que activan este análisis:**
- "¿Cómo se distribuye nuestro gasto por categorías?"
- "¿Qué categorías representan mayor gasto?"
- "¿Dónde va la mayoría de nuestro presupuesto?"

---

### 6. **💸 Promedios de Gasto/Compra**
- Calcula gasto total acumulado
- Gasto promedio por orden de compra
- Promedio de órdenes que haces por mes
- Detecta si los gastos van en aumento o disminución

**Preguntas que activan este análisis:**
- "¿Cuál es el promedio de gasto por compra?"
- "¿Cuántas órdenes de compra hacemos por mes?"
- "¿Cuál es la tendencia de nuestros gastos?"

---

### 7. **📊 Salud General de Compras y Pagos**
- Consolida todos los KPIs principales
- Evalúa estado: 🟢 Saludable | 🟡 Moderado | 🔴 Crítico
- Proporciona prioridades estratégicas según urgencia
- Sugiere acciones inmediatas

**Preguntas que activan este análisis:**
- "¿Cuál es el estado general de la empresa?"
- "¿Cuáles son las prioridades estratégicas?"
- "¿Qué debería preocuparme más?"

---

## Cómo Usar el Copiloto

### Opción A: Hacer una pregunta en texto libre
1. Abre la app Streamlit
2. Ve a la sección **"Copiloto"** en el menú lateral izquierdo
3. Escribe tu pregunta en el campo de texto (en español natural)
4. Presiona el botón **"📤 Enviar"**
5. El copiloto analizará tu pregunta y mostrará la respuesta

### Opción B: Usar botones de acceso rápido
1. En la sección del copiloto, busca los **8 botones sugeridos**
2. Cada botón corresponde a un análisis:
   - 🛒 Compras Principales
   - 📦 Compras Menores
   - 🏭 Proveedores
   - ⏳ Pagos Pendientes
   - 📂 Gastos por Categoría
   - 💸 Promedios de Gasto
   - 📊 Salud General
   - 💡 Recomendaciones
3. Haz clic en cualquier botón
4. El análisis aparecerá automáticamente

---

## Estructura de Cada Respuesta

**Cada análisis que proporciona el copiloto tiene 3 partes:**

### 📊 **PARTE 1: Datos Principales**
Números específicos y exactos:
- Valores totales de gasto
- Porcentajes y comparativas
- Rankings de productos/proveedores

**Ejemplo:**
```
El producto con mayor gasto es PAPELERÍA con:
• Cantidad comprada: 5,000 unidades
• Valor gastado: $25,000,000
• Concentración: 18% del gasto total
```

### 📊 **PARTE 2: Análisis Estratégico**
Interpretación de los números:
- Qué significan los datos
- Cómo impactan la operación
- Riesgos u oportunidades identificados

**Ejemplo:**
```
Concentras el 18% de tu gasto en papelería. Esto es una 
oportunidad para negociar volumen con el proveedor.
```

### 💡 **PARTE 3: 5 Recomendaciones Accionables**
Acciones concretas que puedes implementar:

**Ejemplo:**
```
1. Consolidar órdenes: Agrupa compras semanales en comprasy mensuales
2. Negociar volumen: Usa los $25M anuales para obtener descuentos
3. Diversificar proveedores: Busca 2 proveedores alternativos
4. Automatizar: Implementa sistema de reorden automático
5. Auditar: Revisa si todo el gasto es realmente necesario
```

---

## Ejemplos Prácticos

### Escenario 1: "¿Dónde gastamos más dinero?"
```
Pregunta: "¿Cuáles son nuestros productos más comprados?"

Respuesta podría incluir:
- Producto Top: SERVICIOS DE CONSULTORÍA - $85M (28%)
- Datos: 45 órdenes, alto valor por orden
- Análisis: Dependencia de un proveedor específico
- Recomendaciones: Diversificar, negociar contrato anual, etc.
```

### Escenario 2: "¿Cuánto dinero le debemos a los proveedores?"
```
Pregunta: "¿Cómo está nuestra cartera pendiente?"

Respuesta podría incluir:
- Total pendiente: $32M (12% del gasto total)
- Estado: 🟡 MODERADO - necesita atención
- Desglose: Proveedor X: $15M, Proveedor Y: $10M, Otros: $7M
- Recomendaciones: Establecer plan de pago, designar responsables, etc.
```

### Escenario 3: "¿Cómo van nuestros gastos?"
```
Pregunta: "¿Cuál es el promedio de gasto por compra?"

Respuesta podría incluir:
- Gasto total 2024: $280M
- Promedio por orden: $1.8M
- Órdenes por mes: ~14
- Tendencia: 📈 Gastos en aumento 15% vs 2023
- Recomendaciones: Revisar si es debido a inflación o volumen, etc.
```

---

## Características del Copiloto

✅ **Entiende Preguntas en Español Natural**
- No necesitas términos técnicos exactos
- Busca palabras clave automáticamente
- Se adapta a diferentes formas de preguntar

✅ **Análisis Basado en Datos Reales**
- Números exactos de tu base de datos
- Cálculos de concentración y tendencias
- Comparativas automáticas

✅ **Recomendaciones Oriented al Negocio**
- Enfoque en optimizar gastos
- Mejorar negociaciones con proveedores
- Control de cartera y pagos

✅ **Memoria de Conversación**
- Guarda todo lo que preguntas
- Permite revisar análisis anteriores
- Facilita seguimiento de decisiones

---

## Consejos para Obtener lo Mejor del Copiloto

### 🎯 Sé Específico
**Bueno:** ¿Cuáles son los productos con mayor gasto?
**Mejor:** ¿Cuáles son mis 5 productos principales en los que gasto más, cuánto invierto en cada uno?

### 🎯 Haz Múltiples Preguntas
Combina análisis para visión 360°:
1. Primero: ¿Productos más comprados?
2. Luego: ¿Proveedores principales?
3. Finalmente: ¿Pagos pendientes?

### 🎯 Revisa el Indicador de Salud
En la parte superior ves:
- 🟢 **SALUDABLE** = Cartera <30%, todo bajo control
- 🟡 **MODERADO** = Cartera 30-70%, requiere acción
- 🔴 **CRÍTICO** = Cartera >70%, urgente actuar

### 🎯 Frecuencia Recomendada
- **Diaria:** Revisa pagos pendientes
- **Semanal:** Analiza proveedores y gastos
- **Mensual:** Evalúa salud general y tendencias

---

## Lo Que NO es (Aclaraciones)

❌ **Este NO es un análisis de ventas**
- No analiza lo que vende la empresa
- No mide clientes o ingresos
- Se enfoca en compras (lo que entra)

❌ **Este NO es un reporteautomático**
- Los datos se cargan de los CSV existentes
- Actualiza cuando cambias los archivos

❌ **Este NO reemplaza a tu equipo**
- Es una herramienta de decisión
- Tu equipo sigue siendo responsable

---

## Palabras Clave que Entiende

### Productos
- "productos más comprados"
- "mayor gasto"
- "qué compramos"
- "productos principales"

### Proveedores
- "proveedores"
- "de dónde compramos"
- "mayores órdenes"
- "principales vendedores"

### Gastos/Cartera
- "cartera pendiente"
- "pagos"
- "que debemos"
- "facturas sin pagar"
- "deuda"

### Categorías
- "categorías"
- "distribución"
- "por tipo"
- "presupuesto"

### Promedios
- "promedio"
- "cuántas órdenes"
- "tendencia"
- "comparativa"

---

## Próximos Pasos

1. **Prueba ahora:** Ejecuta `streamlit run appStreamlit.py`
2. **Selecciona Copiloto** del menú lateral
3. **Haz clic en un botón** o **escribe una pregunta**
4. **Revisa las recomendaciones**
5. **Implementa decisiones**

---

**Versión:** 2.1 - Compras y Gastos
**Enfoque:** Optimización de compras, control de gastos, fortalecimiento de relaciones con proveedores
**Última actualización:** 2026
