import pandas as pd
from pandasql import sqldf

# Test: Load data
try:
    df_facturacion = pd.read_csv("Data/Facturacion.csv", sep=';', encoding='latin1')
    df_pedidos = pd.read_csv("Data/Pedidos.csv", sep=';', encoding='latin1')
    df_proveedor = pd.read_csv("Data/Proveedor.csv", sep=';', encoding='latin1')
    print("✅ All data loaded successfully")
    print(f"✅ Facturacion records: {len(df_facturacion)}")
    print(f"✅ Pedidos records: {len(df_pedidos)}")
    print(f"✅ Proveedor records: {len(df_proveedor)}")
    
    # Convert dates
    df_facturacion['fecha_factura'] = pd.to_datetime(df_facturacion['fecha_factura'])
    print("✅ Dates converted successfully")
    
    # Test groupby operations
    print("\n🧪 Testing analysis functions...")
    
    # Test 1: Top products
    top_productos = df_pedidos.groupby('Producto')['Total pedido'].sum().sort_values(ascending=False).head(3)
    print(f"✅ Top 3 products loaded: {len(top_productos)} products")
    
    # Test 2: Main providers
    top_proveedores = df_facturacion.groupby('nombre_proveedor')['valor_total $'].sum().sort_values(ascending=False).head(3)
    print(f"✅ Top 3 providers loaded: {len(top_proveedores)} providers")
    
    # Test 3: Pending invoices
    pendientes = df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']['valor_total $'].sum()
    print(f"✅ Pending invoices total: ${pendientes:,.2f}")
    
    # Test 4: Categories
    categorias = df_facturacion.groupby('categoria')['valor_total $'].sum().sort_values(ascending=False).head(3)
    print(f"✅ Top 3 categories loaded: {len(categorias)} categories")
    
    print("\n✨ All tests passed! The chatbot functions should work correctly.")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
