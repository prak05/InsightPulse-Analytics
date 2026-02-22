#!/usr/bin/env python3
"""
Generate datasets for the Smart Health App frontend.

Outputs:
- expanded_common_diseases_symptoms_dataset.csv
- ultimate_kerala_medical_ai_dataset.csv (requires an existing Kerala base dataset)
"""

from __future__ import annotations

import argparse
import random
from pathlib import Path

try:
    from pandas import DataFrame, concat, read_csv
except Exception as exc:  # pragma: no cover - shown only when pandas missing
    raise SystemExit(
        "pandas is required to run this script. Install with: pip install pandas"
    ) from exc


def build_common_dataset() -> DataFrame:
    data = [
        {"Disease": "Common Cold", "Symptoms": "Runny nose; Sneezing; Sore throat; Mild fever; Cough"},
        {"Disease": "Influenza (Flu)", "Symptoms": "High fever; Body aches; Fatigue; Dry cough; Headache"},
        {"Disease": "COVID-19", "Symptoms": "Fever; Dry cough; Loss of taste or smell; Fatigue; Shortness of breath"},
        {"Disease": "Dengue Fever", "Symptoms": "High fever; Severe headache; Joint pain; Rash; Nausea"},
        {"Disease": "Malaria", "Symptoms": "Fever; Chills; Sweating; Headache; Nausea"},
        {"Disease": "Typhoid", "Symptoms": "Prolonged fever; Weakness; Abdominal pain; Loss of appetite; Headache"},
        {"Disease": "Diabetes", "Symptoms": "Frequent urination; Increased thirst; Fatigue; Blurred vision; Weight loss"},
        {"Disease": "Hypertension", "Symptoms": "Headache; Dizziness; Nosebleeds; Chest pain; Often asymptomatic"},
        {"Disease": "Asthma", "Symptoms": "Shortness of breath; Wheezing; Chest tightness; Coughing"},
        {"Disease": "Tuberculosis", "Symptoms": "Persistent cough; Weight loss; Night sweats; Fever; Chest pain"},
        {"Disease": "Migraine", "Symptoms": "Severe headache; Nausea; Sensitivity to light; Visual disturbances"},
        {"Disease": "Food Poisoning", "Symptoms": "Vomiting; Diarrhea; Abdominal cramps; Fever; Nausea"},
        {"Disease": "Chickenpox", "Symptoms": "Itchy rash; Fever; Fatigue; Loss of appetite"},
        {"Disease": "Measles", "Symptoms": "Fever; Rash; Runny nose; Red eyes; Cough"},
        {"Disease": "Pneumonia", "Symptoms": "Cough; Fever; Chest pain; Difficulty breathing; Fatigue"},
        {"Disease": "Bronchitis", "Symptoms": "Persistent cough; Mucus production; Fatigue; Shortness of breath"},
        {"Disease": "Sinusitis", "Symptoms": "Facial pain; Nasal congestion; Headache; Fever; Postnasal drip"},
        {"Disease": "Appendicitis", "Symptoms": "Severe abdominal pain; Nausea; Vomiting; Fever; Loss of appetite"},
        {"Disease": "Gastritis", "Symptoms": "Stomach pain; Nausea; Bloating; Vomiting; Loss of appetite"},
        {"Disease": "Ulcer", "Symptoms": "Burning stomach pain; Nausea; Bloating; Heartburn"},
        {"Disease": "Anemia", "Symptoms": "Fatigue; Pale skin; Shortness of breath; Dizziness"},
        {"Disease": "Hypothyroidism", "Symptoms": "Fatigue; Weight gain; Cold intolerance; Dry skin"},
        {"Disease": "Hyperthyroidism", "Symptoms": "Weight loss; Rapid heartbeat; Sweating; Anxiety"},
        {"Disease": "Depression", "Symptoms": "Persistent sadness; Fatigue; Loss of interest; Sleep problems"},
        {"Disease": "Anxiety Disorder", "Symptoms": "Restlessness; Rapid heartbeat; Sweating; Excessive worry"},
        {"Disease": "Arthritis", "Symptoms": "Joint pain; Swelling; Stiffness; Reduced mobility"},
        {"Disease": "Osteoporosis", "Symptoms": "Bone pain; Fragile bones; Back pain; Height loss"},
        {"Disease": "Kidney Stones", "Symptoms": "Severe flank pain; Blood in urine; Nausea; Vomiting"},
        {"Disease": "Urinary Tract Infection", "Symptoms": "Burning urination; Frequent urge; Pelvic pain; Cloudy urine"},
        {"Disease": "Hepatitis A", "Symptoms": "Fatigue; Jaundice; Abdominal pain; Nausea"},
        {"Disease": "Hepatitis B", "Symptoms": "Jaundice; Dark urine; Fatigue; Abdominal pain"},
        {"Disease": "Hepatitis C", "Symptoms": "Fatigue; Jaundice; Loss of appetite; Nausea"},
        {"Disease": "Heart Attack", "Symptoms": "Chest pain; Shortness of breath; Sweating; Nausea"},
        {"Disease": "Stroke", "Symptoms": "Sudden numbness; Confusion; Trouble speaking; Loss of balance"},
        {"Disease": "Epilepsy", "Symptoms": "Seizures; Confusion; Staring spells; Loss of awareness"},
        {"Disease": "Parkinson's Disease", "Symptoms": "Tremors; Slow movement; Muscle stiffness; Balance problems"},
        {"Disease": "Alzheimer's Disease", "Symptoms": "Memory loss; Confusion; Difficulty speaking; Mood changes"},
        {"Disease": "Psoriasis", "Symptoms": "Red patches; Itchy skin; Scaly skin; Dryness"},
        {"Disease": "Eczema", "Symptoms": "Itchy skin; Redness; Dry patches; Swelling"},
        {"Disease": "Acne", "Symptoms": "Pimples; Blackheads; Oily skin; Inflammation"},
        {"Disease": "Allergic Rhinitis", "Symptoms": "Sneezing; Runny nose; Itchy eyes; Nasal congestion"},
        {"Disease": "Conjunctivitis", "Symptoms": "Red eyes; Itching; Discharge; Tearing"},
        {"Disease": "Otitis Media", "Symptoms": "Ear pain; Fever; Hearing difficulty; Irritability"},
        {"Disease": "Gout", "Symptoms": "Joint pain; Swelling; Redness; Warm joints"},
        {"Disease": "Obesity", "Symptoms": "Excess body fat; Fatigue; Shortness of breath"},
        {"Disease": "Sleep Apnea", "Symptoms": "Snoring; Daytime sleepiness; Interrupted breathing"},
        {"Disease": "GERD", "Symptoms": "Heartburn; Chest discomfort; Acid regurgitation; Nausea"},
        {"Disease": "Pancreatitis", "Symptoms": "Upper abdominal pain; Nausea; Vomiting; Fever"},
        {"Disease": "Leptospirosis", "Symptoms": "Fever; Muscle pain; Headache; Vomiting"},
        {"Disease": "Cholera", "Symptoms": "Severe diarrhea; Dehydration; Vomiting; Muscle cramps"},
    ]
    return DataFrame(data)


