{
    "name": "account_move_tax",
    'version': '18.0.1.3.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'A2 Systems,ADHOC SA, Moldeo Interactive,Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'summary': '',
    'depends': [
        'uom',
        'l10n_latam_invoice_document',
        'l10n_ar',
        'account'
    ],
    'external_dependencies': {
    },
    'data': [
        'views/move_view.xml',
        'views/tax_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'images': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
