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
    st.markdown("""
        <style>
            .login-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 80vh;
            }
            .left-side {
                display: flex;
                align-items: center;
                margin-right: 60px;
            }
            .logo {
                width: 40px;
                margin-right: 10px;
            }
            .title {
                font-size: 2rem;
                font-weight: bold;
                color: #222;
                margin: 0;
            }
            .right-side {
                display: flex;
                flex-direction: column;
                gap: 10px;
                width: 220px;
            }
        </style>
        <div class="login-container">
            <div class="left-side">
                <img class="logo" src='https://raw.githubusercontent.com/fermoz/tei_moz/main/EU.jpg'>
                <p class="title">TEIs Mozambique</p>
            </div>
            <div class="right-side">
                <form action="#" method="post">
                    <input name="user" type="text" placeholder="Nombre de usuario" class="entrada" style="padding: 10px; border-radius: 10px; border: 1px solid #ccc;">
                    <input name="pass" type="password" placeholder="Contraseña" class="entrada" style="padding: 10px; border-radius: 10px; border: 1px solid #ccc;">
                    <button type="submit" class="boton" style="padding: 8px; border-radius: 8px;">Entrar</button>
                </form>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Inputs capturados con Streamlit
    usuario = st.text_input("", key="user_input", label_visibility="collapsed", placeholder="Nombre de usuario")
    clave = st.text_input("", key="pass_input", label_visibility="collapsed", type="password", placeholder="Contraseña")
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


