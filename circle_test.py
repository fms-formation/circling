import circle
from circle import perimeter

def test_should_return_perimeter():
    expected_value = 12.256
    assert expected_value == perimeter(2)


def test_should_return_perimeter_with_mock(mocker):
    mocker.patch.object(circle,'PI',3.14)
    expected_value: float = 12.26
    assert perimeter(2) == expected_value