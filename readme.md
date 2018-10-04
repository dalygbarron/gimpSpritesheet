# About
These two plugins allow you to convert horizontal spritesheet images into a
collection of layers in gimp, and convert a collection of layers into a
horizontal stylesheet.

The primary usefulness of this comes from easy insertion and rearrangement of
animation frames within a spritesheet without having to configure a grid of the
correct size and move things around etc.

Also, when you are working with animated gifs in gimp, these are naturally in
the form of a sequence of layers, but sometimes it can actually be useful to
convert these layers into a spritesheet temporarily for the application of
special effects to every layer at once. You will find though that if you apply
the kind of effect that moves data around, that there may be "bleed" between
animation frames when using this technique, but it's kinda cool, and there are
a lot of situations where this will not occur.

# Specifically how it works
If you have a sprite sheet which you want to convert to layers, you must
click `Filters/Sheet/from sheet`, you will then be asked to enter the number
of frames in the spritesheet (which the program remembers, kindly. Once you
press ok, the sprite sheet is cut up into individual frames as layers.

If you have a bunch of layers which you want to convert to a sprite sheet,
you must click `Filters/Sheet/to sheet`, and your layers will right away
become frames in a sprite sheet in the order that they appear. All layers
of the animation are used, and they must be visible or else they will
appear as blank on the sprite sheet. It may be wise of me to later update
this so that hidden layers are simply ignored.

# How to install
If you are on linux then these plugins should be put into the folder
`~/.gimp-n.n/plug-ins/`. If you are on windows then I don't know but I would
imagine that it is similar.

# Have fun
Have fun with this plugin OR ELSE.
