import joblib
import pandas as pd
from utils import get_kmers
from ui import build_ui




# 🔹 Entry point
if __name__ == "__main__":
    demo = build_ui()
    demo.launch()
