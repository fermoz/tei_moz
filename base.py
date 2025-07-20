import streamlit as st
from PIL import Image

# Simulación de base de usuarios
USUARIOS = {
    "admin": "clave123",
    "tecnico": "moz2025"
}

# Simulación de proyectos
PROYECTOS = [
    "Reforma del sistema educativo rural en Zambezia",
    "Ampliación de energía solar en escuelas comunitarias",
    "Programa de alfabetización digital para jóvenes",
    "Rehabilitación de manglares en la costa norte",
    "Instalación de mini-hidroeléctricas en Niassa",
    "Reducción de la deforestación en Inhambane",
    "Educación bilingüe en escuelas rurales",
    "Capacitación docente en métodos STEM",
    "Monitoreo satelital de áreas protegidas",
    "Expansión de red eléctrica sostenible en Cabo Delgado"
]

# Estilos CSS personalizados
st.markdown("""
    <style>
        body {
            font-family: 'Roboto', sans-serif;
        }
        .entrada {
            width: 25% !important;
            border-radius: 12px !important;
        }
        .boton {
            width: 25% !important;
        }
        .menu {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Función de autenticación
def autenticar(usuario, clave):
    return USUARIOS.get(usuario) == clave

# Layout de la pantalla de login
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("# TEIs Mozambique")
        logo = Image.open("EU.jpeg")  # ruta relativa a la carpeta donde está el logo
        st.image(logo, width=150)
    with col2:
        st.markdown("## Acceso al sistema")
        usuario = st.text_input("Usuario", key="user", label_visibility="collapsed", placeholder="Nombre de usuario")
        clave = st.text_input("Contraseña", type="password", key="pass", label_visibility="collapsed", placeholder="Contraseña")
        if st.button("Entrar"):
            if autenticar(usuario, clave):
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")

# Página principal tras login
else:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("### Menú")
        opcion = st.radio("", ["Analizar", "Actualizar", "Salir"])
        if opcion == "Salir":
            st.session_state.autenticado = False
            st.rerun()
    with col2:
        st.markdown("### Lista de proyectos")
        for proyecto in PROYECTOS:
            st.markdown(f"- {proyecto}")
