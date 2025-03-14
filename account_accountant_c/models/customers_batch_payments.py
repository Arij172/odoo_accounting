from odoo import models, fields

class AccountingBatchPayment(models.Model):
    _name = 'accounting.batch.payment'
    _description = 'Accounting Batch Payment'

    name = fields.Char(string="Reference", required=True, copy=False, default="New")
    bank_id = fields.Many2one('res.bank', string="Bank")
    date = fields.Date(string="Date", default=fields.Date.context_today)
    amount = fields.Float(string="Amount")
    activities = fields.Text(string="Activities")
    batch_type = fields.Selection([
        ('inbound', 'Inbound'),
        ('outbound','Outbound')
    ], string="Batch Type", default='inbound')
    state = fields.Selection([
        ('new', 'New'),
        ('sent', 'Sent'),
        ('reconciled', 'Reconciled')
    ], string="State", default='new')
    payment_method_id = fields.Many2one('account.payment.method', string ="Payment Method")
