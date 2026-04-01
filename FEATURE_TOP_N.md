# ✨ FEATURE: Top N - Especificar Cantidad de Resultados

## Lo Nuevo

Ahora puedes pedir un **número específico de elementos** en los análisis. Si dices "top 2" o "top 5", el copiloto devuelve exactamente esa cantidad.

---

## 🎯 Cómo Usar

### Formato: "Top N [elemento]" o "¿Top N [elemento]...?"

### Ejemplos:

#### Productos
```
"Top 2 productos más comprados"
→ Devuelve: Top 2 productos con mayor gasto

"Top 5 productos menos comprados"
→ Devuelve: 5 productos con menor gasto

"¿Cuál es top 3 de mis compras?"
→ Devuelve: 3 productos principales
```

#### Proveedores
```
"Top 3 proveedores"
→ Devuelve: 3 proveedores principales

"Top 7 proveedores principales"
→ Devuelve: 7 proveedores por mayor inversión

"¿Top 1 proveedor donde gastamos más?"
→ Devuelve: El proveedor #1 únicamente
```

#### Responsables (Cartera Pendiente)
```
"Top 4 responsables con facturas pendientes"
→ Devuelve: 4 responsables con más cartera

"¿Top 2 responsables?"
→ Devuelve: 2 responsables principales
```

---

## 📊 Valores por Defecto

Si **NO especificas un número**, se usan estos valores por defecto:

| Análisis | Por Defecto |
|----------|------------|
| Productos Más Comprados | 5 |
| Productos Menos Comprados | 3 |
| Proveedores Principales | 5 |
| Responsables (cartera) | Ver todos |
| Categorías | Todas |

---

## 🚀 Ejemplos Prácticos

### Escenario 1: "Solo quiero los 2 productos principales"
```
Pregunta: "Top 2 productos más comprados"

Respuesta:
🛒 Top 2 Productos Más Comprados (Mayor Gasto)

Desglose de Top 2:
1. Licencia ERP empresarial: $85,000,000 (28%)
2. Servicios de consultoría: $65,500,000 (22%)

[Análisis y recomendaciones para estos 2 productos]
```

### Escenario 2: "Quiero ver muchos proveedores"
```
Pregunta: "Top 10 proveedores"

Respuesta:
🏭 Top 10 Proveedores Principales (Mayor Inversión)

Desglose de Top 10 Proveedores:
1. Proveedor X: $50M (16.7%)
2. Proveedor Y: $45M (15%)
3. Proveedor Z: $40M (13.3%)
... (7 más)

[Análisis consolidado de los 10 principales]
```

### Escenario 3: "Solo quiero el peor 1 producto"
```
Pregunta: "Top 1 productos menos comprados"

Respuesta:
📦 Top 1 Productos Menos Comprados (Menor Gasto)

Desglose de Top 1:
1. Suministros menores: $500,000

[Análisis específico]
```

---

## 🔒 Límites

- **Mínimo:** Top 1 (un solo elemento)
- **Máximo:** Top 20 (limitado para no saturar)
- Si escribes "Top 25", automáticamente se convierte a "Top 20"
- Si no escribes un número, usa el valor por defecto

---

## 🎨 Cómo Funciona Internamente

1. **Detección de "Top N"**
   - El copiloto busca patrones como "top 2", "TOP 5", "¿top 3?"
   - Extrae el número usando expresiones regulares

2. **Validación**
   - Valida que esté entre 1 y 20
   - Si no hay número, usa el default

3. **Ejecución**
   - Pasa el número a la función de análisis
   - La función devuelve exactamente esa cantidad
   - Muestra desglose completo

---

## 💡 Tips

### Para Análisis Rápido
```
"Top 2 proveedores"  
→ Rápido e inequívoco
```

### Para Análisis Profundo
```
"Top 10 productos más comprados"
→ Más contexto, más perspectiva
```

### Preguntas Naturales Que También Funcionan
```
"¿Cuál es top 3?"                    ✅ Funciona
"Top de 5 productos"                 ✅ Funciona
"Muestra top 4 proveedores"          ✅ Funciona
"Top 6 de lo que compramos"          ✅ Funciona
"Los top 2"                          ✅ Funciona
"Quiero los 3 mejores top"           ❌ No detecta "top 3"
```

---

## 📝 Análisis que Soportan "Top N"

### ✅ Soportados
- 🛒 **Productos Más Comprados** - Usa el número especificado
- 📦 **Productos Menos Comprados** - Usa el número especificado
- 🏭 **Proveedores Principales** - Usa el número especificado

### ⏳ Parcialmente Soportados
- **Cartera Pendiente** - Muestra todos los responsables (aunque puedes pedir "top X")
- **Categorías** - Muestra siempre top 3 (podría extenderse)

### ❌ No Aplica
- **Promedios** - Calcula sobre todo el dataset
- **Salud General** - Es un resumen consolidado

---

## 🧪 Validación

```
✅ Función extraer_numero_top: Funciona correctamente
✅ Top 2: Devuelve 2 elementos
✅ Top 5: Devuelve 5 elementos
✅ Top 20: Devuelve 20 elementos
✅ Top 25: Se limita a 20 elementos
✅ Sin número: Usa valores por defecto
✅ Desglose: Muestra todos los elementos del top
```

---

## 🚀 Próximos Pasos

Ahora puedes:
1. Ejecutar `streamlit run appStreamlit.py`
2. Ir a Copiloto
3. Escribir: **"Top 3 productos más comprados"**
4. Ver resultados con exactamente 3 productos

---

**Versión:** 2.2 - Feature Top N Implementado
**Estado:** ✅ Completo y Validado
**Fecha:** 2026
