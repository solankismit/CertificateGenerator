import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import base64
import io
import zipfile
from generateCertificate import GenerateCertificate
import random

def generate_certificates(names, font_size, font_path, certificate_path, only_preview=False):
    # Generate certificates
    gc = GenerateCertificate(font_size, font_path, certificate_path)

    certificates = []
    if only_preview:
        # Randomly select 1 name
        
        names = random.sample(names, 1)
        gc.generate_certificate(0, names[0])
        # Save the generated certificate as a base64-encoded string
        img = Image.open(f"certificate{1}.jpg")
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')
        certificates.append(img_base64)

    else:
        for index, name in enumerate(names):
            name = name.strip().title()
            gc.generate_certificate(index, name)

            # Save the generated certificate as a base64-encoded string
            img = Image.open(f"generate/certificate{index + 1}.jpg")
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')

            certificates.append(img_base64)

    return certificates


def main():
    st.set_page_config(page_title="Certificate Generator", layout="wide")

    st.markdown('<link href="style.css" rel="stylesheet">', unsafe_allow_html=True)
    st.title("Certificate Generator")
    st.markdown("---")

    # col1, col2 = st.columns(2)

    certificates = []
    # with col1:
    uploaded_file = st.file_uploader("Upload Excel or CSV File of Names (There should be only one column called \"Name\")", type=["xlsx", "csv"])
    if uploaded_file is not None:

            st.markdown('<div class="drag-drop-container">', unsafe_allow_html=True)
            st.markdown('<i class="drag-drop-icon fas fa-cloud-upload-alt"></i>', unsafe_allow_html=True)
            st.markdown('<p class="drag-drop-text">Drag and drop file here or click to upload</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            try:
                if uploaded_file.type == "application/vnd.ms-excel":
                    df = pd.read_excel(uploaded_file)
                else:
                    df = pd.read_csv(uploaded_file)

                names = df["Name"].tolist()

                font_size = st.slider("Font Size", 50, 150, 98)
                font_path = st.file_uploader("Font File", type=["ttf"])
                certificate_path = st.file_uploader("Certificate Image", type=["png", "jpg", "jpeg"])

                if st.button("Preview Sample Certificate"):
                    if font_path is None or certificate_path is None:
                        st.error("Please upload the font file and certificate image.")
                    else:
                        # Save the uploaded files
                        with open("font.ttf", "wb") as f:
                            f.write(font_path.read())
                        with open("certificate.png", "wb") as f:
                            f.write(certificate_path.read())

                        # Generate certificates
                        certificates = generate_certificates(names, font_size, "font.ttf", "certificate.png", only_preview=True)
                        st.success("Sample Certificate has been generated.")

                        # Display the sample certificate with user-given text
                        st.markdown("### Sample Certificate Preview")
                        sample_img = Image.open(io.BytesIO(base64.b64decode(certificates[0])))
                        st.image(sample_img, use_column_width=True)
                if st.button("Generate and Download Certificates"):
                    certificates = generate_certificates(names, font_size, "font.ttf", "certificate.png")
                    st.success("Sample Certificate has been generated.")
                    if font_path is None or certificate_path is None:
                        st.error("Please upload the font file and certificate image.")
                    elif len(certificates) == 0:
                        st.error("Please preview the sample certificate before generating.")
                    else:
                        # Create a zip file to store the generated certificates
                        zip_file = zipfile.ZipFile("certificates.zip", "w")

                        for index, certificate in enumerate(certificates):
                            certificate_data = base64.b64decode(certificate)

                            # Add the certificate to the zip file
                            zip_file.writestr(f"certificate_{index + 1}.jpg", certificate_data)

                        zip_file.close()
                        st.success("Certificates have been generated and added to the zip file.")


                        
                        # Provide the download link for the zip file
                        with open("certificates.zip", "rb") as f:
                            zip_data = f.read()
                            b64_zip_data = base64.b64encode(zip_data).decode("utf-8")
                            href = f'<a href="data:application/zip;base64,{b64_zip_data}" download="certificates.zip">Download Certificates</a>'
                            st.download_button("Download Certificates", data=zip_data, file_name="certificates.zip")
            except Exception as e:
                st.error(f"Error: {e}")

    
    st.markdown("---")
    st.text("Note: The generated certificates and the zip file will be saved in the same directory as this script.")


if __name__ == "__main__":
    main()
