import os


# from typing import Union, Tuple
from MyUtils.dataprocessing import save_to_pickle, open_from_pickle

PATH = r"C:\Users\jordy\OneDrive\Varia\Health\Food\PyMealplanning"

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

# test.to_latex(folder='Recipes', photo="NesquikCereal")

# ================================================================================
# RECIPE DICTIONARY
# ================================================================================
filename = "Recipe_dictionary"

recipe_dictionary = RecipeDictionary(filename, "Recipes")


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


l = test.create_grocery_list()

l.to_txt(test._savename.replace("Mealplan", "GroceryList"), "Mealplan")
# # test.all_dates
# # test.to_latex_mealplan(folder="Mealplan")
# import numpy as np

# list_of_ingredients = []
# for day in test.days:
#     for meal in day.meals:
#         list_of_ingredients += meal.ingredients

# list_of_ingredients = [x for x in list_of_ingredients if x is not None]
# list_of_ingredients = sorted(list_of_ingredients)

# cum_list = []

# for x in list_of_ingredients:
#     if x not in cum_list:
#         temp = [t for t in list_of_ingredients if t == x]
#         s = np.array(temp).sum()
#         cum_list.append(s)

# cum_list


# set(cum_list)

# # Alphabetical order
# cum_list

# # Category order
# newlist = sorted(cum_list, key=lambda x: x.category, reverse=False)
# t = np.array(newlist)
# t[[x.category == "Varia" for x in t]]

