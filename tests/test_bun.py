import pytest
from praktikum.bun import Bun


class TestBun:
    # Получаем названия булки
    @pytest.mark.parametrize("name, price", [('Флюоресцентная булка R2-D3', 988), ('Краторная булка N-200i', 1255)])
    def test_get_name_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Получаем цену булки
    @pytest.mark.parametrize("name, price", [('Флюоресцентная булка R2-D3', 988), ('Краторная булка N-200i', 1255)])
    def test_get_price_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price