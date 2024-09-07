from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestIngredient:
    # Получаем цену добавленного ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X',90),
        (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15),
        (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 300),
        (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337),])
    def test_get_price_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    # Получаем название добавленного ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90),
        (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15),
        (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 300),
        (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337),])
    def test_get_name_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    # Получаем тип добавленного ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90),
        (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15),
        (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 300),
        (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337),])
    def test_get_type_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type