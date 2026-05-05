# 🎓 Prédiction du Décrochage Scolaire — Modèle ML

> **Projet Data Science** | Classification ML · Interprétabilité SHAP · Démo interactive Streamlit

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Demo-red?logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🎯 Problème

Chaque année, des millions d'étudiants abandonnent leurs études sans diplôme. En Afrique subsaharienne, le taux de décrochage dans l'enseignement supérieur peut dépasser **30%**. Ce projet construit un modèle prédictif capable d'identifier **tôt** les étudiants à risque, avant qu'il ne soit trop tard pour intervenir.

---

## 📁 Structure du projet

```
dropout-prediction/
│
├── 📓 notebooks/
│   ├── 01_EDA.ipynb              # Analyse exploratoire complète
│   ├── 02_modelisation.ipynb     # Entraînement des modèles
│   └── 03_interpretabilite.ipynb # Analyse SHAP
│
├── 📊 src/
│   ├── eda_decrochage.py         # Script EDA principal
│   ├── preprocessing.py          # Nettoyage & feature engineering
│   ├── models.py                 # Entraînement & évaluation
│   └── shap_analysis.py          # Interprétabilité
│
├── 🌐 app/
│   └── streamlit_app.py          # Démo interactive
│
├── 📈 outputs/
│   └── figures/                  # Visualisations générées
│
├── requirements.txt
└── README.md
```

---

## 🗃️ Dataset

**Source** : [UCI Machine Learning Repository — Students Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

| Variable | Description |
|---|---|
| `Age at enrollment` | Âge de l'étudiant à l'inscription |
| `Gender` | Genre (0 = Femme, 1 = Homme) |
| `Admission grade` | Note d'admission |
| `Curricular units Xst sem (grade)` | Moyenne semestrielle |
| `Scholarship holder` | Bénéficiaire d'une bourse |
| `GDP`, `Unemployment rate` | Contexte socio-économique |
| **`Target`** | **Graduate / Dropout / Enrolled** |

---

## 🤖 Modèles testés

| Modèle | AUC-ROC | F1-Score (Dropout) |
|---|---|---|
| Régression Logistique | — | — |
| Random Forest | — | — |
| **XGBoost** ✅ | — | — |

*Les métriques seront mises à jour au fur et à mesure de l'avancement.*

---

## 🔍 Interprétabilité (SHAP)

Le modèle final sera expliqué avec **SHAP** pour identifier les facteurs qui pèsent le plus sur le risque de décrochage.

---

## 🚀 Installation & Lancement

```bash
# 1. Cloner le projet
git clone https://github.com/[ton-username]/dropout-prediction.git
cd dropout-prediction

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'EDA
python src/eda_decrochage.py

# 4. Lancer la démo Streamlit
streamlit run app/streamlit_app.py
```

---

## 📦 Dépendances

```txt
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
plotly>=5.15
scikit-learn>=1.3
xgboost>=1.7
imbalanced-learn>=0.11
shap>=0.42
streamlit>=1.28
```

---

## 👩‍💻 Auteure

**[Ton Nom]** — Statisticienne & Data Analyst | Master en Statistiques

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connecter-blue?logo=linkedin)](https://linkedin.com/in/[ton-profil])
[![Kaggle](https://img.shields.io/badge/Kaggle-Profil-20BEFF?logo=kaggle&logoColor=white)](https://kaggle.com/[ton-profil])

---

## 📄 Licence

MIT — libre d'utilisation avec attribution.
