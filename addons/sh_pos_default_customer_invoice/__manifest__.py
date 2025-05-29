# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

{
    "name": "Point Of Sale Default Customer Invoice | POS Default Customer Invoice | Point Of Sale Default Invoice",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Point Of Sale",
    "license": "OPL-1",
    "summary": "Point Of Sale Default Invoices POS Default Invoice on POS Point Of Sale Bydefault Invoice POS Bydefault Invoice POS Invoices POS Default Invoice Globally For All Customer Global Default Invoice Default Client Invoice Odoo",
    "description": """This module activates the invoice button by default in the POS. Here the invoice button is selected so when an order is placed invoice generates automatically. You can generate default invoice for individual customers wise or for all customers based on configuration.""",
    "version": "0.0.1",
    "depends": ["point_of_sale"],
    "application": True,
    "data": [
        'views/res_config_settings.xml',
        'views/res_partner.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'sh_pos_default_customer_invoice/static/src/**/*',
        ],

    },
    "images": ["static/description/background.png", ],
    "auto_install": False,
    "installable": True,
    "price": "25",
    "currency": "EUR"
}
