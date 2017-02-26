# StarField
A Python/PyGame application to display a pseudo random star field and overlays that would be reminiscent of the computer screens in the background on a space ship in a low budget sci-fi movie

# Running
Before first run make use of pip to install PyGame.
	pip install pygame

This was wrtting in Python 3.5.1 and made use of PyGame in 64bit Windows.

There is no reason it shoudn't work in 32bit.

On Windows it his high DPI aware and should scale nicely.

You can press 'Space' to regenerate the starfield on demand else it will happen every few seconds.

Press 'Escape' to quit

# Starfield
This is the main application that creates the starfield scanner.

It will render and update the scanner on the application loop.  The two are seperate so that second displays can be updating and switched to for drawing one at a time.

# StarfieldScanner
This will create 40 random stars every few seconds.
The Overlay consists of a targeting reticle, a grid and a text display of the current location and a history of the coordinates that the targeting reticle has been too.

[See an example here] (ScreenShot.png)