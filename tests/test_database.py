from unittest.mock import patch
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING,INGREDIENT_TYPE_SAUCE


class TestDatabase:
    # Проверяем доступность булок
    def test_database_available_buns(self):
        mock_bun = [Bun("Флюоресцентная булка R2-D3", 988)]
        database = Database()
        with patch.object(database, 'buns', mock_bun):
            result = database.available_buns()
            assert result == mock_bun

    # Проверяем доступность начинок
    def test_database_available_fillings_ingredients(self):
        mock_ingredient = [Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)]
        database = Database()
        with patch.object(database, 'ingredients', mock_ingredient):
            result = database.available_ingredients()
            assert result == mock_ingredient

    # Проверяем доступность соусов
    def test_database_available_sauce_ingredients(self):
        mock_ingredient = [Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15)]
        database = Database()
        with patch.object(database,'ingredients', mock_ingredient):
            result = database.available_ingredients()
            assert result == mock_ingredient