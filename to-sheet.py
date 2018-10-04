#!/usr/bin/env python

from gimpfu import *

def to_sheet(image):
    pdb.gimp_undo_push_group_start(image)

    width = image.width
    image.resize(width * len(image.layers),image.height,0,0)
    for i,layer in enumerate(image.layers): layer.translate(i * width,0)
    image.merge_visible_layers(CLIP_TO_IMAGE)

    pdb.gimp_undo_push_group_end(image)


register("python-fu-to-sheet",
         "turns a bunch of layers into a sprite sheet",
         "yee",
         "daly","daly","2016",
         "to sheet",
         "RGB*",
         [(PF_IMAGE, "image", "Input image", None)],
         [],
         to_sheet,
         menu="<Image>/Filters/Sheet")

main()
