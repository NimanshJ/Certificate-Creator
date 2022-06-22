from PIL import Image, ImageDraw, ImageFont
import math


def generator():
    # only generates 1 image currently
    print("started")
    img = Image.open("blank_merit.png", mode='r')
    draw = ImageDraw.Draw(img)

    name = "Hello World"
    nameX = 428-(len(name)-11)*7
    font = ImageFont.truetype(
        "Outfit-Medium.ttf",
        math.floor(35-(len(name)-11)*0.5)
    )
    txtSize = font.getsize(name)
    draw.text(
        (nameX, 220),
        name,
        fill='#14C862',
        font=font
    )
    font = ImageFont.truetype(
        "Outfit-Medium.ttf",
        30-(len(name)-11)*1
    )
    draw.text(
        ((nameX+txtSize[0]), 225),
        "  | 13K",
        fill=(255, 255, 255),
        font=font
    )

    font = ImageFont.truetype(
        "Outfit-Light.ttf",
        20
    )
    draw.text(
        (img.width*0.54, 325),
        "1st Position in design event.",
        fill="#14C862",
        font=font
    )

    img.save("Test1.png")
    print("done")


if __name__ == "__main__":

    mail = "temp@mail.com"  # Will be imports from env
    key = "password"  # Will be imports from env
    generator()
