from typing import Union, Optional, TYPE_CHECKING
import random
import colorsys

if TYPE_CHECKING:
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap

from pypalettes.utils import _get_palette


def load_cmap(
    name: Union[str, list[str]] = "random",
    cmap_type: str = "discrete",
    reverse: bool = False,
    keep_first_n: Optional[int] = None,
    keep_last_n: Optional[int] = None,
    keep: Optional[list[bool]] = None,
    repeat: int = 1,
    shuffle: Union[bool, int] = False,
) -> Union["LinearSegmentedColormap", "ListedColormap"]:
    """
    Load a matplotlib colormap from one of the 2500+ available palettes.

    You can find all valid palette names [here](https://python-graph-gallery.com/color-palette-finder/){target="_blank"}

    Args:
        name: Name of the palette
        cmap_type: Type of colormap: 'continuous' or 'discrete'
        reverse: Whether to reverse the order of the colors or not
        keep_first_n: Keep only the first n colors of the palette
        keep: Specify which colors to keep in the palette
        repeat: The number of times the palette must be present in
            the output. Used to access larger palettes that are repeated.
        shuffle: Used to mix the order of colors. If an integer is
            supplied, it will be used as the seed.

    Returns:
        A matplotlib colormap.
    """
    from matplotlib.colors import LinearSegmentedColormap, ListedColormap
    from PIL import ImageColor

    palette: dict = _get_palette(name, reverse, keep_first_n, keep_last_n, keep, repeat)
    hex_list: list = palette["hex_list"]
    source: str = palette["source"]
    kind: str = palette["kind"]

    if shuffle:
        if isinstance(shuffle, int):
            random.seed(shuffle)
        random.shuffle(hex_list)

    if cmap_type == "continuous":
        cmap: LinearSegmentedColormap = LinearSegmentedColormap.from_list(
            name=f"{name}", colors=hex_list
        )
    elif cmap_type == "discrete":
        cmap: ListedColormap = ListedColormap(name=f"{name}", colors=hex_list)
    else:
        raise ValueError("cmap_type argument must be 'continuous' or 'discrete'")

    cmap.source: str = source  # ty: ignore
    cmap.kind: str = kind  # ty: ignore
    cmap.hex: list = hex_list  # ty: ignore
    cmap.colors: list = hex_list  # ty: ignore
    cmap.rgb: list = [ImageColor.getcolor(hex, "RGB") for hex in hex_list]  # ty: ignore
    cmap.yiq: list = [  # ty: ignore
        colorsys.rgb_to_yiq(rgb[0], rgb[1], rgb[2])
        for rgb in cmap.rgb  # ty: ignore
    ]
    cmap.hsv: list = [  # ty: ignore
        colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        for rgb in cmap.rgb  # ty: ignore
    ]

    return cmap
