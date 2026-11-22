from odoo import fields, models


class BaseLocationState(models.Model):
    """
    Represents to the state of cities.
    """

    _name = "base_location.state"
    _description = "States of cities"

    name = fields.Char(required=True)
    country_id = fields.Many2one(
        comodel_name="base_location.country",
        string="Country"
    )
    city_ids = fields.One2many(
        comodel_name="base_location.city",
        inverse_name="state_id",
        string="Cities"
    )
