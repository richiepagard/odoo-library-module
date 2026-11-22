from odoo import fields, models


class BaseLocationCountry(models.Model):
    _inherit = "base_location.country"

    author_ids = fields.One2many(
        comodel_name="library.author",
        inverse_name="country_id",
        string="Authors"
    )


class BaseLocationState(models.Model):
    _inherit = "base_location.state"

    author_ids = fields.One2many(
        comodel_name="library.author",
        inverse_name="state_id",
        string="Authors"
    )


class BaseLocationCity(models.Model):
    _inherit = "base_location.city"

    author_ids = fields.One2many(
        comodel_name="library.author",
        inverse_name="city_id",
        string="Authors"
    )
