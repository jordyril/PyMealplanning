import os


# from typing import Union, Tuple
from MyUtils.dataprocessing import save_to_pickle, open_from_pickle

PATH = r"C:\Users\jordy\OneDrive\Varia\Health\Food\PyMealplanning"
recipe_folder = r"Recipes"

os.chdir(f"{PATH}")

from PyMealPlanning import (
    Ingredient,
    Milk,
    Recipe,
    Day,
    RecipeDictionary,
    MealPlanner,
    Volume,
    Mass,
    NutrientInfo,
)


# ================================================================================
# TESTING RECIPE
# ================================================================================
test = Recipe(
    name="test cereals",
    ingredients=[Milk(Volume(200)), Ingredient("Nesquik cereal", Mass(30, "g"))],
    nutrient_info=NutrientInfo(203, 33, 9, 4),
    score=9,
    source="https://www.google.com/",
)

# test.to_latex(folder=recipe_folder, photo="NesquikCereal")


# ================================================================================
# RECIPE DICTIONARY
# ================================================================================
filename = "Recipe_dictionary"

recipe_dictionary = RecipeDictionary(filename, recipe_folder)


# ================================================================================
# TESTING MEALPLANNER
# ================================================================================

testmeals = ["test cereals", None, "test cereals"]
t = Day(date="15-03-2021", meals=testmeals, recipe_dictionary=recipe_dictionary)
v = Day(date="16-03-2021", meals=testmeals, recipe_dictionary=recipe_dictionary)
print(t.latex_command().dumps())
t < v

test = MealPlanner()
days = []
for i in range(15, 17):
    days.append(
        Day(date=f"{i}-03-2021", meals=testmeals, recipe_dictionary=recipe_dictionary)
    )

test.add_days(days)

test.all_dates
test.to_latex_mealplan(folder="Mealplan")
