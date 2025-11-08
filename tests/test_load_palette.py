from pypalettes import load_palette
import pytest


def test_load_palette():
    assert load_palette("Acadia") == [
        "#FED789FF",
        "#023743FF",
        "#72874EFF",
        "#476F84FF",
        "#A4BED5FF",
        "#453947FF",
    ]

    assert load_palette("kadabra") == [
        "#D0B000FF",
        "#F8E828FF",
        "#886000FF",
        "#603000FF",
        "#886010FF",
        "#A88028FF",
        "#F8F8F8FF",
        "#585858FF",
        "#F8F878FF",
        "#D8D8D8FF",
        "#B0B0B0FF",
        "#F04030FF",
        "#F08888FF",
        "#D0B050FF",
    ]


@pytest.mark.parametrize("repeat", [1, 3])
@pytest.mark.parametrize("keep_first_n", [None, 1])
@pytest.mark.parametrize("reverse", [True, False])
@pytest.mark.parametrize("shuffle", [True, 1, False])
def test_load_palette_random(shuffle, repeat, keep_first_n, reverse):
    """Randomly load 30 palettes"""
    n: int = 30
    for _ in range(n):
        palette: list[str] = load_palette(
            shuffle=shuffle,
            repeat=repeat,
            keep_first_n=keep_first_n,
            reverse=reverse,
        )
        assert isinstance(palette, list)
        assert all(isinstance(color, str) for color in palette)
