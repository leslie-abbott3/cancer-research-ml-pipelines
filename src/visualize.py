import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse, os

def visualize(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(input_file, index_col=0)

    # Heatmap of first 50 genes
    plt.figure(figsize=(10,6))
    sns.heatmap(df.iloc[:, :50].T, cmap="viridis")
    plt.title("Top 50 Gene Expression Heatmap")
    plt.savefig(os.path.join(output_dir, "heatmap.png"))

    # PCA plot
    from sklearn.decomposition import PCA
    X_pca = PCA(n_components=2).fit_transform(df.values)
    plt.figure(figsize=(6,6))
    sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1])
    plt.title("PCA of Genomics Data")
    plt.savefig(os.path.join(output_dir, "pca.png"))

    print(f"[INFO] Visualizations saved to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data/processed/genomics.csv")
    parser.add_argument("--output", type=str, default="reports/")
    args = parser.parse_args()
    visualize(args.input, args.output)
