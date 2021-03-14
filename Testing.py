import os

PATH = r"C:\Users\jordy\OneDrive\Varia\Health\Food\PyMealplanning"
recipe_folder = r"Recipes"

os.chdir(f"{PATH}")

from PyMealPlanning import Recipe, Ingredient

from PyMealPlanning import Mass, Milk
from PyMealPlanning.Nutrient import NutrientInfo

# ================================================================================
# TESTING CLASSES
# ================================================================================
test = Recipe(
    name="test cereals",
    ingredients=[Milk(200), Ingredient("Nesquik cereal", Mass(30, "g"))],
    nutrient_info=NutrientInfo(203, 33, 9, 4),
)

test.to_latex(folder=recipe_folder, photo="NesquikCereal")
