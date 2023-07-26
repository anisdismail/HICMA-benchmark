import cv2
from pyarabic.araby import strip_tashkeel
import swifter

def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_COLOR)


def preprocess_image(image, config):
    if config["image_processing_width"] and config["image_processing_height"]:
        image = cv2.resize(image, (config["image_processing_width"], config["image_processing_height"]))
    if config["grayscale"]:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if config["binarize"]:
        _, image = cv2.threshold(
            image, 80, 255, cv2.THRESH_BINARY)
    return image


def batch_preprocess(df, config):
    images_df = df.copy()
    images_df["image"] = images_df["img_path"].swifter.apply(load_image)
    images_df["preprocessed_image"] = images_df["image"].apply(
        lambda x: preprocess_image(x, config))
    return images_df


def clean_text(text):
    text = "".join(text)
    text = text.replace("\n", "").strip()
    text_no_diacritics = strip_tashkeel(text)
    return text_no_diacritics
