# Smart Health App – CSD 334 Frontend (Streamlit)

This is a **simple, neat Streamlit frontend** prototype for the Smart Health App, created from the PPT
(`SMA.pdf`) and supporting PDFs. It provides clear sections, source-based definitions, a demo symptom UI,
and clean visuals.

## How to run

```bash
cd "/home/prak05/Desktop/naeem project/csd334_streamlit"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Generate datasets (optional)

```bash
cd "/home/prak05/Desktop/naeem project/csd334_streamlit"
python3 scripts/generate_datasets.py
```

Default outputs:
- `data/expanded_common_diseases_symptoms_dataset.csv`
- `data/ultimate_kerala_medical_ai_dataset.csv` (only if `data/kerala_expanded_diseases_symptoms_dataset.csv` exists)

Custom paths:
```bash
python3 scripts/generate_datasets.py \\
  --base-kerala data/kerala_expanded_diseases_symptoms_dataset.csv \\
  --out-dir data \\
  --total-target 320 \\
  --seed 42
```

### Fully executable mode

If the Kerala base dataset is missing, the script now **auto-creates a fallback base** from the common dataset, so the\nultimate dataset is always generated. This makes the pipeline fully executable end-to-end.

## Project structure

```
csd334_streamlit/
  app.py
  README.md
  requirements.txt
  assets/
    hero.svg
    architecture.svg
  data/
    disease_sympts_prec_full.csv
    pima_indians_diabetes.data.csv
    heart_disease.zip
  docs/
```

## What’s inside

- `app.py` – Streamlit UI with navigation, definitions, sources, and demo symptom form.
- `assets/hero.svg` – Simple hero banner.
- `assets/architecture.svg` – Clean system architecture diagram.
- `data/` – Placeholder for datasets (symptom mappings, CSVs, etc.).
- `docs/` – Optional place to keep copies of PDFs if you want the app to reference them locally.

## Sources used (from provided documents)

- **SMA.pdf** – Primary PPT-based source (Abstract, Problem, Objectives, Proposed System, Architecture, Future Enhancements)
- **Smarthealthapp.pdf** – Definition and location-based hospital recommendation concept
- **Intelligent-Disease-Diagnosis-A-Multi-Disease-Prediction-Approach-Using-Machine-Learning.pdf** – Multi-disease prediction definition and ML methods

## Downloaded datasets

- Symptom–disease dataset: `data/disease_sympts_prec_full.csv` (from Hugging Face dataset `shanover/disease_symptoms_prec_full`).  
- Pima Indians Diabetes: `data/pima_indians_diabetes.data.csv` (GitHub mirror of UCI dataset).  
- Heart Disease: `data/heart_disease.zip` (UCI Heart Disease dataset).

The app now **reads these files** and shows dataset counts in the Dataset section.

## Model metrics note

No model has been trained inside this frontend, so metrics are shown as **not computed**. If you want baseline
metrics, I can train a quick model and add them.

## Placeholders to fill later

- Add real dataset sizes and metrics (accuracy, precision, recall, F1)
- Add real hospital/doctor recommendations using a location API
- Add evaluation charts and graphs if required

## Notes

- The demo symptom guidance is rule-based and **not** a medical diagnosis.
- The UI is intentionally minimal and clean for CSD 334 presentation.
