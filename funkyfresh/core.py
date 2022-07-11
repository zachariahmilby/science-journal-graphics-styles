from pathlib import Path

import matplotlib.pyplot as plt


color_dict = {'red': '#D62728', 'orange': '#FF7F0E', 'yellow': '#FDB813',
              'green': '#2CA02C', 'blue': '#0079C1', 'violet': '#9467BD',
              'cyan': '#17BECF', 'magenta': '#D64ECF', 'brown': '#8C564B',
              'darkgrey': '#3F3F3F', 'grey': '#7F7F7F', 'lightgrey': '#BFBFBF',
              'black': '#000000', 'white': '#FFFFFF'}


def _set_style(name: str):
    try:
        plt.style.use(
            Path(Path(__file__).resolve().parent,
                 f'style_sheets/{name}.mplstyle'))
    except OSError:
        raise Exception("Sorry, either you mispelled the journal name or "
                        "the style doesn's exist yet!")


class AAS:

    def __init__(self):

        _set_style('AAS')

    @property
    def column_width(self) -> float:
        return 3.5

    @property
    def page_width(self) -> float:
        return 7.3


class AGU:

    def __init__(self):
        _set_style('AAS')

    @property
    def column_width(self) -> float:
        return 3.5

    @property
    def text_width(self) -> float:
        return 5.6

    @property
    def page_width(self) -> float:
        return 7.5

    @property
    def blue(self) -> str:
        return '#004174'


class PersonalWhitepaper:

    def __init__(self):
        _set_style('personal_whitepaper')

    @property
    def page_width(self) -> float:
        return 4.7917

    @property
    def colors(self) -> dict:
        return color_dict


def set_aas_style():
    """
    Sets graphics style to match American Astronomical Society journals.
    Provides two different graphics width options: column (3.5 inches) and
    full-page (7.3 inches).

    Examples
    --------
    Get the column-width in inches:
    >>> style = set_aas_style()
    >>> style.column_width
    3.5

    Get the page-width in inches:
    >>> style = set_aas_style()
    >>> style.page_width
    7.3
    """
    return AAS()


def set_agu_style():
    """
    Sets graphics style to match American Geophysical Union (JGR) journals.
    Provides three different graphics width options: column (3.5 inches),
    full-text (5.4 inches) and full-page (7.3 inches). Also provides the blue
    color used in lines and section labels. Default figure size width is
    4.7917 pt.

    Examples
    --------
    Get the column-width in inches:
    >>> style = set_agu_style()
    >>> style.column_width
    3.5

    Get the text-width in inches:
    >>> style = set_agu_style()
    >>> style.text_width
    5.6

    Get the page-width in inches:
    >>> style = set_agu_style()
    >>> style.page_width
    7.5

    Get the AGU blue color as a hexadecimal string
    >>> style = set_agu_style()
    >>> style.blue
    '#004174'
    """
    return AGU()


def set_personal_whitepaper_style():
    """
    Sets graphics style to match the default 10-point LaTeX article class I use
    for school papers, reports, etc. Also has a custom color dictionary.

    Examples
    --------
    Get the column-width in inches:
    >>> style = set_personal_whitepaper_style()
    >>> style.page_width
    4.7917

    Get the blue color from the custom color dictionary:
    >>> style = set_personal_whitepaper_style()
    >>> style.colors['blue']
    '#0079C1'

    Get the available colors from the custom color dictionary:
    >>> style = set_personal_whitepaper_style()
    >>> style.colors.keys()
    dict_keys(['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'cyan', 'magenta', 'brown', 'darkgrey', 'grey', 'lightgrey', 'black', 'white'])
    """

    return PersonalWhitepaper()
