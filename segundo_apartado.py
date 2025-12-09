import streamlit as st
import numpy as np
 
# --- CSS PERSONALIZADO (Para simular una calculadora y cambiar fuente) ---
st.markdown("""
<style>
/* 1. Cambiar la fuente principal de la app */
.main {
    font-family: 'Georgia', serif; /* Fuente más clásica */
    background-color: #f0f2f6; /* Fondo gris claro */
}
 
/* 2. Estilo para simular el recuadro de la calculadora */
.calculator-box {
    padding: 20px;
    border: 3px solid #3498db; /* Borde azul */
    border-radius: 15px; /* Esquinas redondeadas */
    background-color: #ffffff; /* Fondo blanco para contraste */
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1); /* Sombra sutil */
    margin-bottom: 20px;
}
 
/* 3. Estilo para el botón */
.stButton>button {
    background-color: #2ecc71; /* Color verde */
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
}

/* 4. Estilo para los títulos (opcional) */
h1 {
    color: #2c3e50;
}
</style>
""", unsafe_allow_html=True)
 
st.title("🧮 Calculadora Estadística Avanzada")
 
# Creamos las pestañas
tab1, tab2, tab3 = st.tabs(["Ingreso de Datos", "Análisis Estadístico", "Acerca de"])
 
# ---
# PESTAÑA 1: INGRESO DE DATOS (Con estilo de calculadora)
# ---
with tab1:
    st.header("🔢 Carga de Datos")
 
    # Usamos un contenedor de Streamlit para aplicar el CSS de "calculator-box"
    st.markdown('<div class="calculator-box">', unsafe_allow_html=True)
    
    st.subheader("Ingreso de la Muestra")
    st.write("Introduce una lista de números separados por **comas** (ej: 10.5, 20, 15.2).")
 
    data_input = st.text_area(
        "Datos Numéricos:", 
        height=150,
        placeholder="Ejemplo: 10, 20, 15, 30, 25"
    )
 
    # Usamos st.columns para centrar o dar espacio al botón
    col_btn, col_spacer = st.columns([1, 4])
    
    with col_btn:
        if st.button("📊 Analizar Datos"):
            try:
                # Convertir texto a lista numérica
                data = [float(x.strip()) for x in data_input.split(",") if x.strip()] # Asegura que no falle en entradas vacías
 
                if not data:
                    st.error("Error: La lista de datos está vacía.")
                    st.session_state["datos"] = []
                    
                else:
                    st.success("✅ Datos cargados correctamente.")
                    st.info(f"Tamaño de la muestra: **{len(data)}**") 
                    st.write(f"Primeros 5 valores cargados: '{data[:5]}'")
                    
                    # Guardamos los datos para usarlos en otras pestañas
                    st.session_state["datos"] = data
 
            except ValueError:
                st.error("❌ Error: Asegúrate de que todos los valores sean números válidos separados por comas.")
            except Exception:
                st.error("Error desconocido al procesar los datos.")
                
    st.markdown('</div>', unsafe_allow_html=True)
 
# ---
# PESTAÑA 2: ESTADÍSTICOS (Con columnas para mejor visualización)
# ---
with tab2:
    st.header("📈 Resultados Estadísticos Clave")
 
    if "datos" in st.session_state and st.session_state["datos"]:
        data = st.session_state["datos"]
        
        # Usar contenedores y columnas para una mejor presentación
        st.subheader("Medidas de Tendencia Central y Dispersión")
        
        # Calcular estadísticos
        media = np.mean(data)
        mediana = np.median(data)
        desviacion = np.std(data, ddof=1)
        varianza = np.var(data, ddof=1)
        minimo = np.min(data)
        maximo = np.max(data)
        rango = maximo - minimo
 
        # Fila 1: Centralización
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric("Promedio (Media)", f"{media:.4f}")
        with col_m2:
            st.metric("Valor Central (Mediana)", f"{mediana:.4f}")
            
        st.divider()
        
        # Fila 2: Dispersión
        st.subheader("Medidas de Variabilidad")
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.metric("Desviación Estándar (Muestral)", f"{desviacion:.4f}")
        with col_d2:
            st.metric("Varianza (Muestral)", f"{varianza:.4f}")

        st.divider()

        # Fila 3: Posición
        st.subheader("Medidas de Posición")
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            st.metric("Mínimo", f"{minimo:.4f}")
        with col_p2:
            st.metric("Máximo", f"{maximo:.4f}")
        with col_p3:
            st.metric("Rango", f"{rango:.4f}")
 
    else:
        st.warning("⚠️ Primero ingresa y carga los datos en la pestaña **'Ingreso de Datos'** para ver los resultados.")
 
# ---
# PESTAÑA 3: ACERCA DE
# ---
with tab3:
    st.header("💡 Información de la Aplicación")
    
    st.info("""
    Esta aplicación fue desarrollada en **Python** utilizando la librería **Streamlit** para el despliegue web y **NumPy** para el cálculo eficiente de las funciones estadísticas.
    """)
 
    st.subheader("Funcionalidades Clave")
    st.markdown("""
    * **Entrada Flexible:** Acepta datos numéricos separados por comas.
    * **Medidas Centrales:** Cálculo de **Media** y **Mediana**.
    * **Medidas de Dispersión:** Cálculo de **Desviación Estándar** y **Varianza** (ambas muestrales, usando `ddof=1`).
    * **Medidas de Posición:** Muestra el **Mínimo**, **Máximo** y el **Rango**.
    * **Diseño Intuitivo:** Usa pestañas y contenedores para una mejor experiencia de usuario (UX).
    """)
 
