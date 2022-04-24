import pytest
from ParentChildSingleFile import Child


@pytest.mark.skip
def test_assert():
    assert 1 == 1


def test_Child():
    testObject = Child(message="test message")
    assert testObject.message == "test message"
