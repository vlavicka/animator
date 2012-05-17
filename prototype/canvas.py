from PIL import Image, ImageDraw


def create_transparent_image(width, height):
    image = Image.new("RGBA", (width, height), "#ffffff")
    mask = Image.new("L", image.size, color=0)
    image.putalpha(mask)
    return image


class PencilTool(object):
    def __init__(self):
        self.pen = "#000000"
        self.width = 20

    def get_drawing_context(self, image):
        return ImageDraw.Draw(image)

    def point(self, image, x, y):
        draw = self.get_drawing_context(image)
        if self.width == 1:
            draw.point((x, y), fill=self.pen)
        else:
            step = self.width / 2
            if self.width % 2:
                draw.ellipse((x - step, y - step, x + step, y + step), outline=self.pen, fill=self.pen)
            else:
                draw.ellipse((x, y, x + step, y + step), outline=self.pen, fill=self.pen)
    

class BitmapLayer(object):
    def __init__(self, width, height):
        self.layer = create_transparent_image(width, height)
        self.tools = PencilTool()

    def point(self, x, y):
        self.tools.point(self.layer, x, y)

    def render(self):
        return self.layer

        
class Canvas(object):
    def __init__(self, width, height):
        self.size = (width, height)
        self.layers = [BitmapLayer(width, height)] # create default bitmap layer

    def point(self, x, y):
        self.layers[0].point(x, y)

    def render(self):
        image = Image.new("RGBA", self.size, "#ffffff")
        for layer in self.layers:
            source = layer.render()
            image.paste(source, None, source)
        return image

def main():
    canvas = Canvas(100, 100)
    canvas.point(10, 10)
    image = canvas.render()
    image.save('canvas.dump.png')

if __name__ == "__main__":
    main()
