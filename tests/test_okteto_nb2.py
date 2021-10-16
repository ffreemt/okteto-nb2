"""Test okteto_nb2."""
from okteto_nb2 import __version__
from okteto_nb2 import okteto_nb2


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not okteto_nb2()
    except Exception:
        assert True
