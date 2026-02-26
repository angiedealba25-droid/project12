import streamlit as st
from datetime import datetime, timedelta

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Dashboard Quirófano - Keralty",
    page_icon="🏥",
    layout="wide"
)

# --------- ESTILOS PERSONALIZADOS ----------
st.markdown("""
<style>

body {
    background-color: #f4f8fb;
}

.header {
    background: linear-gradient(90deg, #00b4d8, #0077b6);
    padding: 20px;
    border-radius: 12px;
    color: white;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

.card {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
    text-align: center;
}

.number {
    font-size: 48px;
    font-weight: bold;
    background: linear-gradient(90deg, #03045e, #0077b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.label {
    font-size: 18px;
    color: #0077b6;
    margin-bottom: 10px;
    font-weight: 600;
}

.status-ok {
    font-size: 40px;
    font-weight: bold;
    color: #00b4d8;
}

.status-delay {
    font-size: 40px;
    font-weight: bold;
    color: red;
}

.footer {
    text-align: center;
    margin-top: 30px;
    color: #0077b6;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown('<div class="header">🏥 QUIRÓFANO 3 - KERALTY S.A</div>', unsafe_allow_html=True)

# -------- LOGO (Cambia por tu ruta local si quieres imagen real) --------
st.markdown("<br>", unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Keralty_logo.svg/2560px-Keralty_logo.svg.png", width=200)

st.markdown("<br><br>", unsafe_allow_html=True)

# -------- INPUT DINÁMICO --------
col1, col2 = st.columns(2)

with col1:
    hora_inicio = st.time_input("Hora Inicio Cirugía", value=datetime.now().time())

with col2:
    duracion_estimada = st.number_input("Duración estimada (minutos)", min_value=30, max_value=600, value=90)

# -------- CÁLCULOS --------
fecha_actual = datetime.now().date()
inicio_datetime = datetime.combine(fecha_actual, hora_inicio)
hora_fin_estimada = inicio_datetime + timedelta(minutes=duracion_estimada)
hora_actual = datetime.now()

atraso = hora_actual > hora_fin_estimada

# -------- TARJETAS --------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <div class="label">Hora Inicio</div>
        <div class="number">{}</div>
    </div>
    """.format(inicio_datetime.strftime("%H:%M:%S")), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="label">Quirófano</div>
        <div class="number">3</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="label">Hora Estimada Fin</div>
        <div class="number">{}</div>
    </div>
    """.format(hora_fin_estimada.strftime("%H:%M:%S")), unsafe_allow_html=True)

with col4:
    if atraso:
        st.markdown("""
        <div class="card">
            <div class="label">Estado Cirugía</div>
            <div class="status-delay">ATRASADO</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card">
            <div class="label">Estado Cirugía</div>
            <div class="status-ok">A TIEMPO</div>
        </div>
        """, unsafe_allow_html=True)

# -------- FOOTER --------
st.markdown('<div class="footer">Sistema Inteligente de Control Quirúrgico - Keralty S.A</div>', unsafe_allow_html=True)
