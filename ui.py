import gradio as gr
from utils import get_kmers  # ensure this is accessible for joblib
import joblib
import pandas as pd

# 🔹 Load trained pipeline & label encoder
pipeline = joblib.load("models/gradient_boosting_pipeline.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

idx_to_label = {
    0: "BIOLOGICAL_REGION",
    1: "OTHER",
    2: "PROTEIN_CODING",
    3: "PSEUDO",
    4: "ncRNA",
    5: "rRNA",
    6: "scRNA",
    7: "snRNA",
    8: "snoRNA",
    9: "tRNA"
}


def predict_gene(sequence, description):
    """
    Run prediction for a single sample (called from UI).
    """
    data = {
        "NucleotideSequence": sequence,
        "GeneGroupMethod": 'NCBI Ortholog',
        "Description": description,
        "SequenceLength": int(len(sequence)),
    }
    df = pd.DataFrame([data])

    pred = pipeline.predict(df)[0]
    return idx_to_label.get(pred, "Unknown")




def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# 🧬 Gene Type Classifier")
        gr.Markdown("Enter gene details below and get predictions:")

        sequence = gr.Textbox(label="Nucleotide Sequence", placeholder="Enter sequence...")
        description = gr.Textbox(label="Description", placeholder="Enter description...")

        output = gr.Textbox(label="Prediction Result")

        gr.Button("Predict").click(
            predict_gene,
            inputs=[sequence, description],
            outputs=output
        )

    return demo
