from pathlib import Path

import matplotlib.pyplot as plt


def _set_style(name: str):
    try:
        plt.style.use(
            Path(Path(__file__).resolve().parent,
                 f'style_sheets/{name}.mplstyle'))
    except OSError:
        raise Exception("Sorry, either you mispelled the journal name or "
                        "the style doesn's exist yet!")


class AAS:
    """
    Sets graphics style to match American Astronomical Society journals.
    Provides two different graphics width options: column (3.5 inches) and
    full-page (7.3 inches).
    """

    def __init__(self):
        """
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
        _set_style('AAS')

    @property
    def column_width(self) -> float:
        return 3.5

    @property
    def page_width(self) -> float:
        return 7.3


def set_aas_style():
    return AAS()


class AGU:
    """
    Sets graphics style to match American Geophysical Union (JGR) journals.
    Provides three different graphics width options: column (3.5 inches),
    full-text (5.4 inches) and full-page (7.3 inches). Also provides the blue
    color used in lines and section labels.
    """

    def __init__(self):
        """
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


def set_agu_style():
    return AGU()
