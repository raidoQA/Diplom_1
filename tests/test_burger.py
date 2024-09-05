from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING



class TestBurger:
    # Добавляем один ингредиент
    def test_add_ingredient_burger(self):
        burger = Burger()
        ingredients = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        burger.add_ingredient(ingredients)
        assert len(burger.ingredients) == 1

    # Удаляем ингредиент
    def test_remove_ingredient_in_burger(self):
        burger = Burger()
        ingredients = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Перемещаем слоя ингредиента
    def test_move_ingredient_in_burger(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, 'Филе Люминесцентного тетраодонтимформа', 988)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2

    # Получаем цену
    def test_get_price_burger(self):
        burger = Burger()
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        burger.set_buns(bun)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, 'Филе Люминесцентного тетраодонтимформа', 988)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 300)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 3264

    # Получаем рецепт бургера
    def test_get_receipt_burger(self):
        burger = Burger()
        bun = Bun('Краторная булка N-200i', 1255)
        burger.set_buns(bun)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, 'Филе Люминесцентного тетраодонтимформа', 988)
        ingredient_sause = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sause)
        expected_receipt = ('(==== Краторная булка N-200i ====)\n'
                            '= filling Филе Люминесцентного тетраодонтимформа =\n'
                            '= sauce Соус традиционный галактический =\n'
                            '(==== Краторная булка N-200i ====)\n'
                            '\n'
                            'Price: 3513')
        assert burger.get_receipt() == expected_receipt