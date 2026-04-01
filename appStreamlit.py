import streamlit as st
import pandas as pd
import plotly.express as px
from pandasql import sqldf

#Dataframe para facturacion.csv
df_facturacion= pd.read_csv("Data/Facturacion.csv", sep=';', encoding='latin1')

#Dataframe para pedidos.csv
df_pedidos = pd.read_csv("Data/Pedidos.csv", sep=';', encoding='latin1')

#Dataframe para proveedor.csv
df_proveedor = pd.read_csv("Data/Proveedor.csv", sep=';', encoding='latin1')

# Convertir fechas a datetime
df_facturacion['fecha_factura'] = pd.to_datetime(df_facturacion['fecha_factura'])

#Ejecutamos sql
pysqldf = lambda q: sqldf(q, globals())

# Nuevos DataFrames basados en las consultas SQL proporcionadas

# Top 5 de productos más pedidos según la cantidad total
df_top5_productos_mas_pedidos_cantidad = (
    df_pedidos.groupby('Producto')['cantidad']
    .sum()
    .reset_index()
    .rename(columns={'cantidad': 'total_cantidad'})
    .sort_values('total_cantidad', ascending=False)
    .head(5)
)

# Top 5 productos menos pedidos según cantidad
df_top5_productos_menos_pedidos_cantidad = (
    df_pedidos.groupby('Producto')['cantidad']
    .sum()
    .reset_index()
    .rename(columns={'cantidad': 'total_cantidad'})
    .sort_values('total_cantidad', ascending=True)
    .head(5)
)

# Top 5 productos más pedidos según valor total facturado
df_top5_productos_mas_pedidos_valor = (
    df_pedidos.groupby('Producto')['Total pedido']
    .sum()
    .reset_index()
    .rename(columns={'Total pedido': 'total_facturado'})
    .sort_values('total_facturado', ascending=False)
    .head(3)
)

# Top 5 productos menos pedidos según valor total facturado
df_top5_productos_menos_pedidos_valor = (
    df_pedidos.groupby('Producto')['Total pedido']
    .sum()
    .reset_index()
    .rename(columns={'Total pedido': 'total_facturado'})
    .sort_values('total_facturado', ascending=True)
    .head(3)
)

# Top 5 proveedores con más facturaciones
df_top5_proveedores_mas_facturaciones = (
    df_facturacion.groupby('nombre_proveedor')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturaciones'})
    .sort_values('total_facturaciones', ascending=False)
    .head(5)
)

# Proveedores con menos facturaciones
df_top5_proveedores_menos_facturaciones = (
    df_facturacion.groupby('nombre_proveedor')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturaciones'})
    .sort_values('total_facturaciones', ascending=True)
    .head(3)
)

# Top 5 proveedores con más valor total facturado
df_top5_proveedores_mas_valor_facturado = (
    df_facturacion.groupby('nombre_proveedor')['valor_total $']
    .sum()
    .reset_index()
    .rename(columns={'valor_total $': 'total_facturado'})
    .sort_values('total_facturado', ascending=False)
    .head(5)
)

# Top 5 proveedores con menos valor total facturado
df_top5_proveedores_menos_valor_facturado = (
    df_facturacion.groupby('nombre_proveedor')['valor_total $']
    .sum()
    .reset_index()
    .rename(columns={'valor_total $': 'total_facturado'})
    .sort_values('total_facturado', ascending=True)
    .head(3)
)

# Facturas pendientes de pago en cada año
df_facturas_pendientes_por_anio = (
    df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']
    .groupby(df_facturacion['fecha_factura'].dt.year)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'facturas_pendientes', 'fecha_factura': 'anio'})
    .sort_values('anio')
)

# Total a pagar en cada año por facturas no pagadas
df_total_pendiente_por_anio = (
    df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']
    .groupby(df_facturacion['fecha_factura'].dt.year)['valor_total $']
    .sum()
    .reset_index()
    .rename(columns={'valor_total $': 'total_pendiente', 'fecha_factura': 'anio'})
    .sort_values('anio')
)

# Frecuencia de tipo de facturas
df_frecuencia_tipo_factura = (
    df_facturacion.groupby('tipo_factura')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'cantidad'})
)

# Mes en el año 2022 donde más se efectúan facturas
df_mes_mas_facturas_2022 = (
    df_facturacion[df_facturacion['fecha_factura'].dt.year == 2022]
    .groupby(df_facturacion['fecha_factura'].dt.month)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturas', 'fecha_factura': 'mes'})
    .sort_values('total_facturas', ascending=False)
)

