from odoo import api, fields, models


class LibraryCity(models.Model):
    """
    Represents to the cities which are came from a state.
    """

    _name = "library.city"
    _description = "Cities came from states"

    name = fields.Char(required=True)
    state_id = fields.Many2one(
        comodel_name="library.state",
        string="State"
    )
    population = fields.Integer()


    @api.depends("name", "state_id")
    def _compute_display_name(self):
        """
        Customize the display name.
        Showing the name of the city with its state.
        """
        for city in self:
            city.display_name = f"{city.name} ({city.state_id.name})"
