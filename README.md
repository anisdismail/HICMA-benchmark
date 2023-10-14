<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![CNC Liscence][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="resources/hicma_benchmark.png" alt="logo" style="max-width: 60%;">
  <h1 align="center"> HICMA OCR Benchmarking Tool</h1>
  <p align="center">
    <br />
    <a href="https://github.com/anisdismail/HICMA-benchmark"><strong>Explore the docs</strong></a>
    <br />
    <br />
    <a href="https://github.com/anisdismail/HICMA-benchmark">View Demo</a>
    ·
    <a href="https://github.com/anisdismail/HICMA-benchmark/issues">Report Bug</a>
    ·
    <a href="https://github.com/anisdismail/HICMA-benchmark/pulls">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
      <li> <a href="#key-features">Key Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
   <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The HICMA Dataset Benchmarking Tool is a powerful utility designed to assess the performance of Optical Character Recognition (OCR) models on a the HICMA Dataset. This tool is intended for researchers, developers, and data scientists working with OCR technologies, providing them with valuable insights into the accuracy and efficiency of their OCR models.

### Key Features:

- **Dataset Evaluation**: The OCR Benchmarking Tool allows users to easily evaluate the performance of their OCR models on the HICMA Dataset. By providing a standardized and consistent evaluation environment, users can compare different OCR systems objectively.

- **Metrics and Statistics**: The tool offers a comprehensive set of evaluation metrics, including character error rate (CER), word error rate (WER) and Levenshtein ratio. It also provides statistical summaries to understand model performance across different images and fonts.

- **Configurable Parameters**: Users can customize evaluation parameters to suit their specific requirements. These parameters include character recognition confidence thresholds, metrics choice and image pre-processing options.

- **Visualizations**: The HICMA OCR Benchmarking Tool generates interactive visualizations and charts to help users visualize the results more intuitively. These visualizations aid in identifying patterns and areas for improvement in the OCR models (TODO).

- **Easy Integration**: The tool is designed to seamlessly integrate with popular OCR frameworks and libraries (Tesseract OCR, Kraken, EasyOCR, etc...), making it convenient for users to benchmark their existing models without significant code modifications.

- **Reproducibility**: The tool ensures reproducibility by saving evaluation results and summmaries. This allows users to review and share their experiments with others easily.


### Built With

* [Tesseract OCR](https://tesseract-ocr.github.io/)
* [EasyOCR](https://www.jaided.ai/easyocr/documentation/)
* [Kraken](https://kraken.re/4.3.0/index.html)
* [PyArabic](https://pyarabic.readthedocs.io/ar/latest/)
* [OpenCV](https://pypi.org/project/opencv-python/)
* [Pandas](https://pandas.pydata.org/docs)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps:

### Prerequisites
Depending on the OCR model you are benchmarking, you need to make sure to set up the environment according to the OCR model documentation:
- **Tesseract OCR** : make sure to set up Tesseract OCR on your machine by following the documentation [here](https://tesseract-ocr.github.io/tessdoc/). Make sure to also provide the link to the pretrained model you would like to use. 
Links to Pretrained Tesseract OCR models on Arabic Text used in this benchmark can be found [here](https://github.com/anisdismail/HICMA-benchmark/blob/main/resources/TesseractOCR.txt).
- **Kraken** : Make sure to also provide the link to the pretrained model you would like to use. 
Links to Pretrained Kraken models on Arabic Text used in this benchmark can be found [here](https://github.com/anisdismail/HICMA-benchmark/blob/main/resources/kraken.txt).

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/anisdismail/HICMA-benchmark
   ```
2. Change to the project repositry:
   ```sh
   cd HICMA-benchmark

   ```
3. Run the following command to create the instant the required packages to the environment:
```sh
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage

1. To start the benchmark script, run the following command:
   ```sh
   python benchmark.py --config config.json
   ```
You can modify the experiment parameters in the config.json file:
   ```json
{
    "general": {
        "save_dir": "",
        "metrics": [],
        "model": "",
        "data_dir": ""
    },
    "image_processing": {
        "image_processing_width": null,
        "image_processing_height": null,
        "binarize": true,
        "grayscale": true
    }
}
   ```
  Please note that the benchmark tool will **only work with one model at a time**, therefore make sure to choose only one of the following models at a time and add it to the config.json. If you provide more than one model in the same config file, the benchmarking script will only use the first.
  ```json
    "TesseractOCR": {
        "tesseract_psm": 13,
        "tesseract_oem": 1,
        "trained_model_url": ,
        "TesseractOCR_path":
    },
    "Kraken": {
        "kraken_url": [],
        "text_direction": "horizontal-lr"
    },
    "EasyOCR": {
        "easyocr_detail": 0
    }
  ```
2. You can run the script from the command line and it will parse the command line arguments based on the given parameters. For example:
```sh
python benchmark.py --save_dir save_dir --metrics "CER" "WER" "Levenshtein_ratio" --model "model" --data_dir "" --image_processing_width null --image_processing_height null --binarize true --grayscale true --tesseract_psm 13 --tesseract_oem 1 --trained_model_url "" --TesseractOCR_path "" --kraken_url "" --text_direction "horizontal-lr" --easyocr_detail 0

```
Please note that you should only specify **one model at a time** in the command line argument. If you provide more than one model in the command, the benchmarking script will only use the first model.

3. You can also check all the possible parameters with their corresponding description using the following command:
```sh
python benchmark.py --help
```
It will generate the following output:
```sh
options:
  --config CONFIG
    Configurati on file path
  --save_dir SAVE_DIR
    Save directory
  --metrics METRICS [METRICS ...]
    List of metrics for benchmarking (e.g.,
    WER, CER, Levenshtein ratio)
  --model MODEL
    Model to be evaluated (e.g., Tesseract OCR,
    KrakenOCR, EasyOCR)
  --data_dir DATA_DIR
    Path to the data directory containing the dataset
  --tesseract_psm TESSERACT_PSM
    Tesseract OCR page segmentation mode (PSM)
  --tesseract_oem TESSERACT_OEM
    Tesseract OCR engine mode (OEM)
  --trained_model_url TRAINED_MODEL_URL
    Tesseract OCR trained model url
  --TesseractOCR_path TESSERACTOCR_PATH
    Tesseract OCR executable path
  --kraken_url KRAKEN_URL
    Kraken OCR trained model url
  --text_direction TEXT_DIRECTION
    Text direction for Kraken OCR (e.g. horizontal-lr)
  --easyocr_detail EASYOCR_DETAIL
    EasyOCR detail level
  --image_processing_width IMAGE_PROCESSING_WIDTH
    Width for image processing
  --image_processing_height IMAGE_PROCESSING_HEIGHT
    Height for image processing
  --binarize Binarize image
  --grayscale
    Convert image to grayscale
```
## Roadmap

**Visualizations**: The HICMA OCR Benchmarking Tool should generate interactive visualizations and charts to help users visualize the results more intuitively. These visualizations aid in identifying patterns and areas for improvement in the OCR models.
See the [open issues](https://github.com/anisdismail/HICMA-benchmark/issues) for an extended list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!--LICENSE -->
## License

The HICMA dataset and its benchmark are publicly available, and are published for research purposes under the Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) licence. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

[Anis Ismail](https://linkedin.com/in/anisdimail) - anis[dot]ismail[at]lau[dot]edu



<!-- ACKNOWLEDGEMENTS 
## Acknowledgements

* []()
-->



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/anisdismail/HICMA-benchmark.svg?style=for-the-badge
[contributors-url]: https://github.com/anisdismail/HICMA-benchmark/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/anisdismail/HICMA-benchmark.svg?style=for-the-badge
[forks-url]: https://github.com/anisdismail/HICMA-benchmark/network/members
[stars-shield]: https://img.shields.io/github/stars/anisdismail/HICMA-benchmark.svg?style=for-the-badge
[stars-url]: https://github.com/anisdismail/HICMA-benchmark/stargazers
[issues-shield]: https://img.shields.io/github/issues/anisdismail/HICMA-benchmark.svg?style=for-the-badge
[issues-url]: https://github.com/anisdismail/HICMA-benchmark/issues
[license-shield]: https://img.shields.io/badge/license-CC--BY--NC--4.0-green?style=for-the-badge
[license-url]: https://github.com/anisdismail/HICMA-benchmark/LICENSE
