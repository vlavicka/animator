import Image, ImageDraw

class BitmapLayer(object):
    def __init__(self, name, width, height):
        self.name = name
        self.canvas = Image.new("RGBA", (width, height), (255,255,255))
        self._current_color = (0, 0, 0)

    @property
    def size(self):
        return self.canvas.size

    def render(self):
        return self.canvas

    def draw_line(self, start_point, end_point):
        draw = ImageDraw.Draw(self.canvas)
        draw.line([start_point, end_point], fill=self._current_color)

    def draw_point(self, point):
        draw = ImageDraw.Draw(self.canvas)
        draw.point(point, fill=self._current_color)

