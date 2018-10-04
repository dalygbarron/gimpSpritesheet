#!/usr/bin/env python

from gimpfu import *

def from_sheet(image, sprites):
    layer = image.layers[0]
    width = layer.width
    frameWidth = int(width / sprites)

    pdb.gimp_undo_push_group_start(image)

    for i in reversed(range(int(sprites))):
        d = layer.copy()
        image.add_layer(d,0)
        d.resize(frameWidth,image.height,i * -frameWidth,0)
        d.translate(i * -frameWidth,0)
    image.resize(frameWidth,image.height,0,0)
    image.remove_layer(layer)
    pdb.gimp_undo_push_group_end(image)


register("python-fu-from-sheet",
         "turns a sprite sheet into a bunch of layers",
         "yee",
         "daly","daly","2018",
         "from sheet",
         "RGB*",
         [
            (PF_IMAGE, "image", "Input image", None),
            (PF_SPINNER, "sprites", "Number of sprites", 1, (2,100,1))
         ],
         [],
         from_sheet,
         menu="<Image>/Filters/Sheet")

main()
