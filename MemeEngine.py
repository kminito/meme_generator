from PIL import Image, ImageFont, ImageDraw
import random


class MemeEngine:
    """Class to generate actual meme file."""

    def __init__(self, path):
        """Initiate meme engine with path where store produced meme files."""
        self.temp_dir = path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Gernerate Meme with given img, text, and author."""
        out_path = f"{self.temp_dir}/{random.randint(0,1000000)}.png"

        if width >= 500:
            width = 500

        with Image.open(img_path) as img:
            ratio = img.height / img.width
            height = width * ratio
            img = img.resize((int(width), int(height)))
            font_size = int(img.height/20)

            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", font_size)

            x_loc = random.randint(0, int(img.width/4))
            y_loc = random.randint(0, int(img.height-font_size*2))

            draw.text((x_loc, y_loc), text, font=font, fill=(0, 0, 0))
            draw.text((int(x_loc*1.2), y_loc+font_size), " - "+author, font=font)

            img.save(out_path)

        return out_path
