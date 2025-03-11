{
    'name': 'Custom Accounting',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Invoices, Payments, Follow-ups & Bank synchronization',
    'description': """
        Invoicing Access Rights
        ========================
        It gives the Administrator user access to important invoicing features such as bank recon and payment follow-up.
    """,
    'depends': ['account', 'base',],
    'data': [
        'security/ir.model.access.csv',  # Fichier de sécurité
        'views/account_move_view.xml',  # Vues pour les écritures comptables
        'views/partner_views.xml',       # Vues pour les clients/fournisseurs
        'views/res_partner_views.xml',
        'views/product_views.xml',
        'views/journal_entries_view.xml',
        'views/bill_views.xml',
        'views/refunds_views.xml',
        'views/vendor_payments_views.xml',
        'views/product_vendor_views.xml',
        'views/vendor_views.xml',

        'security/security.xml',

        'views/menu_views.xml'         # Menuitems
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}