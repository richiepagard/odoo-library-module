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

    _name = "library.author"
    _description = "Library Authors"

    fullname = fields.Char(required=True)
    birth_year = fields.Integer()
    is_active = fields.Boolean(default=True)
    book_ids = fields.Many2many(
        "library.book",
        string="books"
    )
    books_count = fields.Integer(compute="_compute_books_count")

    @api.depends("book_ids")
    def _compute_books_count(self):
        """
        Returns the length of books an author has written.
        """
        for author in self:
            author.books_count = len(author.book_ids)

    @api.depends("fullname", "birth_year")
    def _compute_display_name(self):
        """
        Customize the display name.
        If the author's "birth year" does not None,
        displays its fullname and its birth year -> fullname (birth year)
        otherwise, only display the fullname -> fullname
        """
        for author in self:
            if author.birth_year:
                author.display_name = f"{author.fullname} ({author.birth_year})"
            else:
                author.display_name = author.fullname
