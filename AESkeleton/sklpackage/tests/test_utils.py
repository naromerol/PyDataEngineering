from sklpackage import Utils

def test_version():
    v = Utils(1.0)
    assert v.get_version() == '1.0'