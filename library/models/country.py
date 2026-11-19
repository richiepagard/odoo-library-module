from odoo import fields, models


class LibraryCountry(models.Model):
    """
    Represents to the countries of states.
    """

    _name = "library.country"
    _description = "Countries of states"

    name = fields.Char(required=True)
    state_ids = fields.One2many(
        comodel_name="library.state",
        inverse_name="country_id",
        string="States"
    )
    author_ids = fields.One2many(
        comodel_name="library.author",
        inverse_name="country_id",
        string="Authors"
    )
