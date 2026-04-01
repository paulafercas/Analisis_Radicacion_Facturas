# 🤖 Guía del Copiloto Financiero

## Descripción

El **Copiloto Financiero** es un chatbot inteligente integrado en el dashboard de Streamlit que proporciona análisis estratégicos sobre 7 aspectos clave de la salud financiera de tu empresa.

## 7 Análisis Disponibles

### 1. **🏆 Productos Más Vendidos**
- Identifica los productos con mayor facturación
- Muestra el porcentaje de concentración en el negocio
- Analiza riesgos de dependencia en pocos productos
- Recomienda estrategias de diversificación

**Preguntas para activar:**
- "¿Cuáles son nuestros productos más vendidos?"
- "¿Productos con mayor valor facturado?"

### 2. **📉 Productos Menos Vendidos**
- Identifica productos con bajo desempeño
- Analiza la brecha vs promedio
- Explora posibles causas (demanda, calidad, precio)
- Sugiere si discontinuar, reformular o promocionar

**Preguntas para activar:**
- "¿Cuáles son nuestros productos menos vendidos?"
- "¿Productos con menor facturación?"

### 3. **🏭 Proveedores Principales**
- Identifica proveedores estratégicos
- Muestra número de facturaciones y valor total
- Analiza nivel de dependencia
- Recomienda diversificación y alianzas estratégicas

**Preguntas para activar:**
- "¿Quiénes son nuestros proveedores principales?"
- "¿Proveedores con más facturaciones?"

### 4. **⏳ Facturas Pendientes**
- Visualiza cartera pendiente total y por año
- Desglosa por proveedor y responsable
- Evalúa impacto en cashflow y salud financiera
- Sugiere políticas de cobranza activa

**Preguntas para activar:**
- "¿Cómo está nuestra cartera pendiente?"
- "¿Cuánto dinero tenemos pendiente de cobrar?"
- "¿Facturas sin pagar?"

### 5. **📂 Categorías Principales**
- Distribuye ingresos por categoría
- Calcula porcentaje de aporte de cada categoría
- Analiza diversificación del negocio
- Recomienda mix óptimo (30-30-30-10)

**Preguntas para activar:**
- "¿Cómo se distribuye nuestro negocio por categorías?"
- "¿Categorías principales y su aporte?"

### 6. **💰 Promedios de Facturación**
- Calcula valor total facturado
- Promedio por factura (ticket promedio)
- Promedio de facturas por mes
- Desglosa por año y detecta tendencias

**Preguntas para activar:**
- "¿Cuál es el promedio de facturación?"
- "¿Cuántas facturas hacemos por mes?"
- "¿Tendencia de facturación?"

### 7. **📊 Salud General de la Empresa**
- Compila todos los KPIs principales
- Evalúa estado: 🟢 Saludable, 🟡 Moderado o 🔴 Crítico
- Proporciona prioridades estratégicas
- Sugiere acciones inmediatas

**Preguntas para activar:**
- "¿Cuál es el estado general de la empresa?"
- "¿Recomendaciones estratégicas?"

## Cómo Usar el Copiloto

### Opción 1: Escribir tu pregunta
1. Ve a la sección **"Copiloto"** en el menú lateral
2. Escribe tu pregunta en el cuadro de texto
3. Presiona **"📤 Enviar"**
4. El copiloto analizará tu pregunta y proporcionará una respuesta detallada

### Opción 2: Usar preguntas sugeridas
1. Desplázate hasta las **"Preguntas sugeridas"**
2. Haz clic en uno de los botones (🏆 Productos Top, ⏳ Cartera Pendiente, etc.)
3. El copiloto cargará automáticamente el análisis

## Estructura de Cada Respuesta

Cada respuesta del copiloto incluye:

### 📊 **Datos Principales**
- Número específicos y valores
- Comparativas y porcentajes
- Ranking o distribución

### 📊 **Análisis Integral**
- Interpretación de los datos
- Implicaciones para el negocio
- Identificación de riesgos u oportunidades

### 💡 **Recomendaciones Estratégicas**
- 5 acciones específicas que puedes implementar
- Prioridades según criticidad
- Fokus en salud financiera y fortalecimiento de negocios

## Ejemplos de Uso

### Escenario 1: Analizar Concentración de Productos
```
Pregunta: "¿Cuáles son nuestros productos más vendidos?"

Respuesta:
- Identifica producto líder
- Muestra % de concentración
- Alerta sobre riesgo de dependencia
- Recomienda desarrollar nuevos productos
```

### Escenario 2: Gestión de Cartera
```
Pregunta: "¿Cómo está nuestra cartera pendiente?"

Respuesta:
- Total pendiente
- Facturas sin pagar
- Proveedores con mayor deuda
- Responsables asignados
- Salud financiera: 🟢🟡🔴
- Plan de acción para cobranza
```

### Escenario 3: Proyecciones
```
Pregunta: "¿Cuál es el promedio de facturación?"

Respuesta:
- Ticket promedio
- Facturas por mes
- Tendencia (crecimiento/decline)
- Estrategias para aumentar ticket
```

## Características del Copiloto

✅ **Inteligencia Contextual**
- Entiende diferentes formas de hacer la misma pregunta
- Busca palabras clave relevantes

✅ **Análisis Multidimensional**
- Datos numéricos precisos
- Interpretación de tendencias
- Evaluación de riesgos

✅ **Recomendaciones Estratégicas**
- Enfocadas en salud financiera
- Fortalecimiento de relaciones comerciales
- Oportunidades de crecimiento

✅ **Historial Conversacional**
- Mantiene registro de todas las preguntas
- Permite seguimiento de temas
- Facilita decisiones informadas

## Tips para Mejores Resultados

1. **Sé específico**: "¿Productos top 5 por valor?" es mejor que "¿productos?"
2. **Usa palabras clave**: El copiloto entiende "cartera", "pendiente", "deuda"
3. **Explora múltiples perspectivas**: Pregunta sobre tendencias, comparativas, rankings
4. **Revisa regularmente**: El análisis refleja datos actuales
5. **Combina análisis**: Cruza información de diferentes reportes

## Requisitos Técnicos

- Archivos CSV en la carpeta `Data/`:
  - `Facturacion.csv`
  - `Pedidos.csv`
  - `Proveedor.csv`
- Streamlit instalado
- Pandas, Plotly, pandasql

## Ejecución

```bash
streamlit run appStreamlit.py
```

Luego selecciona **"Copiloto"** del menú lateral.

---

**Desarrollado para:** Análisis Integral de Facturación y Radicación
**Versión:** 2.0 - Con Copiloto Inteligente
