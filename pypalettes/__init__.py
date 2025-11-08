from .load_cmap import load_cmap
from .load_palette import load_palette
from .create_cmap import create_cmap
from .show_cmap import show_cmap
from .deprecated import get_source, get_hex, get_rgb, get_kind, add_cmap

from typing import Literal

__version__: Literal["0.1.6"] = "0.1.6"
__all__: list[str] = [
    "load_cmap",
    "load_palette",
    "add_cmap",
    "create_cmap",
    "show_cmap",
    "get_source",
    "get_hex",
    "get_rgb",
    "get_kind",
]
