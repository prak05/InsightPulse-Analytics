import csv
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Smart Health App – CSD 334",
    page_icon="🩺",
    layout="wide",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
DATA = ROOT / "data"


def symptom_dataset_stats(path: Path):
    if not path.exists():
        return None
    rows = 0
    diseases = set()
    symptoms = set()
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows += 1
            diseases.add(row.get("disease", "").strip())
            for s in row.get("symptoms", "").split(","):
                s = s.strip()
                if s:
                    symptoms.add(s)
    diseases = {d for d in diseases if d}
    return {
        "rows": rows,
        "diseases": len(diseases),
        "symptoms": len(symptoms),
    }


def pima_dataset_stats(path: Path):
    if not path.exists():
        return None
    rows = 0
    cols = 0
    with path.open() as f:
        reader = csv.reader(f)
        for row in reader:
            rows += 1
            if cols == 0:
                cols = len(row)
    return {"rows": rows, "cols": cols}


def simple_dataset_stats(path: Path, key_col: str):
    if not path.exists():
        return None
    rows = 0
    unique_keys = set()
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows += 1
            val = row.get(key_col, "").strip()
            if val:
                unique_keys.add(val)
    return {"rows": rows, "unique": len(unique_keys)}

st.title("Smart Health App")
st.caption("CSD 334 (KTU) – Frontend Prototype")

st.markdown(
    """
This frontend is a **simple, neat** Streamlit prototype for a *Smart Health App* based on the SMA presentation and
supporting PDFs. It focuses on clear sections, light visuals, and placeholders for future data, models, and UI widgets.
"""
)

st.divider()

# Sidebar navigation
section = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Problem & Objectives",
        "Proposed System",
        "Dataset & Algorithms",
        "System Architecture",
        "Features & Future Enhancements",
        "References",
    ],
)

if section == "Overview":
    st.header("Overview")

    hero = ASSETS / "hero.svg"
    if hero.exists():
        st.image(str(hero), use_column_width=True)

    st.subheader("Definition – Smart Health App")
    st.markdown(
        """
A Smart Health App is designed to assist users in monitoring their health conditions and obtaining preliminary
medical guidance based on symptoms. It collects user health data (symptoms, vital signs, lifestyle information)
and provides health suggestions using rule-based logic and data analysis. The app acts as a support system and
is **not** a replacement for doctors.
"""
    )
    st.caption("Source: SMA.pdf – Abstract and Introduction")

    st.subheader("Definition – Intelligent Health Assistance App")
    st.markdown(
        """
An intelligent health assistance mobile application provides preliminary health guidance using user inputs such as
age, gender, symptoms, and location. It applies symptom-analysis logic to infer possible health conditions and
recommends nearby hospitals and doctors. It supports decision-making but does not replace professional medical
consultation.
"""
    )
    st.caption("Source: Smarthealthapp.pdf – Project Summary")

    st.subheader("Definition – Multi-Disease Prediction")
    st.markdown(
        """
A multi-disease prediction system uses machine-learning techniques to analyze medical data and predict diseases
such as diabetes, cancer, and heart disease. Example approaches include logistic regression for heart disease,
CNNs for cancer imaging, and SVM for diabetes prediction.
"""
    )
    st.caption(
        "Source: Intelligent-Disease-Diagnosis-A-Multi-Disease-Prediction-Approach-Using-Machine-Learning.pdf – Abstract"
    )

elif section == "Problem & Objectives":
    st.header("Problem Statement")
    st.markdown(
        """
- Delay in identifying health issues
- Limited access to medical advice in rural areas
- Manual health tracking is inefficient
- Lack of personalized health monitoring tools
"""
    )
    st.caption("Source: SMA.pdf – Problem Statement")

    st.header("Objectives")
    st.markdown(
        """
- Develop a mobile-based Smart Health application
- Analyze user symptoms and provide basic health suggestions
- Store and track user health history
- Improve early detection of health issues
- Promote health awareness among users
"""
    )
    st.caption("Source: SMA.pdf – Objectives")

