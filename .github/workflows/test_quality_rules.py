from src.quality_rules import is_valid_order, normalize_status

def test_order_key_validation():
    assert is_valid_order("o-1", "c-1")
    assert not is_valid_order("", "c-1")
    assert not is_valid_order("o-1", None)

def test_status_normalization():
    assert normalize_status(" Delivered ") == "delivered"
    assert normalize_status(None) is None
