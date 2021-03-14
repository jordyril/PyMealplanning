from PyMealPlanning.RecipeDictionary import RecipeDictionary
import calendar
from datetime import date
from functools import total_ordering
from typing import Union

import pandas as pd
from pylatex import Command

from PyMealPlanning.Recipe import EmptyMeal, Recipe


@total_ordering
class Day(object):
    def __init__(
        self,
        date: Union[str, date],
        recipe_dictionary: Union[RecipeDictionary, tuple],
        breakfast: Union[Recipe, str] = None,
        lunch: Union[Recipe, str] = None,
        dinner: Union[Recipe, str] = None,
        meals: list = None,
    ) -> None:
        # self._check_global_recipe_dic()
        self.recipe_dictionary = (
            recipe_dictionary
            if isinstance(recipe_dictionary, RecipeDictionary)
            else RecipeDictionary(recipe_dictionary[0], recipe_dictionary[1])
        )
        self._check_date(date)
        self.meal_names = ["Breakfast", "Lunch", "Dinner"]

        self.meals = meals if meals else [breakfast, lunch, dinner]

        self._check_meals()

    # def _check_global_recipe_dic(self) -> None:

    # if "recipe_dictionary" not in globals():
    #     raise ValueError("There is no global recipe dictionary defined")
    # global recipe_dictionary

    def _check_meals(self) -> None:
        assert (
            len(self.meals) == 3
        ), "Amount of meals given does not equal 3, so cannot make out which meal is skipped"
        meals = []
        for i, m in enumerate(self.meals):
            if m:
                m = m if isinstance(m, Recipe) else self.recipe_dictionary.recipe_dic[m]
                meals.append(m)
            else:
                meals.append(EmptyMeal())

        self.meals = meals
        assert len(self.meals) == len(self.meal_names)

    def __repr__(self) -> str:
        meals = " \n".join(
            [
                f"{self.meal_names[i]}: {self.meals[i].name}"
                for i, _ in enumerate(self.meals)
            ]
        )

        return f"{self.name} ({self.date}): \n{meals}"

    def _check_date(self, d) -> None:
        self._date = d if isinstance(d, date) else pd.to_datetime(d).date()
        self.date = self._date.strftime("%d/%m")
        self.name = calendar.day_name[self._date.weekday()]

    def _create_links_to_pdfs(self) -> None:
        links = []
        for m in self.meals:
            links.append(f"../../Recipes/pdf/{m._savename}.pdf")

        self._links = links

    def latex_command(self) -> Command:
        self._create_links_to_pdfs()
        arguments = [f"{self.name} ({self.date})"]
        arguments += [
            Command("textattachfile", arguments=[self._links[i], self.meals[i].name])
            if not isinstance(self.meals[i], EmptyMeal)
            else ""
            for i, _ in enumerate(self.meals)
        ]
        return Command("myday", arguments=arguments)

    def __eq__(self, other):
        return self._date == other._date

    def __le__(self, other):
        return self._date <= other._date

    def __lt__(self, other):
        return self._date < other._date
