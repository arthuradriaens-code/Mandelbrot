import numpy as np
from matplotlib import colors
from PIL import Image #per pixel manipulatie (wat we nodig hebben)
import colorsys 

def vergelijking(z,c):
    return z*z + c

def rgb_conv(i): #converteer nummer naar een kleur
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5)) 
    return tuple(color.astype(int)) 

def kleuren(c,maximum_iteraties):
    z = 0
    for iteratie in range(1,maximum_iteraties):
        if abs(z) > 2:
            return rgb_conv(iteratie) #na welke stap divergeert -> kleur
        z = vergelijking(z,c)
    return (0,0,0) #geen kleur (r,g,b)

def mandelbrot(breedte,hoogte,maximum_iteraties):
    afbeelding = Image.new('RGB', (breedte, hoogte))
    pixels = afbeelding.load() #laadt de pixels
    # voorbeeld: pixel = pixels[0,0] verkrijg de eerste pixel zijn waarde
    for rij in range(hoogte):
        # geeft de vordering weer
        print(" %.2f %%" % (rij/ hoogte * 100.0),end='\r')
        for kolom in range(breedte):
            pixels[kolom,rij] = kleuren(complex(4*(kolom-1.2*int(breedte/2))/breedte,2*(rij-int(hoogte/2))/hoogte),maximum_iteraties)
    return afbeelding

breedte = 16384
hoogte = int(breedte/2)
maximum_iteraties = 1000

afbeelding = mandelbrot(breedte,hoogte,maximum_iteraties)
afbeelding.show()
