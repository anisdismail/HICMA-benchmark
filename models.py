import os
import pytesseract
import requests
import kraken
from kraken.lib import models
import easyocr
import shutil


class TesseractOCR:
    def __init__(self, config):
        self.config = config
        self.lang = None
        self.psm = None
        self.oem = None

    def initialize(self):
        url = self.config["trained_model_url"]
        local_filename = url.split("/")[-1]

        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(self.config["save_dir"], local_filename), 'wb') as f:
                f.write(response.content)
            print(f"File '{local_filename}' downloaded successfully.")
        else:
            requests.exceptions.HTTPError(
                f"Failed to download the file. Status code: {response.status_code}")

        try:
            shutil.move(os.path.join(
                self.config["save_dir"], local_filename), self.config["TesseractOCR_path"])
            print("File moved successfully.")
        except Exception as e:
            print(f"Error occurred while moving the file: {e}")

        self.lang = "ar"
        self.psm = self.config["psm"]
        self.oem = self.config["oem"]

    def predict(self, image):
        tesseract_config = f"--psm {self.psm} --oem {self.oem}"
        predicted_text = pytesseract.image_to_string(image,
                                                     lang=self.lang,
                                                     config=tesseract_config)

        return predicted_text


class KrakenOCR:
    def __init__(self, config):
        self.config = config
        self.model = None

    def initialize(self):
        url = self.config["kraken_url"]
        local_filename = url.split("/")[-1]

        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(self.config["save_dir"], local_filename), 'wb') as f:
                f.write(response.content)
            print(f"File '{local_filename}' downloaded successfully.")
        else:
            requests.exceptions.HTTPError(
                f"Failed to download the file. Status code: {response.status_code}")
        self.model = models.load_any(os.path.join(
            self.config["save_dir"], local_filename))

    def predict(self, image):
        seg_box = {'boxes': [[0, 0, image.size[0], image.size[1]]],
                   'text_direction': self.config["text_direction"]}
        preds = kraken.rpred.rpred(self.model, image, seg_box)
        return [pred.prediction for pred in preds]


class EasyOCR:
    def __init__(self, config):
        self.config = config
        self.reader = None

    def initialize(self):
        # Load and initialize the OCR model
        self.reader = easyocr.Reader(["ar"])

    def predict(self, image):
        predicted_text = self.reader.readtext(
            image, detail=self.config["detail"])
        return predicted_text
