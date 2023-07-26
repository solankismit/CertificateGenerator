import cv2

from names import list_name

# list_name = ["Akash Vinodbhai Bagia"]
for index, name in enumerate(list_name):
    template = cv2.imread("certificate.png")
    # Get middle of text
    (text_width, text_height) = cv2.getTextSize(
        name, cv2.FONT_HERSHEY_SIMPLEX, 3, 6
    )[0]


    
    # # draw Line in image
    # cv2.line(template, (749, 689), (1859, 689), (0, 0, 0), 2)
    # print(text_width, text_height)
    text_offset_x =  ((1859+749) - text_width) //2 
    text_offset_y = 643 + (text_height) //2

    
    # Calculate the x-offset based on the image width and text width
    # image_width = template.shape[1]
    # text_offset_x = (image_width - text_width) // 2

    # # Calculate the y-offset based on the image height and text height
    # image_height = template.shape[0]
    # text_offset_y = 639 + (text_height) //2


    # # Calculate the center of the line on the x-axis
    # line_start_x = 749
    # line_end_x = 1859
    # line_center_x = (line_start_x + line_end_x) // 2

    # # Calculate the x-coordinate for the text to align with the line's center
    # text_offset_x = line_center_x - (text_width // 2)


    # Add text to image
    cv2.putText(
        template,
        name,
        (text_offset_x, text_offset_y),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (0, 0, 255),
        6,
        cv2.LINE_AA,
    )
    cv2.imwrite(f"generate/{name}.jpg", template)
    # cv2.imwrite(f"generate//{name}.jpg", template)
    print("Processing certi {}/{}".format(index + 1, len(list_name)))
    # if index ==3:
    #     break
    if index == len(list_name) - 1:
        print("All certificates generated successfully")
