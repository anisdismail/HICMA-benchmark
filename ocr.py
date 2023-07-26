from models import TesseractOCR, KrakenOCR, EasyOCR
from utils import clean_text
import swifter

def predict(image, ocr_model_name, config):
    ocr_models = {
        "TesseractOCR": TesseractOCR(config),
        "Kraken": KrakenOCR(config),
        "EasyOCR": EasyOCR(config)
    }

    if ocr_model_name not in ocr_models:
        raise ValueError(f"""OCR model '{ocr_model_name}' not available. 
                         \n Available models are {list(ocr_models.keys())}""")

    ocr_model = ocr_models[ocr_model_name]
    ocr_model.initialize()
#    image = load_image(image, config)
#    preprocessed_image = preprocess_image(image, config)
    prediction = ocr_model.predict(image)
    cleaned_prediction = clean_text(prediction)
    return {"prediction": prediction, "cleaned_prediction": cleaned_prediction}


def batch_predict(images_df, ocr_model_name, config):
    ocr_models = {
        "TesseractOCR": TesseractOCR(config),
        "Kraken": KrakenOCR(config),
        "EasyOCR": EasyOCR(config)
    }

    if ocr_model_name not in ocr_models:
        raise ValueError(f"""OCR model '{ocr_model_name}' not available. 
                         \n Available models are {list(ocr_models.keys())}""")

    ocr_model = ocr_models[ocr_model_name]
    ocr_model.initialize()
    results_df = images_df.copy()
    results_df[f"prediction_{ocr_model_name}"] = results_df["preprocessed_image"].swifter.apply(
        ocr_model.predict)
    results_df[f"cleaned_prediction_{ocr_model_name}"] = results_df[f"prediction_{ocr_model_name}"].apply(
        clean_text)

    return results_df
