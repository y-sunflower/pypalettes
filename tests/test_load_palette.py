from pypalettes import load_palette

def test_load_palette():
    palette = load_palette("Acadia")
    assert isinstance(palette, list)
    assert all(isinstance(color, str) for color in palette)
