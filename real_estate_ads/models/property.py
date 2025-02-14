from odoo import fields, models

class Property(models.Model):
    _name="estate.property"
    _description="real estate property"

    name=fields.Char(string="Name")
    description =fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability=fields.Date(string="Available From")
    expected_price=fields.Float(string="Expected Price")
    best_offer=fields.Float(string="Best Offer")
    selling_price=fields.Float(string="Selling price")
    bedrooms=fields.Integer(string="Bedrooms")
    living_area=fields.Integer(string="Living Area (sqn)")
    facades=fields.Integer(string="Facades (sqn)")
    garage =fields.Boolean(string="Garage", default=False)
    garden=fields.Boolean(string="Garden", default=False)
    garden_area=fields.Integer(string="Garden Area")
    garden_orientation=fields.Selection([('north','North'),('south','South'),('east','East'),('west','west')],string="Garden Orientation",default="north")

    """id,create_date,create_uid,write_date,write_uid"""