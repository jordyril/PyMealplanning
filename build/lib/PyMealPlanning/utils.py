import shutil

from pylatex import Command, Document
from pylatex.utils import NoEscape


class PyLaTeXRecipeUtil(object):
    def __init__(self, recipe, folder="./") -> None:
        self.recipe = recipe
        self.doc = Document(
            f"{folder}/tex/{self._savename}",
            documentclass=Command(
                "documentclass", arguments="standalone", options="preview"
            ),
            fontenc=None,
            inputenc=None,
            font_size="normalsize",
            lmodern=False,
            textcomp=False,
            microtype=None,
            page_numbers=False,
            indent=None,
            geometry_options=None,
            data=None,
        )
        self.folder = folder

    def _add_tex_title(self, title: str) -> None:
        title_line = NoEscape("% " + 80 * "=")

        self.doc.append(title_line)
        self.doc.append(NoEscape(f"% {title}"))
        self.doc.append(title_line)

    @property
    def _savename(self) -> str:
        return "".join(self.recipe.name.title().split(" "))

    def _space(self) -> None:
        self.doc.append(NoEscape("\n"))

    def _move_pdf(self) -> None:
        # os.remove(f"{self.folder}/")
        shutil.move(
            f"{self.folder}/tex/{self._savename}.pdf",
            f"{self.folder}/pdf/{self._savename}.pdf",
        )

    # def _move_tex(self) -> None:
    #     # os.remove(f"{self.folder}/")
    #     shutil.move(
    #         f"{self.folder}/{self._savename}.tex",
    #         f"{self.folder}/tex/{self._savename}.tex",
    #     )

    def recipe_to_latex(self, photo: str) -> None:
        self._space()

        self.doc.preamble.append(Command("usepackage", "recipe"))
        self._add_tex_title("Data")

        self._space()
        self.doc.append(Command("title", self.recipe.name))
        self.doc.append(Command("serving", self.recipe.serving))

        self._space()

        for var in ["calories", "protein", "fat", "carbs"]:
            self.doc.append(
                Command(var, getattr(self.recipe.nutrient_info, var).metric.quantity)
            )

        self._space()

        if photo:
            self.doc.append(Command("photo", photo))

        self._space()

        for ing in self.recipe.ingredients:
            self.doc.append(
                Command("ingredient", [ing.name, ing.metric.quantity, ing.metric.unit])
            )

        self._space()

        for step in self.recipe.instructions:
            self.doc.append(Command("step", step))

        if self.recipe.source:
            self.doc.append(Command("source", self.recipe.source))

        if self.recipe.score:
            self.doc.append(Command("score", self.recipe.score))

        self._add_tex_title("Doc")
        self.doc.append(Command("createrecipe"))

        self.doc.generate_pdf(clean_tex=False, clean=True)

        self._move_pdf()
