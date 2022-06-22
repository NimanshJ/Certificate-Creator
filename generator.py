from PIL import Image, ImageDraw, ImageFont
import math
import json

# Kenobi Alingment Dekhliyo.
# Nimansh thoda Test karliyo aur apna function paste kardiyo SEND MAIL ke naam se


def makeMerit(per):
    img = Image.open("blank_merit.png", mode='r')
    draw = ImageDraw.Draw(img)

    name = per["name"]
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
        "  | "+str(per["class"])+''+str(per["section"]),
        fill=(255, 255, 255),
        font=font
    )

    font = ImageFont.truetype(
        "Outfit-Light.ttf",
        20
    )
    draw.text(
        (img.width*0.53, 325),
        str(per["position"])+"# Position in "+str(per["field"])+"event.",
        fill="#14C862",
        font=font
    )
    img.save("Merit.png")


def makePart(per):
    img = Image.open("blank_participation.png", mode='r')
    draw = ImageDraw.Draw(img)

    name = per["name"]
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
        "  | "+str(per["class"])+''+str(per["section"]),
        fill=(255, 255, 255),
        font=font
    )

    font = ImageFont.truetype(
        "Outfit-Light.ttf",
        20
    )
    draw.text(
        (608, 302),
        str(per["field"])+" event.",
        fill="#14C862",
        font=font
    )
    img.save("Partake.png")


def conversion(flag):
    i1 = Image.open('Partake.png')
    im1 = i1.convert('RGB')
    im1.save("Certificate.pdf")
    if(flag):
        i2 = Image.open('Merit.png')
        im2 = i2.convert('RGB')
        im2.save("Merit.pdf")


def generator():
    f = open('data.json')
    res = json.load(f)
    dt = res["data"]

    for i in dt:
        makePart(i)
        if i["won"]:
            makeMerit(i)
        conversion(i["won"])
        # sendMail()

    f.close()


if __name__ == "__main__":
    generator()
