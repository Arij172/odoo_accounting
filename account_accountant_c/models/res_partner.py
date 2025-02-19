from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    payment_ids = fields.One2many("account.payment", "partner_id", string="Payments")
    credit_note_ids = fields.One2many('account.move', 'partner_id', domain=[('move_type', '=', 'out_refund')],
                                      string="Credit Notes")