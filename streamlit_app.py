import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# ================================
# TITRE DE L'APPLICATION
# ================================
st.title("🎓 Prédiction du Décrochage Scolaire")
st.write("Entrez le profil d'un étudiant pour savoir s'il risque de décrocher.")
st.markdown("---")

# ================================
# CHARGEMENT DU MODÈLE
# ================================
@st.cache_resource
def charger_modele():
    df = pd.read_csv("data/dataset.csv")
    df_model = df.copy()
    le = LabelEncoder()
    df_model["Target"] = le.fit_transform(df_model["Target"])
    X = df_model.drop("Target", axis=1)
    y = df_model["Target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    return rf, le, X.columns.tolist()

rf, le, colonnes = charger_modele()

# ================================
# FORMULAIRE DE SAISIE
# ================================
st.subheader("📋 Profil de l'étudiant")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Âge à l'inscription", 17, 60, 20)
    bourse = st.selectbox("Bénéficie d'une bourse ?", [0, 1],
                          format_func=lambda x: "Oui" if x == 1 else "Non")
    dette = st.selectbox("A des dettes ?", [0, 1],
                         format_func=lambda x: "Oui" if x == 1 else "Non")
    frais = st.selectbox("Frais de scolarité à jour ?", [0, 1],
                         format_func=lambda x: "Oui" if x == 1 else "Non")

with col2:
    notes_s1 = st.slider("Moyenne au 1er semestre", 0.0, 20.0, 12.0)
    notes_s2 = st.slider("Moyenne au 2ème semestre", 0.0, 20.0, 12.0)
    validees_s1 = st.slider("Matières validées au 1er semestre", 0, 10, 5)
    validees_s2 = st.slider("Matières validées au 2ème semestre", 0, 10, 5)

# ================================
# PRÉDICTION
# ================================
st.markdown("---")

if st.button("🔍 Analyser le profil", use_container_width=True):

    # Créer un profil moyen et remplacer les valeurs saisies
    df_base = pd.read_csv("data/dataset.csv")
    profil = df_base.drop("Target", axis=1).mean().to_dict()

    profil["Age at enrollment"] = age
    profil["Scholarship holder"] = bourse
    profil["Debtor"] = dette
    profil["Tuition fees up to date"] = frais
    profil["Curricular units 1st sem (grade)"] = notes_s1
    profil["Curricular units 2nd sem (grade)"] = notes_s2
    profil["Curricular units 1st sem (approved)"] = validees_s1
    profil["Curricular units 2nd sem (approved)"] = validees_s2

    X_profil = pd.DataFrame([profil])[colonnes]

    # Prédiction
    prediction = rf.predict(X_profil)[0]
    probabilites = rf.predict_proba(X_profil)[0]

    # Résultat
    statuts = ["❌ Risque de Décrochage", "📚 Encore Inscrit", "🎓 Diplômé"]
    couleurs = ["#FF4B4B", "#FFA500", "#00C851"]

    st.subheader("📊 Résultat de l'analyse")

    if prediction == 0:
        st.error(f"**{statuts[0]}**")
        st.write("⚠️ Cet étudiant présente un risque élevé de décrochage.")
        st.write("**Conseils :** Vérifier les notes, proposer un soutien financier, mettre en place un suivi personnalisé.")
    elif prediction == 1:
        st.warning(f"**{statuts[1]}**")
        st.write("👀 Cet étudiant est encore inscrit mais nécessite une attention.")
    else:
        st.success(f"**{statuts[2]}**")
        st.write("✅ Cet étudiant a un bon profil pour terminer ses études.")

    # Probabilités
    st.markdown("---")
    st.subheader("📈 Probabilités détaillées")

    labels = ["Décrochage", "Encore inscrit", "Diplômé"]
    for i, (label, prob) in enumerate(zip(labels, probabilites)):
        st.write(f"**{label}**")
        st.progress(float(prob))
        st.write(f"{prob*100:.1f}%")