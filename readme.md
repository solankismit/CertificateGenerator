# Certificate Generator

This is a Streamlit web application that generates certificates using user-provided data and a custom certificate template.

## Demo

A live demo of the Certificate Generator application is available on Streamlit Sharing. You can access it [here](https://share.streamlit.io/your-username/certificate-generator/app.py).

Note: The live demo may have limited resources and may not be available at all times. If you encounter any issues, please try running the application locally using the instructions provided in the "Usage" section.


## Getting Started

### Prerequisites

- Python 3.7 or higher
- Streamlit
- pandas
- Pillow
- tqdm

### Installation

1. Clone the repository:
shell git clone https://github.com/your-username/certificate-generator.git

2. Navigate to the project directory:
shell cd certificate-generator

3. Install the required dependencies:
shell pip install -r requirements.txt


## Usage

1. Run the Streamlit app: shell streamlit run app.py

2. Upload an Excel or CSV file containing the names of the recipients. The file should have a single column named "Name".

3. Adjust the font size and upload the font file (.ttf) and the certificate template image (.png, .jpg, .jpeg).

4. Click the "Preview Sample Certificate" button to see a sample certificate with the user-provided text.

5. Click the "Generate and Download Certificates" button to generate the certificates for all the names in the uploaded file. The generated certificates will be added to a zip file that can be downloaded.

## Customization

- You can set "certificate.png" file with your own image file from streamlit app. Make sure the image contains LINE to add name in it and layout for the certificate.

- The font size and font file can be adjusted to match your desired style.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
