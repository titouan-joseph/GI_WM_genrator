from PIL import Image, ImageDraw, ImageFont

height = 150
width = 600

# Color
transparent = (0, 0, 0, 0)
white = (255, 255, 255)

name = "C.Titouan"

# Set transparent background
background = Image.new("RGBA", (width, height), transparent)

# Load logo and font
logo = Image.open('assets/img/logo_transparent.png')
font32 = ImageFont.truetype("assets/font/yugothic-medium.otf", 32)
font72 = ImageFont.truetype("assets/font/yugothic-medium.otf", 72)

# Rectangle
rect = Image.new('RGB', (65, 15), white)

# Copy logo
background.paste(logo, (0, 0))
background.paste(rect, (190, 110))
background.paste(rect, (525, 110))

# Write on WM
drawer = ImageDraw.Draw(background)
drawer.text((262, 100), "Graines d'images", font=font32)
nameSize = font72.getsize(name)
if nameSize[0] > 410:
    print("pb avec ce nom, trop grand")
    exit()

drawer.text((190+(205-(nameSize[0]/2)), 20), name, font=font72)

# Save to png
background.save(f"WM_{name}.png", "PNG")
