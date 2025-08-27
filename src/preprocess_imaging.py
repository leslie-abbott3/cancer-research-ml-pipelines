import os, argparse
import numpy as np
import scanpy as sc

def preprocess_images(input_dir, output_dir):
    """
    Preprocess single-cell imaging data using Scanpy:
    - Load raw single-cell expression matrices
    - Normalize counts
    - Log-transform data
    - Save processed AnnData objects
    """
    os.makedirs(output_dir, exist_ok=True)
    for f in os.listdir(input_dir):
        if f.endswith(".h5ad"):
            adata = sc.read_h5ad(os.path.join(input_dir, f))
            sc.pp.normalize_total(adata, target_sum=1e4)
            sc.pp.log1p(adata)
            outpath = os.path.join(output_dir, f)
            adata.write(outpath)
            print(f"[INFO] Processed {f} -> {outpath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data/raw/imaging")
    parser.add_argument("--output", type=str, default="data/processed/imaging")
    args = parser.parse_args()
    preprocess_images(args.input, args.output)
