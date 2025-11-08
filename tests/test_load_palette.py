from pypalettes import load_palette


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


def test_load_palette_random():
    """Randomly load 30 palettes"""
    n: int = 30
    for _ in range(n):
        palette: list[str] = load_palette()
        assert isinstance(palette, list)
        assert all(isinstance(color, str) for color in palette)
