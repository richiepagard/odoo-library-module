from odoo import feilds, models


class LibraryCountry(models.Model):
    """
    Represents to the countries of states.
    """

    _name = "library.country"
    _description = "Countries of states"

    name = fields.Char(required=True)
    state_ids = fields.One2Many(
        comodel="library.state",
        inverse_name="country_id",
        string="States"
    )
