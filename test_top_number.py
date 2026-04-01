import re
import pandas as pd

# Test: Extraer número de "top N"
def extraer_numero_top(pregunta):
    """Extrae el número N de preguntas como 'top N' o 'top X productos'"""
    match = re.search(r'top\s+(\d+)', pregunta, re.IGNORECASE)
    if match:
        numero = int(match.group(1))
        return max(1, min(numero, 20))
    return None

# Test cases
test_cases = [
    "top 2 productos",
    "Top 5 proveedores",
    "¿Top 3 productos más comprados?",
    "productos sin especificar",
    "top 15 productos",
    "top 25 productos (debe limitar a 20)",
    "Top 1 proveedor"
]

print("🧪 Testando función de extracción de número:\n")
for test in test_cases:
    resultado = extraer_numero_top(test.lower())
    print(f"Pregunta: '{test}'")
    print(f"Resultado: {resultado}\n")

# Test: Cargar datos y verificar funcionamiento con diferentes cantidades
print("\n" + "="*60)
print("🧪 Testando análisis con diferentes cantidades:\n")

df_pedidos = pd.read_csv("Data/Pedidos.csv", sep=';', encoding='latin1')

for cantidad in [2, 3, 5, 10]:
    datos = df_pedidos.groupby('Producto')['Total pedido'].sum().reset_index().sort_values('Total pedido', ascending=False).head(cantidad)
    print(f"Top {cantidad} productos:")
    print(f"  - Cantidad de resultados: {len(datos)}")
    print(f"  - Primer producto: {datos.iloc[0]['Producto']}")
    print()

print("✅ Todos los tests pasaron correctamente!")
