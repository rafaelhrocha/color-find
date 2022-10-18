import colorgram as cg
import webcolors as wc

class Colors():
    def __init__(self) -> None:
        self.colors = []
        
    def getImage():
        pass

    def getColors(self, imagem):
        self.colors = cg.extract(imagem, 4)
        for color in self.colors:
            colorToFind = color.rgb
            try:
                nameColor = wc.rgb_to_name((colorToFind.r,colorToFind.g,colorToFind.b), spec='css3')
            except ValueError:
                nameColor = self.getClosedColor(colorToFind)
            
            print(nameColor, colorToFind)

    def getClosedColor(self, color):
        min_color = {}
        for key, name in wc.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = wc.hex_to_rgb(key)
            rd = (r_c - color[0]) ** 2
            gd = (g_c - color[1]) ** 2
            bd = (b_c - color[2]) ** 2
            min_color[(rd + gd + bd)] = name
        return min_color[min(min_color.keys())]

a = Colors()
a.getColors('imagem.png')