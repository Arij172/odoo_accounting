# models/account_move_line.py
from odoo import models

class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'
    # Aucune modification n'est nécessaire ici si vous ne souhaitez pas ajouter de nouveaux champs ou méthodes
