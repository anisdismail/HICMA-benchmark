import argparse
import json
import os
import sys
import pandas as pd

from ocr import batch_predict
from utils import batch_preprocess
from eval import batch_evaluate

# TODO: add default values

# Create argument parser
parser = argparse.ArgumentParser(description="Dataset Benchmark Tool")

parser.add_argument('--save_dir', type=str, required=True,
                    help="Save directory")
parser.add_argument("--metrics", nargs="+", type=str, default=["WER", "CER", "Levenshtein_ratio"],
                    help="List of metrics for benchmarking (e.g., WER, CER, Levenshtein ratio)")
parser.add_argument("--model", type=str, required=True,
                    help="Model to be evaluated (e.g., Tesseract OCR, KrakenOCR, EasyOCR)")
parser.add_argument("--data_dir", type=str, required=True,
                    help="Path to the data directory containing the dataset")

# TesseractOCR settings
parser.add_argument("--tesseract_psm", type=int, default=13,
                    help="Tesseract OCR page segmentation mode (PSM)")
parser.add_argument("--tesseract_oem", type=int, default=1,
                    help="Tesseract OCR engine mode (OEM)")
parser.add_argument("--trained_model_url", type=str, default=None,
                    help="Tesseract OCR trained model url")
parser.add_argument("--TesseractOCR_path", type=str, default=None,
                    help="Tesseract OCR executable path")
# Kraken settings
parser.add_argument("--kraken_url", type=str, default=None,
                    help="Kraken OCR trained model url")
parser.add_argument("--text_direction", type=str, default="horizontal-lr",
                    help="Text direction for Kraken OCR (e.g., horizontal-lr)")

# EasyOCR settings
parser.add_argument("--easyocr_detail", type=int, default=0,
                    help="EasyOCR detail level")

# Image processing settings
parser.add_argument("--image_processing_width", type=int, default=None,
                    help="Width for image processing")
parser.add_argument("--image_processing_height", type=int, default=None,
                    help="Height for image processing")
parser.add_argument("--binarize", type=bool, action='store_true',
                    help="Binarize image")
parser.add_argument("--grayscale", type=bool, action='store_true',
                    help="Convert image to grayscale")


# Parse the arguments
config = parser.parse_args()
if config.config is not None:
    with open(config.config, 'r', encoding='utf-8') as file:
        config = json.load(file)
        config = {param: value for _, params in config.items()
                  for param, value in params.items()}

elif config.data_dir is None:
    print("The following argument is required: --data_dir")
    parser.print_help()
    sys.exit(1)

df = pd.read_csv(os.path.join(config["data_dir"], "val_labels_50.csv"))

df["img_path"] = df["img_name"].apply(lambda x: os.path.join(
    config["data_dir"], "val", x)).values.tolist()

preprocessed_df = batch_preprocess(df, config=config)
prediction_df = batch_predict(
    preprocessed_df, ocr_model_name=config["model"], config=config)
results_df = prediction_df.copy()
for metric in config["metrics"]:
    results_df = batch_evaluate(preds_df=results_df, metric_name=metric)

print(results_df.describe())
