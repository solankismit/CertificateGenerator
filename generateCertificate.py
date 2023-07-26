import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from names import list_name

class GenerateCertificate:
    def __init__(self,font_size=98,font_path="fonts/DancingScript-SemiBold.ttf",certificate_path="certificate.png"):
        a = self.getLineFromImage(certificate_path)
        self.color = self.getTextColorByImage(certificate_path)
        self.certi_path = certificate_path
        self.line_start_x = a[0]+50
        self.line_end_x = a[2]+50
        self.line_y = a[1]-30+50 if self.isLandScape else a[1]-100
        self.font_size = font_size
        self.font_path = font_path

    def generate_certificate(self,index,text,list_length=len(list_name)):

        # Configuration
        font_path = self.font_path if self.font_path else "fonts/DancingScript-SemiBold.ttf"
        line_start_x = self.line_start_x if self.line_start_x else 50
        line_end_x = self.line_end_x if self.line_end_x else 50
        line_y = self.line_y if self.line_y else 50
        font_size = self.font_size if self.font_size else 50

        # DON'T CHANGE ANYTHING BELOW THIS LINE

        font = ImageFont.truetype(font_path, font_size)

        # Get Certification text
        image = np.array(cv2.imread(self.certi_path))

        # Convert the image to PIL Image
        pil_image = Image.fromarray(image)

        # Create a Draw object
        draw = ImageDraw.Draw(pil_image)
        color = self.color  # Blue color

        # Get the text size in pixels
        text_width = draw.textlength(text, font=font)
        text_bbox = font.getbbox(text)
        text_height = text_bbox[3] - text_bbox[1]

        text_offset_x =  ((line_start_x + line_end_x) - text_width) //2 
        text_offset_y = line_y - (text_height) 


        position = (text_offset_x, text_offset_y)
        # Put the text on the image using the custom font
        draw.text(position, text, font=font, fill=color,align="center")


        # Convert the PIL Image back to a NumPy array
        output_image = np.array(pil_image)
        # Save the image
        cv2.imwrite(f"certificate{index+1}.jpg", output_image)
        print("Processing certi {}/{}".format(index + 1, list_length))



    def getLineFromImage(self,image_path):
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Ignore Border
        gray = gray[50:-50,50:-50]
        edges = cv2.Canny(gray, 75, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, maxLineGap=250)
        for line in lines:
            if line[0][1] == line[0][3] and line[0][2]-line[0][0] > 600:
                x1, y1, x2, y2 = line[0]
                print(x1+50, y1+50, x2+50, y2+50)
                return line[0]
    
    def getTextColorByImage(self,image_path):
        image = cv2.imread(image_path)
        self.isLandScape = True if image.shape[1] > image.shape[0] else False
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = gray[50:-50,50:-50]
        gray = np.sort(np.array(gray).flatten())
        median = gray[len(gray) // 2]
        print(median)
        if median > 127:
           return (0,0,0)
        else:
          return (255,255,255)
         
    
if __name__ == "__main__":
    gc = GenerateCertificate( certificate_path="certi3.png")
    for index,name in enumerate(list_name):
        name = name.strip().title()
        gc.generate_certificate(index,name)
        break