# Mes en el año 2023 donde más se efectúan facturas
df_mes_mas_facturas_2023 = (
    df_facturacion[df_facturacion['fecha_factura'].dt.year == 2023]
    .groupby(df_facturacion['fecha_factura'].dt.month)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturas', 'fecha_factura': 'mes'})
    .sort_values('total_facturas', ascending=False)
)

# Mes en el año 2024 donde más se efectúan facturas
df_mes_mas_facturas_2024 = (
    df_facturacion[df_facturacion['fecha_factura'].dt.year == 2024]
    .groupby(df_facturacion['fecha_factura'].dt.month)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturas', 'fecha_factura': 'mes'})
    .sort_values('total_facturas', ascending=False)
)

# Mes en el año 2025 donde más se efectúan facturas
df_mes_mas_facturas_2025 = (
    df_facturacion[df_facturacion['fecha_factura'].dt.year == 2025]
    .groupby(df_facturacion['fecha_factura'].dt.month)['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_facturas', 'fecha_factura': 'mes'})
    .sort_values('total_facturas', ascending=False)
)

# Responsable con más facturas pendientes de pago
df_responsable_mas_pendientes = (
    df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']
    .groupby('responsable')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'total_pendientes'})
    .sort_values('total_pendientes', ascending=False)
)

# Facturas pendientes por proveedor
df_facturas_pendientes_por_proveedor = (
    df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']
    .groupby('nombre_proveedor')['numero_factura']
    .count()
    .reset_index()
    .rename(columns={'numero_factura': 'facturas_pendientes'})
    .sort_values('facturas_pendientes', ascending=False)
    .head(10)
)

# Consultas adicionales: totales únicos y generales

# Total de proveedores únicos
total_proveedores_unicos = df_facturacion['nombre_proveedor'].nunique()

# Total de facturaciones
total_facturaciones = len(df_facturacion)

# Total de valor facturado
total_valor_facturado = df_facturacion['valor_total $'].sum()

# Total de productos únicos
total_productos_unicos = df_pedidos['Producto'].nunique()

# Para consistencia, crear DataFrames con estos totales
df_totales_generales = pd.DataFrame({
    'metrica': ['Total Proveedores Únicos', 'Total Facturaciones', 'Total Valor Facturado', 'Total Productos Únicos'],
    'valor': [total_proveedores_unicos, total_facturaciones, total_valor_facturado, total_productos_unicos]
})

# Limpiar nombres: remover tildes y truncar si son largos
import unicodedata

def limpiar_nombres(df, columna):
    df[columna] = df[columna].astype(str).apply(lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('ascii'))
    df[columna] = df[columna].apply(lambda x: x[:20] + '...' if len(x) > 20 else x)
    return df

# Aplicar limpieza a DataFrames relevantes
df_top5_productos_mas_pedidos_cantidad = limpiar_nombres(df_top5_productos_mas_pedidos_cantidad, 'Producto')
df_top5_productos_menos_pedidos_cantidad = limpiar_nombres(df_top5_productos_menos_pedidos_cantidad, 'Producto')
df_top5_productos_mas_pedidos_valor = limpiar_nombres(df_top5_productos_mas_pedidos_valor, 'Producto')
df_top5_productos_menos_pedidos_valor = limpiar_nombres(df_top5_productos_menos_pedidos_valor, 'Producto')
df_top5_proveedores_mas_facturaciones = limpiar_nombres(df_top5_proveedores_mas_facturaciones, 'nombre_proveedor')
df_top5_proveedores_menos_facturaciones = limpiar_nombres(df_top5_proveedores_menos_facturaciones, 'nombre_proveedor')
df_top5_proveedores_mas_valor_facturado = limpiar_nombres(df_top5_proveedores_mas_valor_facturado, 'nombre_proveedor')
df_top5_proveedores_menos_valor_facturado = limpiar_nombres(df_top5_proveedores_menos_valor_facturado, 'nombre_proveedor')
df_facturas_pendientes_por_proveedor = limpiar_nombres(df_facturas_pendientes_por_proveedor, 'nombre_proveedor')
df_responsable_mas_pendientes = limpiar_nombres(df_responsable_mas_pendientes, 'responsable')

# Estilo de la pagina
st.set_page_config(
    page_title="Dashboard Facturación",
    layout="wide"
)

# CSS personalizado con colores púrpura, azul y naranja
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

<style>
.metric-card {
    background-color: #f0f0f0;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    font-family: 'Helvetica Neue', sans-serif;
    border-left: 5px solid #6a0dad; /* Púrpura */
}

.metric-title {
    color: #333;
    font-size: 14px;
    margin-bottom: 10px;
}

.metric-value {
    color: #1f77b4; /* Azul */
    font-size: 32px;
    font-weight: 700;
}

