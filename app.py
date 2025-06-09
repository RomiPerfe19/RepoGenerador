import streamlit as st

def generar_descripcion(nombre, estilo, beneficio, cliente_objetivo):
    if estilo.lower() == "cercano":
        return (
            f"¿Buscás algo especial? Nuestra {nombre} es ideal para vos. "
            f"{beneficio}. Pensada especialmente para {cliente_objetivo}, con mucho amor 💛."
        )
    elif estilo.lower() == "profesional":
        return (
            f"Presentamos la {nombre}: una solución diseñada para {cliente_objetivo}. "
            f"{beneficio}. Calidad y confianza garantizadas."
        )
    elif estilo.lower() == "creativo":
        return (
            f"¡Dale vida a tu día con la {nombre}! {beneficio} en cada detalle. "
            f"Creada para {cliente_objetivo}, con una chispa única ✨."
        )
    else:
        return (
            f"La {nombre} es perfecta para {cliente_objetivo}. {beneficio}."
        )

# --- Interfaz Streamlit ---
st.set_page_config(page_title="Generador de descripciones", page_icon="📝")
st.title("📝 Generador de descripciones de productos")

nombre = st.text_input("🧸 Nombre del producto")
estilo = st.selectbox("🎨 Estilo de redacción", ["cercano", "profesional", "creativo"])
beneficio = st.text_input("✅ Beneficio principal")
cliente_objetivo = st.text_input("👥 ¿Para quién es?")

if st.button("✍️ Generar descripción"):
    if nombre and beneficio and cliente_objetivo:
        descripcion = generar_descripcion(nombre, estilo, beneficio, cliente_objetivo)
        st.success("Descripción generada:")
        st.write(descripcion)
    else:
        st.warning("Por favor, completá todos los campos.")

