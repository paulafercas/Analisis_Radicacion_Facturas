# 📚 Documentación Técnica del Copiloto Financiero

## Arquitectura General

```
appStreamlit.py
├── Carga de datos (CSV)
│   ├── df_facturacion
│   ├── df_pedidos
│   └── df_proveedor
├── Pre-procesamiento
│   └── Conversión de fechas a datetime
├── Funciones de Análisis (7 módulos)
│   ├── obtener_analisis_productos_mas_vendidos()
│   ├── obtener_analisis_productos_menos_vendidos()
│   ├── obtener_analisis_proveedores_principales()
│   ├── obtener_analisis_facturas_pendientes()
│   ├── obtener_analisis_categorias()
│   ├── obtener_analisis_promedios()
│   └── responder_pregunta_general()
└── Interfaz Streamlit
    ├── Input del usuario
    ├── Botones de sugerencias rápidas
    ├── Historial de conversación
    └── Session state management
```

## Funciones de Análisis

### 1. `obtener_analisis_productos_mas_vendidos()`
```python
def obtener_analisis_productos_mas_vendidos():
    # Agrupa por producto y suma valor
    # Identifica top 5
    # Calcula concentración %
    # Genera respuesta con 5 recomendaciones
    return respuesta
```

**Lógica:**
- GroupBy 'Producto' en df_pedidos
- Suma 'Total pedido' 
- Sort descending
- Top row = líder
- Cálculo: (valor_top / valor_total) * 100 = concentración

**Palabras clave que activan:**
- "producto" + ("más" | "top" | "mayor" | "vend")

---

### 2. `obtener_analisis_productos_menos_vendidos()`
Similar a anterior pero con `sort_values(ascending=True)`

**Palabras clave:**
- "producto" + ("menos" | "bajo" | "menor")

---

### 3. `obtener_analisis_proveedores_principales()`
```python
def obtener_analisis_proveedores_principales():
    # GroupBy 'nombre_proveedor' en df_facturacion
    # Cuenta 'numero_factura' (total facturaciones)
    # Suma 'valor_total $' (valor total)
    # Identifica dependencia
```

**Palabras clave:**
- "proveedor"

---

### 4. `obtener_analisis_facturas_pendientes()`
```python
def obtener_analisis_facturas_pendientes():
    # Filtra df_facturacion['estado_factura'] == 'Pendiente'
    # Suma 'valor_total $'
    # GroupBy 'nombre_proveedor' y 'responsable'
    # Calcula porcentaje de cartera pendiente
    # Evalúa salud: 🟢 <30% | 🟡 30-70% | 🔴 >70%
```

**Palabras clave:**
- "cartera" | "pendiente" | "cobrar" | "deuda" | "pago"

---

### 5. `obtener_analisis_categorias()`
```python
def obtener_analisis_categorias():
    # GroupBy 'categoria'
    # Suma 'valor_total $'
    # Calcula porcentaje de aporte
    # Evalúa diversificación
```

**Palabras clave:**
- "categor"

---

### 6. `obtener_analisis_promedios()`
```python
def obtener_analisis_promedios():
    # Calcula promedio de 'valor_total $' en facturación
    # GroupBy año y mes
    # Genera tabla por año con métricas
    # Detecta tendencia crecimiento/decline
```

**Palabras clave:**
- "promedio" | ("factura" + "mes")

---

### 7. `responder_pregunta_general()`
Función por defecto si no coincide con otras palabras clave.
Devuelve análisis general con todos los KPIs.

---

## Integración con Streamlit

### Session State
```python
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Agregar mensaje
st.session_state.chat_history.append({
    "role": "user" | "assistant",
    "message": texto
})

# Rerun para actualizar UI
st.rerun()
```

### Flow del Chatbot

1. **Usuario escribe pregunta** → Text input captura
2. **Click "Enviar"** → Valida entrada
3. **Procesa pregunta:**
   - Convierte a minúsculas
   - Busca palabras clave
   - Llama función de análisis correspondiente
4. **Agrega respuesta al historial**
5. **`st.rerun()`** → Redibuja UI con nuevo mensaje

---

## Estructura de Respuestas

Cada respuesta sigue este patrón:

```markdown
**[EMOJI] [TÍTULO]**

[DATOS PRINCIPALES]
• Métrica 1: Valor
• Métrica 2: Valor
• Métrica 3: Valor

**📊 Análisis:**
[Interpretación de datos y contexto empresarial]

**💡 Recomendaciones Estratégicas:**
1. [Acción 1]
2. [Acción 2]
3. [Acción 3]
4. [Acción 4]
5. [Acción 5]
```

---

## Extensibilidad

### Agregar Nuevo Análisis

1. **Crear función:**
```python
def obtener_analisis_nuevo_tema():
    # Lógica aquí
    respuesta = f"""
    **Análisis**
    
    Datos: {datos}
    """
    return respuesta
```

2. **Agregar palabra clave en procesamiento:**
```python
elif "nueva_palabra" in user_message:
    respuesta = obtener_analisis_nuevo_tema()
```

3. **Agregar botón de sugerencia:**
```python
sugerencias = [
    ...,
    ("🆕 Nuevo Tema", "¿Pregunta sobre nuevo tema?")
]
```

### Personalizar Recomendaciones

Cada función genera recomendaciones custom. Para cambiar:

1. Editar la sección `**💡 Recomendaciones Estratégicas:**`
2. Mantener 5 recomendaciones
3. Enfocar en: salud financiera, relaciones comerciales, optimización

---

## Fuentes de Datos

### df_facturacion
Columnas principales:
- `fecha_factura` - Fecha del documento
- `numero_factura` - ID de factura
- `nombre_proveedor` - Nombre del proveedor
- `valor_total $` - Monto de la factura
- `estado_factura` - "Pagado" | "Pendiente"
- `categoria` - Categoría del producto/servicio
- `responsable` - Persona responsable

### df_pedidos
Columnas principales:
- `Numero_pedido` - ID del pedido
- `nombre_proveedor` - Proveedor
- `Producto` - Descripción del producto
- `cantidad` - Unidades
- `Total pedido` - Valor total

### df_proveedor
Columnas principales:
- `nombre_proveedor` - Nombre
- `nit_proveedor` - NIT (ID)
- `categoria` - Categoría del proveedor
- `ubicacion` - Ubicación

---

## Validación de Datos

Ejecutar antes de cambios:
```bash
python test_copiloto.py
```

Verifica:
- ✅ Carga de datos
- ✅ Conversión de fechas
- ✅ Operaciones de groupby
- ✅ Cálculos principales

---

## Mejoras Futuras

- [ ] Integrar IA para procesamiento de lenguaje natural más avanzado
- [ ] Agregar gráficos a las respuestas del copiloto
- [ ] Exportar análisis a PDF
- [ ] Integración con bases de datos en tiempo real
- [ ] Alertas automáticas basadas en umbrales
- [ ] Machine Learning para predicciones
- [ ] Dashboard comparativo (mes anterior, mismo mes año anterior)
- [ ] Análisis de márgenes y rentabilidad por categoría

---

## Notas Importantes

1. **Encoding**: Los CSV usan encoding 'latin1' durante carga
2. **Separador**: Los CSV usan ';' como separador
3. **Moneda**: Todos los valores están en pesos ($)
4. **Período**: Datos de 2022-2025
5. **Session**: El historial se reinicia cada vez que recargas la página

---

**Versión:** 2.0  
**Última actualización:** 2024  
**Autor:** Dashboard Development Team