.sidebar-button {
    background-color: #6a0dad; /* Púrpura */
    color: white;
    border: 2px solid #6a0dad; /* Borde morado */
    padding: 15px 20px;
    border-radius: 0px; /* Rectangulares */
    margin: 5px;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    font-family: 'Helvetica Neue', sans-serif;
    transition: background-color 0.3s, color 0.3s;
}

.sidebar-button:hover {
    background-color: #1f77b4; /* Azul al hover */
}

.sidebar-button.selected {
    background-color: #1f77b4; /* Azul cuando seleccionado */
    color: white;
}

/* Estilos para radio buttons */
.stRadio > div > label {
    background-color: #87CEEB; /* Azul celeste */
    color: white;
    border: 2px solid #87CEEB;
    padding: 10px 15px; /* Más pequeño */
    border-radius: 10px; /* Esquinas suavizadas */
    margin: 5px 0;
    width: 100%;
    display: block;
    font-size: 16px;
    font-weight: bold;
    font-family: 'Helvetica Neue', sans-serif;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
}

.stRadio > div > label:hover {
    background-color: #4682B4; /* Azul más oscuro */
    color: white;
}

.stRadio > div > input[type="radio"]:checked + label {
    background-color: #4682B4; /* Azul más oscuro */
    color: white;
}

.sub-button {
    background-color: #ff7f0e; /* Naranja */
    color: white;
    border: none;
    padding: 8px;
    border-radius: 5px;
    margin: 5px;
}