elif section == "Proposed System":
    st.header("Proposed System")
    st.markdown(
        """
The Smart Health App provides:
- User registration and profile management
- Symptom input and analysis
- Health recommendations
- Medical reminders
- Health history storage

Advantages:
- Quick response
- User-friendly
- Accessible anytime, anywhere
"""
    )
    st.caption("Source: SMA.pdf – Proposed System")

    st.subheader("Symptom Input (Demo UI)")
    st.caption("This is a frontend demo only. It does not provide medical diagnosis.")

    with st.form("symptom_form"):
        c1, c2, c3 = st.columns(3)
        with c1:
            name = st.text_input("Name", placeholder="User name")
            age = st.number_input("Age", min_value=1, max_value=120, value=22)
            gender = st.selectbox("Gender", ["Female", "Male", "Other"])
        with c2:
            temperature = st.number_input("Body Temperature (°C)", min_value=34.0, max_value=42.0, value=36.8, step=0.1)
            pulse = st.number_input("Pulse (bpm)", min_value=40, max_value=160, value=78)
            bp = st.text_input("Blood Pressure", placeholder="e.g., 120/80")
        with c3:
            location = st.text_input("Location", placeholder="City / area")
            symptoms = st.multiselect(
                "Symptoms",
                [
                    "Fever",
                    "Cough",
                    "Sore throat",
                    "Headache",
                    "Fatigue",
                    "Chest pain",
                    "Shortness of breath",
                    "Nausea",
                    "Body pain",
                ],
            )
            duration = st.selectbox("Duration", ["< 24 hours", "1–3 days", "4–7 days", "> 1 week"])

        submitted = st.form_submit_button("Get Guidance")

    if submitted:
        st.subheader("Recommendation (Demo Output)")
        guidance = []

        if "Chest pain" in symptoms or "Shortness of breath" in symptoms:
            guidance.append("Seek urgent medical evaluation if symptoms are severe or sudden.")
        if "Fever" in symptoms and temperature >= 38.0:
            guidance.append("Monitor temperature, hydrate well, and rest.")
        if "Cough" in symptoms or "Sore throat" in symptoms:
            guidance.append("Consider warm fluids and avoid irritants; seek care if symptoms worsen.")
        if not guidance:
            guidance.append("Maintain hydration, balanced diet, and monitor symptoms for changes.")

        st.write("**User:**", name or "(not provided)")
        st.write("**Summary:**", ", ".join(symptoms) if symptoms else "No symptoms selected")
        st.write("**Guidance:**")
        for item in guidance:
            st.write(f"- {item}")

        st.info("Placeholder: Add nearby hospital/doctor results using real location services.")

