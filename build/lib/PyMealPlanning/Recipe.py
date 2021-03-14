from typing import Optional, Union

from PyMealPlanning.Ingredient import Ingredient
from PyMealPlanning.Nutrient import NutrientInfo
from PyMealPlanning.UnitMetrics import Serving
from PyMealPlanning.utils import PyLaTeXRecipeUtil

# ================================================================================
# RECIPES
# ================================================================================


# @total_ordering
class Recipe(object):
    def __init__(
        self,
        name: str,
        ingredients: Union[list, Ingredient],
        nutrient_info: NutrientInfo,
        prep_time: Optional[float] = 1,
        prep_time_unit: Optional[str] = "min",
        serving: Union[float, Serving] = 1,
        tag: Union[str, list] = ["Breakfast", "Lunch", "Dinner"],
        score: float = 5,
        instructions: Union[str, list] = "Mix everything and Enjoy!",
        source: Optional[str] = None,
    ) -> None:

        self.name = name
        self.ingredients = (
            ingredients if isinstance(ingredients, list) else [ingredients]
        )
        self.nutrient_info = nutrient_info
        self.serving = serving if isinstance(serving, Serving) else Serving(serving)
        self.tags = tag if isinstance(tag, list) else [tag]
        self.prep_time = prep_time
        self.prep_time_unit = prep_time_unit
        self.instructions = (
            instructions if isinstance(instructions, list) else [instructions]
        )
        self.score = score
        self.source = source

        # methods
        self._sort_ingredients()

    def _sort_ingredients(self) -> None:
        self.ingredients = sorted(self.ingredients, reverse=True)

    def __eq__(self, other) -> bool:
        pass

    def __lt__(self, other) -> bool:
        pass

    def to_latex(self, photo=None, folder=".") -> None:
        wrapper = PyLaTeXRecipeUtil(self, folder)
        wrapper.recipe_to_latex(photo=photo)
