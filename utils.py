from pyarabic.araby import strip_tashkeel


def preprocess_image(image, config):
    pass


def load_image(image_path, config):
    pass


def clean_text(text):
    text = "".join(text)
    text = text.replace("\n", "").strip()
    text_no_diacritics = strip_tashkeel(text)
    return text_no_diacritics


def batch_preprocess(df, config):
    images_df = df.copy()
    images_df["image"] = images_df["img_path"].apply(
        lambda x: load_image(x, config))
    images_df["preprocessed_image"] = images_df["image"].apply(
        lambda x: preprocess_image(x, config))
    return images_df