.chart-container {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Helvetica Neue', sans-serif;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Navegación con sidebar
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("Selecciona una opción:", ["Inicio", "Productos", "Proveedores", "Facturas pendientes", "Facturas", "Copiloto"])

# Función para mostrar métricas generales
def mostrar_metricas_generales():
    st.header("Dashboards Informacionales")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Proveedores Únicos</div>
            <div class="metric-value">{total_proveedores_unicos}</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Facturaciones</div>
            <div class="metric-value">{total_facturaciones}</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Valor Facturado</div>
            <div class="metric-value">${total_valor_facturado:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Productos Únicos</div>
            <div class="metric-value">{total_productos_unicos}</div>
        </div>
        """, unsafe_allow_html=True)

# Escala de salud de la empresa
def mostrar_escala_salud():
    total_pendiente = df_total_pendiente_por_anio['total_pendiente'].sum()
    salud_porcentaje = max(0, (total_pendiente / total_valor_facturado) * 100)
    if salud_porcentaje < 30:
        emoji = "🟢"
        status = "Saludable"
        color = "#28a745"  # Verde
    elif salud_porcentaje < 70:
        emoji = "🟡"
        status = "Moderado"
        color = "#ffc107"  # Amarillo
    else:
        emoji = "🔴"
        status = "Alto Riesgo"
        color = "#dc3545"  # Rojo
    st.subheader("📊 Escala de Salud de la Empresa")
    progress_html = f"""
    <div style="width: 100%; background-color: #e9ecef; border-radius: 10px; height: 20px;">
        <div style="width: {salud_porcentaje}%; background-color: {color}; height: 20px; border-radius: 10px;"></div>
    </div>
    """
    st.markdown(progress_html, unsafe_allow_html=True)
    st.write(f"{emoji} Porcentaje de Endeudamiento: {salud_porcentaje:.1f}% - {status}")

# Mostrar métricas y salud en todas las páginas
mostrar_metricas_generales()
mostrar_escala_salud()

# Contenido basado en la opción seleccionada
if opcion == "Productos":
    st.header("📦 Análisis de Productos")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 5 Productos con mayor volumen de facturacion")
        fig = px.bar(df_top5_productos_mas_pedidos_cantidad, x='Producto', y='total_cantidad', color='Producto', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)
    with col2:
        st.subheader("Top 5 Productos con mayor valor facturado")
        fig = px.bar(df_top5_productos_menos_pedidos_cantidad, x='Producto', y='total_cantidad', color='Producto', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Productos con menor volumen de facturacion")
        fig = px.bar(df_top5_productos_mas_pedidos_valor, x='Producto', y='total_facturado', color='Producto', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)
    with col4:
        st.subheader("Productos con menor valor facturado")
        fig = px.bar(df_top5_productos_menos_pedidos_valor, x='Producto', y='total_facturado', color='Producto', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)

elif opcion == "Proveedores":
    st.header("🏭 Análisis de Proveedores")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 5 Proveedores con mayor volumen de facturacion")
        fig = px.bar(df_top5_proveedores_mas_facturaciones, x='nombre_proveedor', y='total_facturaciones', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)
    with col2:
        st.subheader("Proveedores con menor volumen de facturacion")
        fig = px.bar(df_top5_proveedores_menos_facturaciones, x='nombre_proveedor', y='total_facturaciones', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Top 5 Proveedores con mayor Valor Facturado")
        fig = px.bar(df_top5_proveedores_mas_valor_facturado, x='nombre_proveedor', y='total_facturado', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)
    with col4:
        st.subheader("Proveedores con menor Valor Facturado")
        fig = px.bar(df_top5_proveedores_menos_valor_facturado, x='nombre_proveedor', y='total_facturado', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)

elif opcion == "Facturas pendientes":
    st.header("⏳ Análisis de Facturas Pendientes")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Facturas Pendientes por Año")
        fig = px.bar(df_facturas_pendientes_por_anio, x='anio', y='facturas_pendientes', color='anio', color_discrete_sequence=px.colors.qualitative.Set1)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)
    with col2:
        st.subheader("Valor Total Pendiente por Año")
        def estilo_violetta(row):
            colores = ['#f3e5ff', '#e0bbff']
            return ['background-color: %s' % colores[i % 2] for i in range(len(row))]
        st.dataframe(
            df_total_pendiente_por_anio.style
                .apply(estilo_violetta, axis=1)
                .hide(axis='index')
                .set_table_styles([
                    {'selector': 'th', 'props': [('background-color', '#d1c4e9'), ('color', '#3f2f67'), ('font-weight', 'bold')]},
                    {'selector': 'td', 'props': [('padding', '8px'), ('text-align', 'center'), ('color', '#2a1f4b')]}
                ])
        )
    st.subheader("Responsables con Más Facturas Pendientes")
    fig = px.bar(df_responsable_mas_pendientes, x='responsable', y='total_pendientes', color='responsable', color_discrete_sequence=px.colors.qualitative.Set1)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig)
    st.subheader("Top 10 Proveedores con Facturas Pendientes")
    fig = px.bar(df_facturas_pendientes_por_proveedor, x='nombre_proveedor', y='facturas_pendientes', color='nombre_proveedor', color_discrete_sequence=px.colors.qualitative.Set1)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig)

elif opcion == "Facturas":
    st.header("📄 Análisis de Facturas por Año")
    anio_seleccionado = st.selectbox("Selecciona un año:", [2022, 2023, 2024, 2025])
    if anio_seleccionado == 2022:
        df_mes = df_mes_mas_facturas_2022
    elif anio_seleccionado == 2023:
        df_mes = df_mes_mas_facturas_2023
    elif anio_seleccionado == 2024:
        df_mes = df_mes_mas_facturas_2024
    elif anio_seleccionado == 2025:
        df_mes = df_mes_mas_facturas_2025
    st.subheader(f"Facturas por Mes en {anio_seleccionado}")
    fig = px.bar(df_mes, x='mes', y='total_facturas', color='mes', color_discrete_sequence=px.colors.qualitative.Set1)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig)

    st.subheader("Distribución de Tipo de Facturas")
    fig_pie = px.pie(df_frecuencia_tipo_factura, names='tipo_factura', values='cantidad', title='Distribución de Tipo de Facturas (Física/Electrónica)', color_discrete_sequence=['#1f77b4', '#9467bd'])
    st.plotly_chart(fig_pie)

elif opcion == "Copiloto":
    st.header("🤖 Copiloto Financiero - Análisis Inteligente")
    st.markdown("*Chatbot inteligente para análisis empresarial y recomendaciones estratégicas*")
    
    # ==================== FUNCIONES DE ANÁLISIS ====================
    
    def obtener_analisis_productos_mas_vendidos():
        """Análisis de productos más vendidos con valor facturado"""
        datos = df_pedidos.groupby('Producto').agg({
            'cantidad': 'sum',
            'Total pedido': 'sum'
        }).reset_index().sort_values('Total pedido', ascending=False).head(5)
        
        top_producto = datos.iloc[0]
        total_valor_top = top_producto['Total pedido']
        promedio_valor = datos['Total pedido'].mean()
        concentracion = (total_valor_top / datos['Total pedido'].sum()) * 100
        
        respuesta = f"""
        **🏆 Productos Más Vendidos**
        
        El producto líder es **{top_producto['Producto']}** con:
        • Cantidad vendida: {top_producto['cantidad']:,.0f} unidades
        • Valor facturado: ${total_valor_top:,.2f}
        • Concentración: {concentracion:.1f}% del valor total
        
        **📊 Análisis:**
        El volumen de ventas está concentrado en pocos productos ({concentracion:.1f}% en el principal). 
        Esto sugiere que tu empresa depende significativamente de estos productos clave.
        
        **💡 Recomendaciones Estratégicas:**
        1. **Diversificación**: Considera desarrollar nuevos productos para reducir riesgos
        2. **Fortalecimiento**: Asegura cadenas de suministro robustas para los productos estrella
        3. **Pricing**: Evalúa aumentar márgenes de los productos de mayor demanda
        4. **Marketing**: Invierte en promoción de productos con menor rotación
        """
        return respuesta
    
    def obtener_analisis_productos_menos_vendidos():
        """Análisis de productos menos vendidos"""
        datos = df_pedidos.groupby('Producto').agg({
            'cantidad': 'sum',
            'Total pedido': 'sum'
        }).reset_index().sort_values('Total pedido', ascending=True).head(3)
        
        peor_producto = datos.iloc[0]
        valor_peor = peor_producto['Total pedido']
        promedio_general = df_pedidos.groupby('Producto')['Total pedido'].sum().mean()
        brecha = ((promedio_general - valor_peor) / promedio_general) * 100
        
        respuesta = f"""
        **📉 Productos Menos Vendidos**
        
        El producto con menor desempeño es **{peor_producto['Producto']}** con:
        • Cantidad vendida: {peor_producto['cantidad']:,.0f} unidades
        • Valor facturado: ${valor_peor:,.2f}
        • Brecha vs promedio: {brecha:.1f}% por debajo
        
        **📊 Análisis:**
        Estos productos representan oportunidades de mejora. Su baja facturación puede deberse a:
        - Falta de demanda del mercado
        - Problemas de calidad o presentación
        - Desconocimiento del cliente
        - Precios no competitivos
        
        **💡 Recomendaciones Estratégicas:**
        1. **Revisar Rentabilidad**: Verifique si estos productos son rentables o están perdiendo dinero
        2. **Discontinuar o Reformular**: Considere retirar productos no rentables o mejorar su propuesta
        3. **Ajuste de Precios**: Intente descuentos estratégicos para estimular demanda
        4. **Bundle Estratégico**: Combine con productos exitosos para impulsar ventas
        """
        return respuesta
    
    def obtener_analisis_proveedores_principales():
        """Análisis de proveedores principales"""
        datos_facturaciones = df_facturacion.groupby('nombre_proveedor').agg({
            'numero_factura': 'count',
            'valor_total $': 'sum'
        }).reset_index().rename(columns={
            'numero_factura': 'total_facturas',
            'valor_total $': 'valor_total'
        }).sort_values('valor_total', ascending=False).head(5)
        
        proveedor_top = datos_facturaciones.iloc[0]
        total_valor_empresa = df_facturacion['valor_total $'].sum()
        concentracion_proveedor = (proveedor_top['valor_total'] / total_valor_empresa) * 100
        
        respuesta = f"""
        **🏭 Proveedores Principales**
        
        Tu proveedor estratégico es **{proveedor_top['nombre_proveedor']}**:
        • Número de facturaciones: {proveedor_top['total_facturas']:.0f}
        • Valor facturado: ${proveedor_top['valor_total']:,.2f}
        • % del total de compras: {concentracion_proveedor:.1f}%
        
        **📊 Análisis:**
        Tu empresa tiene {len(datos_facturaciones)} proveedores principales. La concentración del {concentracion_proveedor:.1f}% 
        indica dependencia en este proveedor. Esto puede ser positivo (relación consolidada) o 
        riesgoso (vulnerabilidad si hay problemas con el proveedor).
        
        **💡 Recomendaciones Estratégicas:**
        1. **Fortalecer Relaciones**: Negocie contratos a largo plazo con proveedores clave para mejores términos
        2. **Diversificación**: Busque proveedores alternativos para reducir riesgo
        3. **Evaluación Periódica**: Revise calidad, plazos y precios regularmente
        4. **Alianzas Estratégicas**: Considere acuerdos de volumen discounted con proveedores principales
        5. **Contingentes**: Tenga proveedores de respaldo en caso de disrupciones
        """
        return respuesta
    
    def obtener_analisis_facturas_pendientes():
        """Análisis de facturas pendientes"""
        total_pendiente = df_facturacion[df_facturacion['estado_factura'] == 'Pendiente']['valor_total $'].sum()
        cantidad_pendientes = len(df_facturacion[df_facturacion['estado_factura'] == 'Pendiente'])
        valor_total = df_facturacion['valor_total $'].sum()
        porcentaje_pendiente = (total_pendiente / valor_total) * 100
        
        pendientes_por_proveedor = df_facturacion[df_facturacion['estado_factura'] == 'Pendiente'].groupby('nombre_proveedor')['valor_total $'].sum().sort_values(ascending=False).head(3)
        
        pendientes_por_responsable = df_facturacion[df_facturacion['estado_factura'] == 'Pendiente'].groupby('responsable')['numero_factura'].count().sort_values(ascending=False).head(3)
        
        respuesta = f"""
        **⏳ Facturas Pendientes de Pago**
        
        Estado actual de cartera:
        • Total pendiente: ${total_pendiente:,.2f}
        • Número de facturas: {cantidad_pendientes:,.0f}
        • % del total facturado: {porcentaje_pendiente:.1f}%
        • Salud financiera: {"🟢 SALUDABLE" if porcentaje_pendiente < 30 else "🟡 MODERADO" if porcentaje_pendiente < 70 else "🔴 CRÍTICO"}
        
        **Top Proveedores con Cartera Pendiente:**
        """
        for i, (proveedor, valor) in enumerate(pendientes_por_proveedor.items(), 1):
            respuesta += f"\n{i}. {proveedor}: ${valor:,.2f}"
        
        respuesta += f"""
        
        **📊 Análisis:**
        Un {porcentaje_pendiente:.1f}% de cartera pendiente {"es saludable" if porcentaje_pendiente < 30 else "requiere atención" if porcentaje_pendiente < 70 else "es crítico"}.
        Esta situación afecta:
        - **Cashflow**: Dinero bloqueado que podría usarse en otras operaciones
        - **Riesgo crediticio**: Posibilidad de incobrables
        - **Capacidad operativa**: Limitación para nuevas inversiones
        
        **💡 Recomendaciones Estratégicas:**
        1. **Gestión Activa**: Implemente seguimiento diario de cartera pendiente
        2. **Políticas de Pago**: Establezca términos claros y sanciones por retraso
        3. **Cobranza**: Asigne responsables específicos para seguimiento
        4. **Descuentos**: Ofrezca incentivos por pronto pago
        5. **Reasignación**: Revise responsables con muchas facturas pendientes
        """
        return respuesta
    
    def obtener_analisis_categorias():
        """Análisis de categorías principales"""
        datos_categoria = df_facturacion.groupby('categoria')['valor_total $'].sum().reset_index().sort_values('valor_total $', ascending=False)
        total_facturado = datos_categoria['valor_total $'].sum()
        datos_categoria['porcentaje'] = (datos_categoria['valor_total $'] / total_facturado) * 100
        
        top_categoria = datos_categoria.iloc[0]
        
        respuesta = f"""
        **📂 Categorías Principales y Aporte**
        
        **Top 3 Categorías por Valor Facturado:**
        """
        for i in range(min(3, len(datos_categoria))):
            row = datos_categoria.iloc[i]
            respuesta += f"\n{i+1}. **{row['categoria']}**: ${row['valor_total $']:,.2f} ({row['porcentaje']:.1f}%)"
        
        respuesta += f"""
        
        **📊 Análisis:**
        La categoría '{top_categoria['categoria']}' representa el {top_categoria['porcentaje']:.1f}% del negocio.
        La diversificación por categoría es: {"buena" if datos_categoria.iloc[0]['porcentaje'] < 40 else "concentrada" if datos_categoria.iloc[0]['porcentaje'] < 60 else "muy concentrada"}.
        
        **Implicaciones Financieras:**
        - **Riesgo de mercado**: Cambios en una categoría afectan significativamente el resultado
        - **Oportunidades**: Categorías emergentes pueden generar crecimiento
        - **Seasonal**: Algunas categorías pueden tener patrones estacionales
        
        **💡 Recomendaciones Estratégicas:**
        1. **Análisis de Márgenes**: Verifique rentabilidad de cada categoría
        2. **Especialización**: Fortalezca categorías rentables
        3. **Innovación**: Desarrolle nuevas categorías para diversificar riesgos
        4. **Pricing Estratégico**: Ajuste precios según demanda de cada categoría
        5. **Mix Óptimo**: Intente conseguir 30-30-30-10 en distribución de categorías
        """
        return respuesta
    
    def obtener_analisis_promedios():
        """Análisis de promedios de facturación"""
        valor_facturado_total = df_facturacion['valor_total $'].sum()
        promedio_factura = df_facturacion['valor_total $'].mean()
        
        facturas_por_mes = df_facturacion.copy()
        facturas_por_mes['year_month'] = facturas_por_mes['fecha_factura'].dt.to_period('M')
        promedio_facturas_por_mes = facturas_por_mes.groupby('year_month')['numero_factura'].count().mean()
        
        por_anio = facturas_por_mes.groupby(facturas_por_mes['fecha_factura'].dt.year).agg({
            'numero_factura': 'count',
            'valor_total $': 'sum'
        }).reset_index()
        por_anio.columns = ['anio', 'total_facturas', 'valor_total']
        
        respuesta = f"""
        **💰 Promedios de Facturación**
        
        **Métricas Generales:**
        • Valor total facturado: ${valor_facturado_total:,.2f}
        • Promedio por factura: ${promedio_factura:,.2f}
        • Promedio de facturas por mes: {promedio_facturas_por_mes:.0f}
        
        **Facturación por Año:**
        """
        for row in por_anio.itertuples():
            valor_promedio_anio = row.valor_total / row.total_facturas if row.total_facturas > 0 else 0
            respuesta += f"\n• **{row.anio}**: {row.total_facturas:.0f} facturas | ${row.valor_total:,.2f} (Promedio: ${valor_promedio_anio:,.2f})"
        
        tendencia = "📈 En crecimiento" if por_anio.iloc[-1]['valor_total'] > por_anio.iloc[0]['valor_total'] else "📉 En decline"
        
        respuesta += f"""
        
        **Tendencia General:** {tendencia}
        
        **📊 Análisis:**
        El promedio de ${promedio_factura:,.2f} por factura es tu ticket promedio.
        La consistencia de facturas por mes ({promedio_facturas_por_mes:.0f}) indica la velocidad de operación.
        
        **Implicaciones para el Negocio:**
        - **Predictibilidad**: Permite proyectar ingresos y recursos
        - **Capacidad**: Ayuda a dimensionar equipo y operaciones
        - **Eficiencia**: Facturas más altas = mejor eficiencia administrativa
        
        **💡 Recomendaciones Estratégicas:**
        1. **Aumentar Ticket Promedio**: Negocie contratos de mayor valor  
        2. **Acelerar Rotación**: Incremente cantidad de facturas haciendo procesos más eficientes
        3. **Consolidación**: Agrupe múltiples pedidos en menos facturas para ahorrar en administración
        4. **Automatización**: Automatice para manejar más facturas sin aumentar costos
        5. **Proyección**: Use promedios para planificar capital de trabajo
        """
        return respuesta
    
    def responder_pregunta_general(pregunta):
        """Responde preguntas generales sobre la salud de la empresa"""
        salud_porcentaje = (df_total_pendiente_por_anio['total_pendiente'].sum() / total_valor_facturado) * 100 if total_valor_facturado > 0 else 0
        
        respuesta = f"""
        **📋 Estado General de la Empresa**
        
        **KPIs Principales:**
        • Total de proveedores: {total_proveedores_unicos}
        • Productos únicos: {total_productos_unicos}
        • Total facturaciones: {total_facturaciones}
        • Valor total facturado: ${total_valor_facturado:,.2f}
        • Cartera pendiente: {salud_porcentaje:.1f}% (${df_total_pendiente_por_anio['total_pendiente'].sum():,.2f})
        • Estado: {"🟢 SALUDABLE" if salud_porcentaje < 30 else "🟡 MODERADO" if salud_porcentaje < 70 else "🔴 CRÍTICO"}
        
        **📊 Análisis Integral:**
        Tu empresa tiene un modelo de negocio basado en {total_productos_unicos} productos distribuidos a {total_proveedores_unicos} proveedores.
        La facturación de ${total_valor_facturado:,.2f} distribuida en {total_facturaciones} facturas muestra 
        un ticket promedio de ${total_valor_facturado/total_facturaciones:,.2f}.
        
        **💡 Prioridades Estratégicas:**
        1. **Urgente**: Gestionar cartera pendiente (${df_total_pendiente_por_anio['total_pendiente'].sum():,.2f})
        2. **Importante**: Diversificar productos y proveedores
        3. **Mejora**: Aumentar ticket promedio y velocidad de facturación
        4. **Innovación**: Explorar nuevas categorías y clientes
        5. **Sostenibilidad**: Fortalecer relaciones clave con múltiples alternativas
        """
        return respuesta
    
    # ==================== INTERFAZ DEL CHATBOT ====================
    
    # Inicializar historial de chat en session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "last_processed" not in st.session_state:
        st.session_state.last_processed = -1
    
    # Mostrar historial del chat primero
    st.subheader("📞 Conversación")
    
    # Contenedor para mostrar el chat
    chat_container = st.container()
    
    with chat_container:
        for i, message in enumerate(st.session_state.chat_history):
            if message["role"] == "user":
                st.write(f"**👤 Tú:** {message['message']}")
            else:
                st.write(message["message"])
                st.divider()
    
    # Sección de entrada
    st.subheader("💬 Haz tu pregunta")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_input = st.text_input(
            "Pregunta sobre análisis financiero:",
            placeholder="Ej: ¿Cuáles son nuestros productos más vendidos?",
            key="user_query"
        )
    
    with col2:
        send_button = st.button("📤 Enviar", use_container_width=True)
    
    # Procesar entrada del usuario
    if send_button and user_input.strip():
        user_message = user_input.lower()
        st.session_state.chat_history.append({"role": "user", "message": f"**Pregunta:** {user_input}"})
        
        # Determinar tema y generar respuesta
        if "producto" in user_message and ("más" in user_message or "top" in user_message or "mayor" in user_message or "vend" in user_message):
            respuesta = obtener_analisis_productos_mas_vendidos()
        elif "producto" in user_message and ("menos" in user_message or "bajo" in user_message or "menor" in user_message):
            respuesta = obtener_analisis_productos_menos_vendidos()
        elif "proveedor" in user_message:
            respuesta = obtener_analisis_proveedores_principales()
        elif ("cartera" in user_message or "pendiente" in user_message or "cobrar" in user_message or "deuda" in user_message or "pago" in user_message):
            respuesta = obtener_analisis_facturas_pendientes()
        elif "categor" in user_message:
            respuesta = obtener_analisis_categorias()
        elif "promedio" in user_message or ("factura" in user_message and "mes" in user_message):
            respuesta = obtener_analisis_promedios()
        else:
            respuesta = responder_pregunta_general(user_message)
        
        st.session_state.chat_history.append({"role": "assistant", "message": respuesta})
        st.rerun()
    
    # Mostrar sugerencias rápidas
    st.divider()
    st.write("**💡 Preguntas sugeridas - Haz clic para explorar:**")
    
    sugerencias = [
        ("🏆 Productos Top", "¿Cuáles son nuestros productos más vendidos?"),
        ("📉 Productos Bajos", "¿Cuáles son nuestros productos menos vendidos?"),
        ("🏭 Proveedores", "¿Quiénes son nuestros proveedores principales?"),
        ("⏳ Cartera Pendiente", "¿Cómo está nuestra cartera pendiente?"),
        ("📂 Categorías", "¿Cómo se distribuye nuestro negocio por categorías?"),
        ("💰 Promedios", "¿Cuál es el promedio de facturación?"),
        ("📊 Salud General", "¿Cuál es el estado general de la empresa?"),
        ("💡 Recomendaciones", "¿Qué recomendaciones estratégicas tiene?")
    ]
    
    # Crear botones de sugerencias rápidas en columnas
    cols = st.columns(4)
    for idx, (label, sugerencia) in enumerate(sugerencias):
        col_idx = idx % 4
        with cols[col_idx]:
            if st.button(label, key=f"sugerencia_{idx}", use_container_width=True):
                # Agregar pregunta al historial
                st.session_state.chat_history.append({"role": "user", "message": f"**Pregunta:** {sugerencia}"})
                
                # Generar respuesta según el tipo de sugerencia
                user_message = sugerencia.lower()
                if "producto" in user_message and ("más" in user_message or "top" in user_message):
                    respuesta = obtener_analisis_productos_mas_vendidos()
                elif "producto" in user_message and ("menos" in user_message):
                    respuesta = obtener_analisis_productos_menos_vendidos()
                elif "proveedor" in user_message:
                    respuesta = obtener_analisis_proveedores_principales()
                elif "cartera" in user_message or "pendiente" in user_message:
                    respuesta = obtener_analisis_facturas_pendientes()
                elif "categor" in user_message:
                    respuesta = obtener_analisis_categorias()
                elif "promedio" in user_message:
                    respuesta = obtener_analisis_promedios()
                else:
                    respuesta = responder_pregunta_general(user_message)
                
                st.session_state.chat_history.append({"role": "assistant", "message": respuesta})
                st.rerun()

else:
    st.header("🏢 Bienvenido al Dashboard de Facturación Interactivo")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #6a0dad, #1f77b4); color: white; padding: 30px; border-radius: 15px; text-align: center; font-family: 'Helvetica Neue', sans-serif; box-shadow: 0px 4px 15px rgba(0,0,0,0.3);">
        <h2 style="color: #ff7f0e; margin-bottom: 20px;">Descubre Insights Poderosos para tu Empresa</h2>
        <p style="font-size: 18px; line-height: 1.6;">
            Explora análisis detallados de <strong>productos</strong>, <strong>proveedores</strong> y <strong>facturaciones</strong> con gráficos interactivos que te permiten identificar tendencias, optimizar procesos y tomar decisiones estratégicas. 
            Monitorea facturas pendientes, evalúa la salud financiera de tu empresa y accede a métricas clave en tiempo real. 
            ¡Transforma datos en oportunidades de crecimiento!
        </p>
        <p style="font-size: 16px; margin-top: 20px;">
            <em>Desarrollado por: Maria Alejandra Florez, Biviana Andrea Vanegas Salazar, Jose Andres Diaz Gutierrez, Paula Andrea Fernandez Castaño</em>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.write("Selecciona una opción del menú lateral para explorar los datos.")

