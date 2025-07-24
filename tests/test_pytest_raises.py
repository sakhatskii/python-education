import pytest


class TestPytestRaises:
    """Способы отлавливания ошибок в тестах, чтобы тесты не падали"""
    def test_1(self):
        """Тест с использованием блока try/except"""
        x = 1
        y = 0
        try:
            print(x/y)
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")

    def test_2(self):
        """Тест с использованием pytest.raises"""
        x = 1
        y = 0
        with pytest.raises(ZeroDivisionError):
            print(x/y)
