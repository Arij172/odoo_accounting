from odoo import fields, models

class PropertyOffer(models.Model):

    _name = 'estate.property.offer'
    _description = "Real Estate Property offers"

    price=fields.Float(string="Price")
    status=fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string="Garden Orientation",
        default="north")