#! /usr/bin/python3
from PIL import Image, ImageDraw, ImageFont
import argparse


def generateWM(name, verbose=False):
    if verbose:
        print(f"Creating WM for {name}")

    # Size
    height = 140
    width = 690

    # Color
    transparent = (0, 0, 0, 0)
    white = (255, 255, 255)

    # Set transparent background
    background = Image.new("RGBA", (width, height), transparent)

    # Load logo and font
    logo = Image.open('assets/img/logo_transparent.png')
    font32 = ImageFont.truetype("assets/font/yugothic-medium.otf", 32)
    font72 = ImageFont.truetype("assets/font/yugothic-medium.otf", 72)

    # Rectangle
    rect = Image.new('RGB', (110, 15), white)

    # Copy logo & Rectangle
    background.paste(logo, (0, 0))
    background.paste(rect, (190, 110))
    background.paste(rect, (width-110, 110))

    # Write "Graines d'images" on WM
    txt = "Graines d'images"
    drawer = ImageDraw.Draw(background)
    drawer.text((190+(250-(font32.getsize(txt)[0]/2)), 100), txt, font=font32)

    # Check size of name
    nameSize = font72.getsize(name)
    if nameSize[0] > 500:
        print(nameSize)
        print(f"The name {name} is to big !")
        return False
    # Write name on WM
    drawer.text((190+(250-(nameSize[0]/2)), 55-(nameSize[1]/2)), name, font=font72)

    # Save to png
    background.save(f"WM_{name}.png", "PNG")
    if verbose:
        print(f"WM created")
    return True


if __name__ == '__main__':
    # Parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", "-n", help="The name will be write on WM")
    parser.add_argument("--multipleName", "-m", help="Generate multiple WM", nargs='+')
    parser.add_argument("--file", "-f", help=".txt file with names. One per line")
    parser.add_argument("--verbose", "-v", help="Verbose mode", action="store_true")

    # Get arguments
    args = parser.parse_args()

    if args.name:
        generateWM(args.name, args.verbose)

    if args.multipleName:
        for pseudo in args.multipleName:
            generateWM(pseudo, args.verbose)

    if args.file:
        with open(args.file, "r") as file:
            for line in file.readlines():
                generateWM(line.rsplit('\n')[0], args.verbose)
