# `funkyfresh`: Science Journal Graphics Styles for Matplotlib

This package provides functions which automatically set Matplotlib style 
parameters (fonts, line weights, etc.) to match those of select scientific 
journals.

## Currently-Supported Styles
- American Geophysical Union (AGU)
  - Journal of Geophyiscal Research (JGR)
  - Geophysical Research Letters (GRL)
- American Astronomical Society (AAS)
  - Astrophysical Journal Letters (ApJL)
  - Astronomical Journal (AJ)
  - Astrophysical Journal (ApJ)
  - Planetary Science Journal (PSJ)
- My personal styles:
  - LaTeX article class with 10-point STIX2 fonts

## Installation
Here are some installation instructions for the average Anaconda user, if 
you're more advanced I'm sure you can figure it out from here. (Note: in the
instructions below I will assume that you are using a virtual environment named 
`myenv`.) I've tested this using Python 3.10.
1. Activate your virtual environment:<br>
    `% conda activate myenv`
2. Install the `funkyfresh` package and its dependencies:<br>
    `% python -m pip install git+https://github.com/zachariahmilby/science-journal-graphics-styles.git`

You're now ready to use the `funkyfresh` package!

> **NOTE**<br>
> If you're using Jupyter on a Mac, including <br>
> `%config InlineBackend.figure_format = 'retina'` after you import `pyplot` 
> will make any of your inline graphics displayed with `plt.show()` higher 
> resolution.

## Usage
Usage is pretty simple. Start by importing the function for the desired style.
There are currently three options: `set_aas_style`, `set_agu_style` and 
`set_personal_whitepaper_style()`. For example, to set the style to match a JGR 
journal:
```
from funkyfresh import set_agu_style
style = set_agu_style()
```
The function returns an object which has a few parameters you might want to 
use when making figures. The AGU style includes three figure widths (column, 
text and page) and the predominant blue color used for section title font 
colors. The AAS style includes two figure widths (column and page).

To create a column-width figure with a height of 2 inches, you might do this:
```
fig = plt.figure(figsize=(style.column_width, 2))
```
If you wanted to plot sine using the JGR blue color (#004174), you could do 
this:
```
theta = np.linspace(0, 2 * np.pi, 1000)
plt.plot(theta, np.sin(theta), color=style.blue)
```
The AAS articles don't seem to have any particular house color, so it isn't an 
option.
