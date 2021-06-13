# Copyright Kee (c) 2021. All rights reserved.
# Any code below is written by it's owner,
# and the copyright belongs to it's owner

# User Agreement:
# You can re-edit, re-code, and use as much as you want
# Just don't replace my copyright

# open-source <http://github.com/rushkii/welcome-banner/

from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from typing import Optional
import textwrap, os

class WelcomeBanner:
    _fonts = "assets/font"
    _imgs = "assets/image"
    _stickers = 'assets/image/stickers'
    _font = f"{_fonts}/Chocolate Covered Raindrops BOLD.ttf"

    def __init__(self, name:Optional[str], message:Optional[str], frame:Optional[str], use_sticker:Optional[bool]) -> None:
        self.name = str(name)[0:50]
        self.message = str(message)[0:100]
        self.frame = frame
        self.use_sticker = use_sticker
        self.__image = Image.open(f"{self._imgs}/welcome_banner2.png")

    def set_background(self, impath):
        self.__image = Image.open(impath)

    def set_frame(self, path=None):
        if self.frame is None or not self.frame or self.frame != "":
            path = f"{self._imgs}/395aebb5f536f65d7817d38f0d1c1925-edited.png" # default
        elif path is not None:
            path = path
        else:
            path = self.frame
        im = Image.open(path)
        im = im.resize((343,313))
        self.__image.paste(im, (51,34))

    def add_sticker(self):
        import random
        pack = random.choice(os.listdir(self._stickers)[:-1])
        sticker = random.choice(os.listdir(self._stickers+"/"+pack))
        simg = Image.open(f"{self._stickers}/{pack}/{sticker}").resize((210,210)).convert('RGBA') # resize((w,h))
        self.__image.paste(simg, (0, 580), simg) # x,y

    def add_message(self):
        _,H = self.__image.size
        font = ImageFont.truetype(self._font, size=70)
        draw = ImageDraw.Draw(self.__image)
        wrapper = textwrap.TextWrapper(width=15) 
        word_list = wrapper.wrap(text=self.message)
        caption = '\n'.join(line.center(80) for line in word_list)
        _,h = draw.textsize(caption, font)
        draw.text((700, (H-h)/2), caption, fill='rgb(0,0,0)', font=font)

    def add_name(self): # Help me to make it as a center text in top bar for placing a name tag
        font = ImageFont.truetype(self._font, size=50)
        capt = self.name
        draw = ImageDraw.Draw(self.__image)
        draw.text((443,36), capt, fill='rgb(255, 255, 255)', font=font)

    def add_watermark(self):
        font = ImageFont.truetype(self._font, size=50)
        draw = ImageDraw.Draw(self.__image)
        draw.text((1120,720), "Generated by @NekohaShzkBot", fill='rgb(255, 255, 255)', font=font)

    def __create_all(self):
        self.set_frame()
        self.add_watermark()
        if self.use_sticker:
            self.add_sticker()
        self.add_name()
        self.add_message()

    def save(self, saveAs=None):
        self.__create_all()
        if saveAs == "" or not saveAs or saveAs is None:
            import uuid
            saveAs = str(uuid.uuid4())
        savefile = f"{saveAs}{'' if saveAs.endswith('.png') or saveAs.endswith('.jpg') else '.png'}"
        self.__image.save(savefile)
        return savefile

    def show(self):
        self.__create_all()
        return self.__image.show()
