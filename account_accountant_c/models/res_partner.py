from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    payment_ids = fields.One2many("account.payment", "partner_id", string="Payments")
