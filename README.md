# Cancer Research ML Pipelines

This repository contains **data processing and machine learning pipelines** for cancer research applications.  
Developed during my work as a **Data & Machine Learning Associate at the Helmholtz Institute of AI for Health Services (Munich, Germany)**.  

It focuses on:
- 🧬 Preprocessing **single-cell imaging** and **genomics** datasets  
- 🤖 Supporting **diagnostic model validation** for cancer research  
- 📊 Producing **visualizations & statistical summaries** for cross-functional teams  

---

## 🚀 Getting Started

### Install requirements
```bash
pip install -r requirements.txt
Preprocess single-cell imaging data
bash
Copy code
python src/preprocess_imaging.py --input data/raw/imaging --output data/processed/imaging
Preprocess genomics data
bash
Copy code
python src/preprocess_genomics.py --input data/raw/genomics.csv --output data/processed/genomics.csv
Validate diagnostic model
bash
Copy code
python src/validate_model.py --model models/saved/cancer_model.h5 --data data/processed/genomics.csv
Generate visualizations
bash
Copy code
python src/visualize.py --input data/processed/genomics.csv --output reports/
📊 Example Outputs
PCA plots of single-cell embeddings

ROC curves for cancer classification

Statistical summaries of gene expression

Heatmaps of important diagnostic features

🛠️ Tech Stack
Python 3.9+

TensorFlow / Keras

scikit-learn

pandas / NumPy

matplotlib / seaborn

scanpy (for single-cell data)

📜 License
MIT License

yaml
Copy code

---

## 🔹 `requirements.txt`
```txt
tensorflow>=2.8
scikit-learn
numpy
pandas
matplotlib
seaborn
scanpy
pyyaml
scipy
