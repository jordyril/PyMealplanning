import os
from datetime import date
from typing import Union

from MyUtils.dataprocessing import open_from_pickle, save_to_pickle

from PyMealPlanning.Recipe import Recipe


class RecipeDictionary(object):
    def __init__(self, filename: str, folder: str = ".") -> None:
        self.filename = filename
        self.folder = folder

        self._load_existing()

    def _load_existing(self) -> None:
        if not os.path.exists(f"{self.folder}/{self.filename}.pickle"):
            self.recipe_dic = {}
            save_to_pickle(self.filename, self.recipe_dic, folder=self.folder)
        else:
            self.recipe_dic = open_from_pickle(self.filename, folder=self.folder)
            save_to_pickle(
                f"{self.filename}_backup{date.today().strftime('%d%m%Y')}",
                self.recipe_dic,
                folder=f"{self.folder}/backups",
            )

    def _save_dic(self) -> None:
        save_to_pickle(self.filename, self.recipe_dic, folder=self.folder)

    def add_recipe(self, recipe) -> None:
        self._check_dic_key(recipe.name)

        self.recipe_dic[recipe.name] = recipe

        self._save_dic()

    def delete_recipe(self, recipe: Union[str, Recipe]):
        key = recipe.name if isinstance(recipe, Recipe) else recipe
        self.recipe_dic.pop(key, None)
        self._save_dic()

    def _check_dic_key(self, key) -> None:
        if key in self.recipe_dic:
            raise KeyError("Recipe (with same name) already exists in dictionary")

    def __repr__(self) -> str:
        return "\n".join(list(self.recipe_dic.keys()))
