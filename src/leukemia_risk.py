import pandas as pd
import numpy as np
import argparse, os
import seaborn as sns
import matplotlib.pyplot as plt

# Example leukemia-associated gene panel
LEUKEMIA_GENES = {
    "TP53": 3.0,
    "FLT3": 2.5,
    "NPM1": 2.0,
    "CEBPA": 1.5,
    "RUNX1": 2.2,
    "DNMT3A": 1.8,
    "IDH2": 1.7,
    "IKZF1": 1.6
}

def compute_risk_score(variants):
    """
    Compute risk score:
    - Check if variants overlap with leukemia-associated genes
    - Weight contribution by known risk factor
    """
    score = 0
    flagged_genes = []
    for gene, weight in LEUKEMIA_GENES.items():
        if gene in variants:
            score += weight
            flagged_genes.append(gene)
    return score, flagged_genes

def analyze_patient_file(filepath):
    """
    Reads patient genomics CSV:
    Expected format: gene, variant, effect
    """
    df = pd.read_csv(filepath)
    patient_id = os.path.basename(filepath).split(".")[0]
    genes = df["gene"].unique().tolist()

    score, flagged = compute_risk_score(genes)
    return {
        "patient_id": patient_id,
        "risk_score": score,
        "flagged_genes": ";".join(flagged) if flagged else "None"
    }

def leukemia_pipeline(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    results = []

    for file in os.listdir(input_dir):
        if file.endswith(".csv"):
            res = analyze_patient_file(os.path.join(input_dir, file))
            results.append(res)

    # Save summary table
    df_results = pd.DataFrame(results)
    outpath = os.path.join(output_dir, "leukemia_risk_summary.csv")
    df_results.to_csv(outpath, index=False)

    # Visualization
    plt.figure(figsize=(8,6))
    sns.barplot(data=df_results, x="patient_id", y="risk_score")
    plt.xticks(rotation=45)
    plt.title("Genetic Predisposition Risk Scores for Leukemia")
    plt.ylabel("Risk Score")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "leukemia_risk_scores.png"))

    print(f"[INFO] Analysis complete. Results saved to {outpath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data/raw/patients")
    parser.add_argument("--output", type=str, default="data/processed/patients")
    args = parser.parse_args()
    leukemia_pipeline(args.input, args.output)
