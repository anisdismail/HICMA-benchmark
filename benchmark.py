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