def build_ultimate_dataset(base_csv: Path, total_target: int, seed: int) -> DataFrame:
    random.seed(seed)

    df_existing = read_csv(base_csv)

    departments = [
        "General Medicine",
        "Cardiology",
        "Neurology",
        "Dermatology",
        "Gastroenterology",
        "Pulmonology",
        "Infectious Disease",
        "Orthopedics",
        "Psychiatry",
        "Endocrinology",
        "ENT",
        "Ophthalmology",
        "Nephrology",
        "Pediatrics",
    ]

    severity_levels = ["Mild", "Moderate", "Severe", "Critical"]

    symptom_pool = [
        "Fever",
        "Headache",
        "Fatigue",
        "Cough",
        "Joint pain",
        "Rash",
        "Vomiting",
        "Diarrhea",
        "Abdominal pain",
        "Chest pain",
        "Shortness of breath",
        "Dizziness",
        "Nausea",
        "Weight loss",
        "Night sweats",
        "Muscle pain",
        "Sneezing",
        "Runny nose",
        "Skin redness",
        "Blurred vision",
    ]

    treatments = [
        "Hydration and rest",
        "Antibiotics if bacterial",
        "Antiviral medication",
        "Pain management",
        "Hospital observation",
        "Lifestyle modification",
        "Specialist referral",
        "Supportive care",
    ]

    needed = max(0, total_target - len(df_existing))
    synthetic = []

    for i in range(needed):
        disease_name = f"Regional Syndrome {i + 1}"
        symptoms = "; ".join(random.sample(symptom_pool, 5))
        severity = random.choice(severity_levels)
        department = random.choice(departments)
        treatment = random.choice(treatments)

        synthetic.append(
            {
                "Disease": disease_name,
                "Symptoms": symptoms,
                "Severity": severity,
                "Department": department,
                "TreatmentHint": treatment,
            }
        )

    df_existing = df_existing.copy()
    df_existing["Severity"] = [random.choice(severity_levels) for _ in range(len(df_existing))]
    df_existing["Department"] = [random.choice(departments) for _ in range(len(df_existing))]
    df_existing["TreatmentHint"] = [random.choice(treatments) for _ in range(len(df_existing))]

    df_synthetic = DataFrame(synthetic)
    df_final = concat([df_existing, df_synthetic], ignore_index=True)
    return df_final


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate health datasets for the project.")
    parser.add_argument(
        "--base-kerala",
        type=Path,
        default=Path("data/kerala_expanded_diseases_symptoms_dataset.csv"),
        help="Path to the existing Kerala dataset CSV.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("data"),
        help="Output directory for generated CSV files.",
    )
    parser.add_argument(
        "--total-target",
        type=int,
        default=320,
        help="Target row count for the ultimate dataset.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility.",
    )
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)

    # Always write the common dataset
    common_path = args.out_dir / "expanded_common_diseases_symptoms_dataset.csv"
    common_df = build_common_dataset()
    common_df.to_csv(common_path, index=False)
    print(f"Saved: {common_path}")

    # Ensure a base Kerala dataset exists for full execution
    if not args.base_kerala.exists():
        fallback_base = args.out_dir / "kerala_expanded_diseases_symptoms_dataset.csv"
        print(f"Base Kerala dataset not found: {args.base_kerala}")
        print(f"Creating fallback base dataset at: {fallback_base}")
        common_df.to_csv(fallback_base, index=False)
        args.base_kerala = fallback_base

    # Write the ultimate dataset
    ultimate_path = args.out_dir / "ultimate_kerala_medical_ai_dataset.csv"
    build_ultimate_dataset(args.base_kerala, args.total_target, args.seed).to_csv(
        ultimate_path, index=False
    )
    print(f"Saved: {ultimate_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
