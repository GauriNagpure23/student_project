import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Path setup
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FILE = os.path.join(PROJECT_ROOT, "data", "phonebook_cleaned.csv")
GRAPH_FOLDER = os.path.join(PROJECT_ROOT, "graphs")

os.makedirs(GRAPH_FOLDER, exist_ok=True)

def plot_graphs():
    print("📊 Loading cleaned dataset for visualization...")

    df = pd.read_csv(DATA_FILE)

    print("\n--- DATA PREVIEW ---")
    print(df.head(100))

    # ---------------- LINE PLOT ----------------
    plt.figure()
    plt.plot(df["Age"], df["Percentage"])
    plt.title("Age vs Percentage (Line Plot)")
    plt.xlabel("Age")
    plt.ylabel("Percentage")
    plt.savefig(os.path.join(GRAPH_FOLDER, "line_plot.png"))
    plt.close()

    # ---------------- BAR PLOT ----------------
    plt.figure()
    df["Class"].value_counts().plot(kind="bar")
    plt.title("Students per Class")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.savefig(os.path.join(GRAPH_FOLDER, "bar_plot.png"))
    plt.close()

    # ---------------- HISTOGRAM ----------------
    plt.figure()
    plt.hist(df["Percentage"], bins=10)
    plt.title("Percentage Distribution")
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(GRAPH_FOLDER, "histogram.png"))
    plt.close()

    # ---------------- CORRELATION HEATMAP ----------------
    plt.figure()
    corr = df[["Age", "Percentage"]].corr()
    sns.heatmap(corr, annot=True)
    plt.title("Correlation Heatmap")
    plt.savefig(os.path.join(GRAPH_FOLDER, "heatmap.png"))
    plt.close()

    print("✅ All graphs saved in graphs/ folder")
