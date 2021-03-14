import shutil

from pylatex import Command, Document
from pylatex.utils import NoEscape


class PyLaTeXUtil(object):
    def __init(self):
        pass

    def _add_tex_title(self, title: str) -> None:
        title_line = NoEscape("% " + 80 * "=")

        self.doc.append(title_line)
        self.doc.append(NoEscape(f"% {title}"))
        self.doc.append(title_line)

    def _space(self) -> None:
        self.doc.append(NoEscape("\n"))


class PyLaTeXRecipeUtil(PyLaTeXUtil):
    def __init__(self, recipe, folder=".") -> None:
        self.recipe = recipe
        self.doc = Document(
            f"{folder}/tex/{self.recipe._savename}",
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

    def _move_pdf(self) -> None:
        shutil.move(
            f"{self.folder}/tex/{self.recipe._savename}.pdf",
            f"{self.folder}/pdf/{self.recipe._savename}.pdf",
        )

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


class PyLaTeXMealPlanUtil(PyLaTeXUtil):
    def __init__(self, mealplan, folder=".") -> None:
        self.mealplan = mealplan
        self.doc = Document(
            # f"{folder}/{self.mealplan._savename}",
            f"{folder}/tex/{self.mealplan._savename}",
            documentclass=Command("documentclass", "article"),
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

    def _move_pdf(self) -> None:
        shutil.move(
            f"{self.folder}/tex/{self.mealplan._savename}.pdf",
            f"{self.folder}/pdf/{self.mealplan._savename}.pdf",
        )

    def mealplan_to_latex(self) -> None:
        self._space()

        self.doc.preamble.append(Command("usepackage", "mealplan"))
        self._add_tex_title("Data")

        self._space()
        self.doc.append(Command("firstdate", self.mealplan.start_date))
        self.doc.append(Command("lastdate", self.mealplan.end_date))

        self._space()

        self._add_tex_title("Doc")
        self.doc.append(Command("mytitle"))

        self._space()

        for i, d in enumerate(self.mealplan.days):
            self.doc.append(NoEscape(f"%Day {i+1}"))
            self.doc.append(d.latex_command())
            self._space()

        self.doc.generate_pdf(clean_tex=False, clean=True)

        self._move_pdf()
