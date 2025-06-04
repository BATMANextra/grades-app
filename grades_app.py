import streamlit as st

st.title("🎓 Student Grade Calculator")

def weighted_avg(td=None, tp=None, exam=None):
    if td is not None and tp is not None:
        return ((td + tp) / 2) * 0.4 + exam * 0.6
    elif td is not None:
        return td * 0.4 + exam * 0.6
    else:
        return tp * 0.4 + exam * 0.6

td_algo = st.number_input("TD Algorithmique ", min_value=0.0)
tp_algo = st.number_input("TP Algorithmique ", min_value=0.0)
exmn_algo = st.number_input("Exam Algorithmique ", min_value=0.0)
note_algo = weighted_avg(td_algo, tp_algo, exmn_algo)
st.write("Note Algorithmique:", note_algo)

td_vereficaton = st.number_input("TD Vérification", min_value=0.0)
exmn_vereficaton = st.number_input("Exam Vérification", min_value=0.0)
note_vereficaton = weighted_avg(td_vereficaton, None, exmn_vereficaton)
st.write("Note Vérification:", note_vereficaton)

tp_network = st.number_input("TP Réseaux sans-fil", min_value=0.0)
exmn_network = st.number_input("Exam Réseaux sans-fil", min_value=0.0)
note_network = weighted_avg(None, tp_network, exmn_network)
st.write("Note Réseaux sans-fil:", note_network)

tp_projet_SE = st.number_input("TP Projets systèmes embarqués", min_value=0.0)
exmn_projet_SE = st.number_input("Exam Projets systèmes embarqués", min_value=0.0)
note_projet_SE = weighted_avg(None, tp_projet_SE, exmn_projet_SE)
st.write("Note Projets systèmes embarqués:", note_projet_SE)

tp_modiliation = st.number_input("TP Modélisation et simulation", min_value=0.0)
exmn_modiliation = st.number_input("Exam Modélisation et simulation", min_value=0.0)
note_modiliation = weighted_avg(None, tp_modiliation, exmn_modiliation)
st.write("Note MModélisation et simulation:", note_modiliation)

tp_vision = st.number_input("TP vision artificielle", min_value=0.0)
exmn_vision = st.number_input("Exam vision artificielle", min_value=0.0)
note_vison = weighted_avg(None, tp_vision, exmn_vision)
st.write("Note vision artificielle:", note_vison)

Devlompnt = st.number_input("Exam Développement M/L", min_value=0.0)
anglais = st.number_input("Exam Anglais 2", min_value=0.0)
expression = st.number_input("Exam Techniques d'expression 2", min_value=0.0)
legilastion = st.number_input("Exam Législation", min_value=0.0)

if st.button("Calculate Moyenne"):
    moy = (note_algo*2 + note_vereficaton*3 + note_network*2 + note_projet_SE*2 +
           note_modiliation*2 + note_vison*2 + anglais + expression + Devlompnt + legilastion) / 17
    st.success(f"✅ Moyenne: {round(moy, 2)}")
