from typing import Union, List, Optional
import random

from pypalettes.utils import _get_palette


def load_palette(
    name: Union[str, List[str]] = "random",
    reverse: bool = False,
    keep_first_n: Optional[int] = None,
    keep_last_n: Optional[int] = None,
    keep: Optional[List[bool]] = None,
    repeat: int = 1,
    shuffle: Union[bool, int] = False,
) -> list[str]:
    """
    Load a color palette from one of the 2500+ available palettes.

    You can find all valid palette names [here](https://python-graph-gallery.com/color-palette-finder/){target="_blank"}

    Args:
        name: Name of the palette
        reverse: Whether to reverse the order of the colors or not
        keep_first_n: Keep only the first n colors of the palette
        keep: Specify which colors to keep in the palette
        repeat: The number of times the palette must be present in
            the output. Used to access larger palettes that are repeated.
        shuffle: Used to mix the order of colors. If an integer is
            supplied, it will be used as the seed.

    Returns:
        A list of colors.
    """

    palette: dict = _get_palette(name, reverse, keep_first_n, keep_last_n, keep, repeat)
    hex_list: list = palette["hex_list"]

    if shuffle:
        if isinstance(shuffle, int):
            random.seed(shuffle)
        random.shuffle(hex_list)

    return hex_list
