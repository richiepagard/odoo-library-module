from odoo import fields, models


class LibraryState(models.Model):
    """
    Represents to the state of cities.
    """

    _name = "library.state"
    _description = "States of cities"

    name = fields.Char(required=True)
    country_id = fields.Many2one(
        comodel="library.country",
        string="Country"
    )
    city_ids = fields.One2many(
        comodel_name="library.city",
        inverse_name="state_id",
        string="Cities"
    )
