import pytest

from python_education.decorator_and_closure.decorator_with_save_signature import add


class TestfunctionAdd:
    @pytest.mark.parametrize("x, y, result", [(3, 2, 5), (6, 4, 10)])
    def test_add_1(self, x, y, result):
        assert add(x, y) == result
