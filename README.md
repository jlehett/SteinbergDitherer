# FLOYD-STEINBERG DITHERING

![An example picture](https://github.com/jlehett/SteinbergDitherer/blob/master/Examples/TwistedFate.png)

<p>Simple Python program that applies a Floyd-Steinberg dithering effect to a .png or .jpg file. If you aren't sure what the Floyd-Steinberg dithering effect is, check this wikipedia article - https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering</p>

## Use

<p>Run main.py - It will provide you with a file selection dialog. Choose whatever picture you want to dither.</p>
<p>The program will then show the available options on the command line. First, you choose a dithering method. You can either choose to render the image in a 2-tone black and white image, or you can choose to use an RGB palette dithering method.</p>
<p>If you select the RGB palette option, an additional choice will appear. You can then decide whether to have the program pick a completely random palette, or if it should select random values found in the image itself to make up the palette. After you choose one of these options, you must specify how many colors should be available in the palette.</p>
<p>Once you have selected your options, the program will start to apply the dithering effect. Once it is done, a window displaying the picture will appear. You can press 's' to save it to the project home folder or 'ESCAPE' to close the window.</p>
