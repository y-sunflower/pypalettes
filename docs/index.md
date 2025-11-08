<br><br>

<div class="hero">
<div align="center">
  <h1 class="pypalettes">pypalettes</h1>
</div>

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/pypalettes/image.png?raw=true" alt="pypalettes logo" align="right" width="120px"/>

A <i>dependency-free</i> large (<b>+2500</b>) collection of <u>colormaps</u> and <u>palettes</u> for Python.

<br><br>

<img src="https://static.pepy.tech/badge/pypalettes" alt="total number of downloads of pypalettes"/>

</div>

## Get started

`pypalettes` primarly offers 2 functions:

- `load_palette("palette_name")`: loads a list of colors (dependency-free)
- `load_cmap("palette_name")`: loads a colormap object (for matplotlib/seaborn/etc)

=== "Continuous colormap"

    ```py hl_lines="6"
    # mkdocs: render
    import matplotlib.pyplot as plt
    import numpy as np
    from pypalettes import load_cmap

    cmap = load_cmap("Sunset2", cmap_type="continuous")

    data = np.random.randn(20, 20)

    plt.imshow(data, cmap=cmap)
    plt.colorbar()
    ```

=== "Categorical palette"

    ```py hl_lines="6"
    # mkdocs: render
    import matplotlib.pyplot as plt
    import seaborn as sns
    from pypalettes import load_palette

    palette = load_palette("Fun")

    df = sns.load_dataset("penguins")

    g = sns.lmplot(
        data=df,
        x="bill_length_mm",
        y="bill_depth_mm",
        hue="species",
        palette=palette,
    )
    ```

=== "Your own colormap"

    ```py hl_lines="6 7 8 9"
    # mkdocs: render
    import matplotlib.pyplot as plt
    from pypalettes import create_cmap
    import numpy as np

    cmap = create_cmap(
        colors=["#D57A6DFF", "#E8B762FF", "#9CCDDFFF", "#525052FF"],
        cmap_type="continuous",
    )

    x = np.linspace(0, 20, 1000)
    y = np.sin(x)

    plt.scatter(x, y, c=y, cmap=cmap)
    plt.colorbar()
    ```

- [**See all palettes**](https://python-graph-gallery.com/color-palette-finder/){target="\_blank"}
- [**More examples**](./examples.md)

## Installation

=== "pip"

    ```bash
    pip install pypalettes
    ```

=== "conda"

    ```bash
    conda install conda-forge::pypalettes
    ```

## Acknowledgements

`PyPalettes` is **highly** inspired (and relies on for the first one)
from

- the R package [paletteer](https://github.com/EmilHvitfeldt/paletteer)
- the python library [palettable](https://github.com/jiffyclub/palettable)

A big thanks to [Yan Holtz](https://www.yan-holtz.com/) for creating the Color Palette Finder, a [web app for browsing palettes](https://python-graph-gallery.com/color-palette-finder/)

<br><br>
