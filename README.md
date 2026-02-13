📊 Automated Data Analysis Project

📌 Overview

This project is an automated data analysis system built using Python. It processes CSV datasets and automatically generates structured reports and visualizations without manual intervention.
The script performs data inspection, statistical summarization, correlation analysis, and visualization generation, making it a reusable tool for analyzing different datasets efficiently.
The entire implementation is contained in a single Python script (autolysis.py) to ensure simplicity, portability, and ease of evaluation.
🚀 Features
Automatic CSV loading with encoding fallback (UTF-8 / Latin-1)
1.Dataset shape and column analysis
2.Missing value detection
3.Automatic detection of numeric and categorical columns
4.Statistical summary for numeric data
5.Correlation heatmap generation
6.Distribution plot for numeric features
7.Bar chart for top categorical values
8.Atomatic generation of structured README report

Compatible with uv for dependency management

⚙️ Project Workflow

1️⃣ Dataset Input

The user provides a CSV file when running the script.

2️⃣ Data Inspection

The script analyzes:

Number of rows and columns

Column names

Data types

Missing values

3️⃣ Data Classification

Columns are automatically categorized into:

Numeric columns

Categorical columns

4️⃣ Statistical Analysis

For numeric columns, the script calculates:

Mean

Standard deviation

Minimum and maximum

Quartiles

If multiple numeric columns exist, a correlation matrix is generated.

5️⃣ Visualization Generation

The script automatically creates:

correlation.png

distribution.png

categories.png

6️⃣ Automated Report Generation

A structured README.md is generated for each dataset containing:

Dataset summary

Column details

Missing values

Statistical summary

Reference to generated charts

🛠 Technologies Used

Python 3.11+

pandas

numpy

matplotlib

seaborn

uv

📂 Project Structure
llm-project/
│
├── autolysis.py
├── goodreads/
├── happiness/
├── media/
└── README.md


Each dataset folder contains:

CSV file

Generated charts

Auto-generated report

▶️ How to Run

Install uv:
pip install uv

Run the script:
python -m uv run autolysis.py dataset.csv

Example:
python -m uv run autolysis.py happiness/happiness.csv
