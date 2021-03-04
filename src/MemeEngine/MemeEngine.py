from PIL import Image, ImageDraw
import os
import random


class MemeEngine:
    """This class has the following functionalities,
        # Resize
        # draw text
        # Save modified image

    This class can only handle two file formats; '.jpg' and '.png'. It can be extended by modifying the 'self._extensions' variable.
    """
    def __init__(self, dst_folder):
        self.dst_folder = dst_folder

    def resize_image(self, img, width=500):
        """Resize image by the given width while maintaining aspect ratio
        @params:
            loaded_img : obj
                image object opened with PIL
            width: int
            width to resize the image with
        @return:
            resized_img: obj
                resized image
        """
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        return img

    def draw_text(self, img, text, author):
        """ Draw text to the image
        We calcalute the x and y axis base on the shape of the image and the size of the text
        so that we don't overflow the text on the image

        @params:
            resized_img: obj
                image that has been resized to the required shape
            text: str
                text that represents the body of the quote
            author: str
                The author of the quote
        @return:
            resized_img: obj
                the captioned image
        """

        draw = ImageDraw.Draw(img)
        text = text.encode("utf-8")
        text = str(text, "latin-1")
        x = random.randint(0, 200)
        y = random.randint(0, x)
        draw.text((x, y), f'{text} {author}', fill='white')
        return img

    def make_meme(self, img_path, text, author, width=500):
        """Controls the process of loading image with PIL, resizing and captioning the image
        It makes use of methods defined above.

        @param:
            img_path: str
                path containing the image to load, resize and caption
            text: str
                text that represents the body of the quote
            author: str
                The author of the quote
            width: int
                width to resize the image with
        @return:
            captioned_path: str
                path to the captioned image
        """
        img = self.resize_image(Image.open(img_path), width)
        img = self.draw_text(img, text, author)
        out_path = os.path.basename(img_path)
        img.save(out_path)
        return out_path
