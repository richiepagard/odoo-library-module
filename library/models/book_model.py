from odoo import api, fields, models


class LibraryBook(models.Model):
    """
    Represents to the books of the library.

    Attributes:
        title (str): The book's title. Shouldn't be unique.
        author (int): The authors of the book.
        isbn (str): Numeric commercial book identifier that is intended to be unique.
        publish_year (int): The year this book published.
        age (int): Not stored, only shows the age of the book by computing base on publish year.
        pages (int): The pages that book included.
        state (str): Current state of the book, is the book available or not.
        is_active (int): The activation status of the book.
        description (str): Book's description for more information.
    """

    _name = "book"
    _description = "Librarary Books"

    title = fields.Char(required=True)
    author = fields.Many2many(
        "library.author",
        string="authors"
    )
    isbn = fields.Char(string="ISBN")
    publish_year = fields.Integer(string="Yearh Published")
    age = fields.Integer(
        compute="_compute_age",
        stirng="Book's age base on its published year"
    )
    pages = fields.Integer()
    state = fields.Selection(
        [ ("available", "Available"), ("lost", "Lost") ],
        default="available"
    )
    is_active = feilds.Boolean(default=True)
    description = fields.Text()

    @api.depends("age")
    def _compute_age(self):
        """
        Calculate the age of the book according to its published year.
        """
        current_year = fields.Date.today().year

        for book in self:
            book.age = current_year - book.year if book.year else 0

    @api.constrains("year")
    def _check_year(self):
        """
        Check whether the published year of the book is correct.
        If the published year is bigger than the current date year,
        the validation error raised.
        """
        current_year = fields.Date.today().year

        for book in self:
            if book.year > current_year:
                raise ValidationError("The publication year cannot be in the future!")
