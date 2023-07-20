import pandas as pd
import os
import re
from pyarabic.araby import strip_tashkeel
import pytesseract
import shutil
import os

try:
    from PIL import Image
except ImportError:
    import Image


#TODO: add default values

# Create argument parser
parser = argparse.ArgumentParser(description="Dataset Benchmark Tool")

parser.add_argument("--config", default=None, 
                    help='Configuration file path')
parser.add_argument('--save_dir', type=str, 
                    help='Save directory')
parser.add_argument("--metrics", nargs="+", type=str, required=False,
                    help="List of metrics for benchmarking (e.g., WER, CER, Levenshtein ratio)")
parser.add_argument("--models", nargs="+", type=str, required=False,
                    help="List of models to be evaluated (e.g., Tesseract OCR, KrakenOCR, EasyOCR)")
parser.add_argument("--data_dir", type=str, required=True,
                    help="Path to the data directory containing the dataset")

# Parse the arguments
config = parser.parse_args()
if config.config is not None:
    with open(config.config, 'r', encoding='utf-8') as file:
        config = json.load(file)
        config = {param: value for _, params in config.items()
                  for param, value in params.items()}

elif any([config.data_dir is None):
    print("The following argument is required: --data_dir")
    parser.print_help()
    exit(1)

from ocr import batch_predict
df = pd.read_csv(
    "/gdrive/MyDrive/Arabic Calligraphy/Full_Dataset/val_labels_50.csv")

df["img_path"] = df["img_name"].apply(lambda x: os.path.join(
    "/gdrive/MyDrive/Arabic Calligraphy/Full_Dataset/val", x)).values.tolist()
df["prediction_arr"] = df["img_path"].apply(lambda x: pytesseract.image_to_string(Image.open(x).resize((300, 50)).convert('RGB'),
                                                                                  lang='ara',
                                                                                  config='--psm 13 --oem 1'))
df["prediction"] = df["prediction_arr"].apply("".join).str.replace(
    "\n", "").str.strip().apply(strip_tashkeel)

df["leven_ratio"] = df.apply(lambda x: Levenshtein.ratio(
    x["label"], x["prediction"]), axis=1)
df["character_error_rate"] = df.apply(lambda x: Levenshtein.distance(
    x["label"], x["prediction"])/len(x["label"]), axis=1)
df["accuracy"] = df["label"] == df["prediction"]
df['accuracy'].sum()/df.shape[0]
df["word_error_rate"] = df.apply(
    lambda x: wer(x["label"], x["prediction"]), axis=1)
df.describe()
