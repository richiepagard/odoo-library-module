from odoo import api, fields, models


class LibraryAuthor(models.Model):
    """
    Represnts to the books' authors. Mange authors information such as the length
    of books written and personal stuff like birth year.

    Attributes:
        fullname (str): The fullname or nickname of an author.
        birth_year (int): The year author born.
        is_active (bool): Is the author alive or writing actively.
        books_ids (int): Reverse relation for books.
        books_count (int): The total length of book the author has written.
    """

    _name = "author"
    _description = "Library Authors"

    fullname = fields.Char(required=True)
    birth_year = fields.Integer()
    is_active = fields.Boolean(default=True)
    book_ids = fields.Many2many(
        "library.book",
        string="books"
    )
    books_count = fields.Integer(compute="_compute_books_count")

    @api.depends("books_count")
    def _compute_books_count(self):
        """
        Returns the length of books an author has written.
        """
        for book in self:
            book.books_count = len(books_ids)
