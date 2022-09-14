import pytest
from main import get_routes

def test_get_distance():
    assert get_routes("CDC") == 16
    assert get_routes("CEBC") == 9
    assert get_routes("CEBCDC") == 25
    assert get_routes("CDCEBC") == 25
    assert get_routes("CDEBC") == 21
    assert get_routes("CEBCEBC") == 18
    assert get_routes("CEBCEBCEBC") == 27
    assert get_routes("AED") == "NO SUCH ROUTE"
