from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'  # Héritage du modèle existant
    _inherit='account.payment'
    custom_field = fields.Char(string="    ",readonly=True,invisible=True)

    partner_id = fields.Many2one('res.partner', string='Customer', ondelete='cascade', index=True, store=True)

    # Filtrer uniquement les notes de crédit et les factures clients
    def _get_credit_notes(self):
        return self.search([('move_type', 'in', ['out_invoice', 'out_refund'])])

    # Lier la note de crédit aux partenaires clients
    def get_credit_notes_by_partner(self):
        return self.search([('move_type', '=', 'out_refund')])  # Note de crédit (out_refund)
