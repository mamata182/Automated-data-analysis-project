# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas",
#     "numpy",
#     "matplotlib",
#     "seaborn"
# ]
# ///

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_dataset(csv_path):

    # Load CSV safely with encoding fallback
    try:
        df = pd.read_csv(csv_path, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(csv_path, encoding="latin-1")
    except Exception as e:
        print("Error loading CSV:", e)
        sys.exit(1)

    print("Dataset Loaded:", csv_path)
    print("Shape:", df.shape)

    shape = df.shape
    columns = df.columns.tolist()
    dtypes = df.dtypes
    missing = df.isnull().sum()

    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    numeric_summary = df[numeric_cols].describe() if len(numeric_cols) > 0 else None

    # 1️⃣ Correlation
    if len(numeric_cols) > 1:
        corr = df[numeric_cols].corr()
        plt.figure(figsize=(6, 5))
        sns.heatmap(corr, cmap="coolwarm")
        plt.title("Correlation Matrix")
        plt.tight_layout()
        plt.savefig("correlation.png")
        plt.close()

    # 2️⃣ Distribution
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
        plt.savefig("distribution.png")
        plt.close()

    # 3️⃣ Categories
    if len(categorical_cols) > 0:
        col = categorical_cols[0]
        top = df[col].value_counts().head(10)
        plt.figure(figsize=(6, 4))
        sns.barplot(x=top.values, y=top.index)
        plt.title(f"Top {col}")
        plt.tight_layout()
        plt.savefig("categories.png")
        plt.close()

    # Generate README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Automated Data Analysis Report\n\n")
        f.write(f"## Dataset Shape\nRows: {shape[0]}, Columns: {shape[1]}\n\n")
        
        f.write("## Columns\n")
        for col in columns:
            f.write(f"- {col}\n")

        f.write("\n## Data Types\n")
        f.write(dtypes.to_string())

        f.write("\n\n## Missing Values\n")
        f.write(missing.to_string())

        if numeric_summary is not None:
            f.write("\n\n## Numeric Summary\n")
            f.write(numeric_summary.to_string())

        f.write("\n\nCharts generated automatically.\n")

    print("Analysis complete. README.md and charts generated.")


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run autolysis.py <dataset.csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    analyze_dataset(csv_path)


if __name__ == "__main__":
    main()