elif section == "Dataset & Algorithms":
    st.header("Dataset Used")
    st.markdown(
        """
- Predefined medical symptom dataset
- Common disease–symptom mapping
- Basic health condition database
- Local rule-based dataset stored in app
"""
    )
    st.caption("Source: SMA.pdf – Dataset Used")

    st.subheader("Dataset Stats (Select Dataset)")
    dataset_choice = st.selectbox(
        "Choose dataset",
        [
            "Symptom–disease mapping",
            "Pima Indians Diabetes",
            "Expanded common diseases",
            "Ultimate Kerala medical AI",
        ],
    )

    if dataset_choice == "Symptom–disease mapping":
        sym_stats = symptom_dataset_stats(DATA / "disease_sympts_prec_full.csv")
        if sym_stats:
            st.table(
                {
                    "Field": [
                        "Dataset type",
                        "Size (records)",
                        "Diseases covered",
                        "Symptom count",
                        "Source file",
                    ],
                    "Value": [
                        "Symptom–disease mapping",
                        f"{sym_stats['rows']}",
                        f"{sym_stats['diseases']}",
                        f"{sym_stats['symptoms']}",
                        "disease_sympts_prec_full.csv",
                    ],
                }
            )
        else:
            st.warning("Symptom dataset not found in data/ folder.")

    if dataset_choice == "Pima Indians Diabetes":
        pima_stats = pima_dataset_stats(DATA / "pima_indians_diabetes.data.csv")
        if pima_stats:
            st.table(
                {
                    "Field": ["Dataset", "Rows", "Columns", "Source file"],
                    "Value": [
                        "Pima Indians Diabetes",
                        f"{pima_stats['rows']}",
                        f"{pima_stats['cols']}",
                        "pima_indians_diabetes.data.csv",
                    ],
                }
            )
        else:
            st.warning("Pima Indians dataset not found in data/ folder.")

    if dataset_choice == "Expanded common diseases":
        common_stats = simple_dataset_stats(
            DATA / "expanded_common_diseases_symptoms_dataset.csv", "Disease"
        )
        if common_stats:
            st.table(
                {
                    "Field": ["Dataset", "Rows", "Diseases", "Source file"],
                    "Value": [
                        "Expanded common diseases",
                        f"{common_stats['rows']}",
                        f"{common_stats['unique']}",
                        "expanded_common_diseases_symptoms_dataset.csv",
                    ],
                }
            )
        else:
            st.warning("Expanded common diseases dataset not found in data/ folder.")

    if dataset_choice == "Ultimate Kerala medical AI":
        ultimate_stats = simple_dataset_stats(
            DATA / "ultimate_kerala_medical_ai_dataset.csv", "Disease"
        )
        if ultimate_stats:
            st.table(
                {
                    "Field": ["Dataset", "Rows", "Diseases", "Source file"],
                    "Value": [
                        "Ultimate Kerala medical AI",
                        f"{ultimate_stats['rows']}",
                        f"{ultimate_stats['unique']}",
                        "ultimate_kerala_medical_ai_dataset.csv",
                    ],
                }
            )
        else:
            st.warning("Ultimate Kerala dataset not found in data/ folder.")

    st.header("Algorithms Used (Rule-Based)")
    st.markdown(
        """
- Rule-based symptom matching
- Decision tree logic
- If-else classification
- Keyword-based symptom mapping
"""
    )
    st.caption("Source: SMA.pdf – Algorithms Used")

    st.subheader("Model Metrics")
    st.table(
        {
            "Metric": ["Accuracy", "Precision", "Recall", "F1-Score"],
            "Value": [
                "Not computed (no trained model in this frontend)",
                "Not computed (no trained model in this frontend)",
                "Not computed (no trained model in this frontend)",
                "Not computed (no trained model in this frontend)",
            ],
        }
    )

    st.header("ML Methods from Literature (Optional Extension)")
    st.markdown(
        """
The multi-disease prediction literature highlights these methods:
- Logistic regression for heart disease prediction
- CNNs for cancer imaging classification
- SVM for diabetes prediction
"""
    )
    st.caption(
        "Source: Intelligent-Disease-Diagnosis-A-Multi-Disease-Prediction-Approach-Using-Machine-Learning.pdf – Abstract"
    )

elif section == "System Architecture":
    st.header("System Architecture")
    st.markdown(
        """
**Core modules**
- User Interface (Mobile App)
- Health Data Input
- Rule-Based Processing / Logic Engine
- Health Recommendation Module
- Database (User Health Records)

**Technologies**
- Frontend: Android (Java / Kotlin / XML)
- Backend: Firebase / SQLite
- Tools: Android Studio
- OS: Android
- Database: Cloud / Local Storage
"""
    )
    st.caption("Source: SMA.pdf – System Architecture")

    arch = ASSETS / "architecture.svg"
    if arch.exists():
        st.image(str(arch), use_column_width=True)

elif section == "Features & Future Enhancements":
    st.header("Key Features")
    st.markdown(
        """
- Instant symptom analysis
- Health tracking
- Basic medical guidance
- Nearby hospital and doctor recommendations (location-based)
"""
    )
    st.caption("Sources: SMA.pdf – Introduction; Smarthealthapp.pdf – Project Summary")

    st.header("Future Enhancements")
    st.markdown(
        """
- AI-based diagnosis
- Integration with wearable devices
- Doctor consultation feature
- Emergency alert system
"""
    )
    st.caption("Source: SMA.pdf – Future Enhancements")

elif section == "References":
    st.header("References (From Provided Documents)")
    st.markdown(
        """
1. **SMA.pdf** – Smart Health App (primary PPT-based source)
2. **Smarthealthapp.pdf** – Smart Health Assistance Mobile Application (project summary)
3. **Intelligent-Disease-Diagnosis-A-Multi-Disease-Prediction-Approach-Using-Machine-Learning.pdf** –
   Multi-disease prediction using ML (journal article)
"""
    )
    st.info("Placeholder: Add formatted citations (APA/IEEE) here")
