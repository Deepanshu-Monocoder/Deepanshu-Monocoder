from rembg import remove
from PIL import Image
import cv2
import numpy as np
from pathlib import Path


def remove_background(input_path, output_path):
    input_image = Image.open(input_path).convert("RGBA")

    output_image = remove(input_image)

    # White background
    white_bg = Image.new("RGBA", output_image.size, (255, 255, 255, 255))
    white_bg.paste(output_image, mask=output_image)

    # Convert to grayscale
    img = cv2.cvtColor(np.array(white_bg), cv2.COLOR_RGBA2GRAY)

    # Improve contrast
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    img = clahe.apply(img)

    # Save final image
    cv2.imwrite(str(output_path), img)


if __name__ == "__main__":
    input_file = Path("assets/photo.jpg")
    output_file = Path("assets/source_prepped.png")

    remove_background(input_file, output_file)

    print("Background removed successfully!")