from rse_lecture.logic import convert_to_meters

def test_conversion():
    assert convert_to_meters(1, "km") == 1000