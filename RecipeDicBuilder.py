import os
from PyMealPlanning.RecipeDictionary import RecipeDictionary
from PyMealPlanning.Recipe import Recipe
from PyMealPlanning.Ingredient import Ingredient, Milk
from PyMealPlanning.Nutrient import NutrientInfo, Calories, Carbs, Fat, Proteins
from PyMealPlanning.UnitMetrics import Mass, Serving

PATH = r"C:\Users\jordy\OneDrive\Varia\Health\Food\PyMealplanning"
recipe_folder = r"Recipes"

os.chdir(f"{PATH}")

# ================================================================================
# LOAD/CREATE LIBRARY
# ================================================================================
recipe_dictionary = RecipeDictionary(filename="RecipeDictionary", folder=recipe_folder)

# ================================================================================
# ADD RECIPES
# ================================================================================
# -------
# RECIPE
# -------
recipe = Recipe(
    name="Nesquik cereals",
    ingredients=[Ingredient("Nesquik cereals", Mass(30)), Milk(150)],
    nutrient_info=NutrientInfo(calories=180, fat=3, carbs=30, protein=7),
    tag=["Quick", "Lunch", "Breakfast", "NoCooking"],
    score=7,
)

recipe.to_latex(folder=recipe_folder, photo=True)

recipe_dictionary.add_recipe(recipe)
# ================================================================================
# ADDED RECIPES
# ================================================================================
# # -------
# # RECIPE
# # -------
# recipe = Recipe(
#     name="Taboule couscous salat Alnatura",
#     ingredients=Ingredient("Alnatura taboule couscous-salat", Mass(100)),
#     nutrient_info=NutrientInfo(calories=115, fat=0.7, carbs=21, protein=4.3),
#     tag=["Quick", "Lunch", "Dinner", "NoCooking"],
#     score=7.5,
#     instructions="Package instructions",
# )

# recipe.to_latex(folder=recipe_folder, photo=True)

# recipe_dictionary.add_recipe(recipe)

# # -------
# # RECIPE
# # -------
# recipe = Recipe(
#     name="Nesquik cereals",
#     ingredients=[Ingredient("Nesquik cereals", Mass(30)), Milk(150)],
#     nutrient_info=NutrientInfo(calories=180, fat=3, carbs=30, protein=7),
#     tag=["Quick", "Lunch", "Breakfast", "NoCooking"],
#     score=7,
# )

# recipe.to_latex(folder=recipe_folder, photo=True)

# recipe_dictionary.add_recipe(recipe)
