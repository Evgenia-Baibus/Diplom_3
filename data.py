class Ingredient:
    def __init__(self, name, ingredient_id):
        self.name = name
        self.ingredient_id = ingredient_id

class IngredientData:
    ingredient_id = '61c0c5a71d1f82001bdaaa6d'

    bun_name = 'Флюоресцентная булка R2-D3'
    bun_id = '61c0c5a71d1f82001bdaaa6d'

    sauce_name = 'Соус Spicy-X'
    sauce_id = '61c0c5a71d1f82001bdaaa72'

    filling_name = 'Мясо бессмертных моллюсков Protostomia'
    filling_id = '61c0c5a71d1f82001bdaaa6f'

    bun = Ingredient('Флюоресцентная булка R2-D3', 'c0c5a71d1f82001bdaaa6d')
    sauce = Ingredient('Соус Spicy-X', '61c0c5a71d1f82001bdaaa72')
    filling = Ingredient('Мясо бессмертных моллюсков Protostomia', '61c0c5a71d1f82001bdaaa6f')


