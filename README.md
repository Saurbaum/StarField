# StarField
A Python/PyGame application to display a pseudo random star field and overlays that would be reminiscent of the computer screens in the background on a space ship in a low budget sci-fi movie

# Running
This was wrtting in Python 3.5.1 and made use of PyGame (pygame-1.9.2a0-cp35-none-win_amd64.whl from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame) in 64bit Windows.

There is no reason it shoudn't work in 32bit.

In making it high DPI aware it's possible I've made it not cross platform.  Needs testing to be sure.

# Starfield
This is the main application that creates the stars and overlay.
It will create 40 random stars every few seconds.
The Overlay consists of a targeting reticle, a grid and a text display of the current location and a history of the coordinates that the targeting reticle has been too.

[See an example here] (ScreenShot.png)