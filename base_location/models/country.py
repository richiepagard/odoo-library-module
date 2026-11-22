from odoo import fields, models


class BaseLocationCountry(models.Model):
    """
    Represents to the countries of states.
    """

    _name = "base_location.country"
    _description = "Countries of states"

    name = fields.Char(required=True)
    state_ids = fields.One2many(
        comodel_name="base_location.state",
        inverse_name="country_id",
        string="States"
    )
