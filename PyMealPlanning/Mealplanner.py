import calendar
from datetime import date
from typing import Tuple, Union

import pandas as pd
import numpy as np

from PyMealPlanning.Day import Day
from PyMealPlanning.utils import PyLaTeXMealPlanUtil


class GroceryList(object):
    def __init__(self, list,) -> None:
        self._list = list

    # set(cum_list)

    # # Alphabetical order
    # cum_list

    # # Category order
    # newlist = sorted(cum_list, key=lambda x: x.category, reverse=False)
    # t = np.array(newlist)
    # t[[x.category == "Varia" for x in t]]

    def to_txt(self, filename, folder="."):
        longest_article = max([len(x.name) for x in self._list])
        f = open(f"{folder}/{filename}.txt", "w+")

        for article in self._list:
            f.write(f"{article.name.ljust(longest_article + 10)}{article.metric}\n")

        f.close()

    def __repr__(self):
        return self._list.__repr__()


class MealPlanner(object):
    def __init__(self) -> None:
        self.days = None

    def set_dates(self, start: Union[str, date], end: Union[str, date]):
        self._start_date, self.start_date, self.start_day = self._check_date(start)
        self._end_date, self.end_date, self.end_day = self._check_date(end)
        self._all_dates = pd.date_range(self._start_date, self._end_date)
        self.all_dates = [self._check_date(x)[1] for x in self._all_dates]
        self.all_days = [self._check_date(x)[2] for x in self._all_dates]

    def _check_date(self, d) -> Tuple[date, str, str]:
        d = d if isinstance(d, date) else pd.to_datetime(d).date()
        return (d, d.strftime("%d/%m/%Y"), calendar.day_name[d.weekday()])

    def add_days(self, days=Union[Day, list]):
        self.days = [days] if isinstance(days, Day) else days
        self.days = sorted(self.days, reverse=False)
        self.set_dates(start=self.days[0]._date, end=self.days[-1]._date)

    def __repr__(self) -> str:
        if self.days:
            return " \n \n".join(str(x) for x in self.days)

    @property
    def _savename(self):
        return f"Mealplan_{self.start_date.replace('/', '')}_{self.end_date.replace('/', '')}"

    def to_latex_mealplan(self, folder: str = ".") -> None:
        wrapper = PyLaTeXMealPlanUtil(self, folder)

        wrapper.mealplan_to_latex()

    def create_grocery_list(self) -> GroceryList:
        list_of_ingredients = []
        for day in self.days:
            for meal in day.meals:
                list_of_ingredients += meal.ingredients

        list_of_ingredients = [x for x in list_of_ingredients if x is not None]
        list_of_ingredients = sorted(list_of_ingredients)

        # aggregate over ingredients
        cum_list = []
        for x in list_of_ingredients:
            if x not in cum_list:
                temp = [t for t in list_of_ingredients if t == x]
                s = np.array(temp).sum()
                cum_list.append(s)

        self.grocery_list = GroceryList(cum_list)
        return self.grocery_list
