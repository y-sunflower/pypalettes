from pypalettes import show_cmap
from matplotlib.figure import Figure


def test_show_cmap():
    fig = show_cmap("Acadia")
    assert isinstance(fig, Figure)
