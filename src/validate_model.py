import argparse, os
import numpy as np, pandas as pd
import tensorflow as tf
from sklearn.metrics import classification_report, roc_auc_score

def load_data(path):
    df = pd.read_csv(path, index_col=0)
    y = (df.index.str.contains("cancer")).astype(int)  # Mock labels: cancer vs control
    return df.values, y

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="models/saved/cancer_model.h5")
    parser.add_argument("--data", type=str, default="data/processed/genomics.csv")
    args = parser.parse_args()

    X, y = load_data(args.data)
    model = tf.keras.models.load_model(args.model)

    preds = (model.predict(X) > 0.5).astype("int32")
    print("\nClassification Report:\n", classification_report(y, preds))
    print("\nROC-AUC:", roc_auc_score(y, preds))
