from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'  # Héritage du modèle existant

    custom_field = fields.Char(string="Champ Personnalisé", help="Ceci est un champ personnalisé pour les écritures comptables.")