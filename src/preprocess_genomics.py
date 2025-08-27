import pandas as pd
import argparse
from sklearn.preprocessing import StandardScaler

def preprocess_genomics(input_file, output_file):
    """
    Preprocess genomics dataset:
    - Load gene expression CSV
    - Standardize features
    - Save cleaned dataset
    """
    df = pd.read_csv(input_file, index_col=0)
    X = df.values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    df_scaled = pd.DataFrame(X_scaled, index=df.index, columns=df.columns)
    df_scaled.to_csv(output_file)
    print(f"[INFO] Processed genomics -> {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data/raw/genomics.csv")
    parser.add_argument("--output", type=str, default="data/processed/genomics.csv")
    args = parser.parse_args()
    preprocess_genomics(args.input, args.output)
