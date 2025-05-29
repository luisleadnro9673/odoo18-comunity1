# -*- coding: utf-8 -*-
{
    'name': "Change POS logo as Company logo",
    'summary': "This Odoo POS customization module enhances your point of sale interface by aligning it with your brand identity. It replaces the default Odoo POS logo with your company logo from Company Settings, updates the dynamic “Odoo POS” title to a static “POS” label, and removes the “Powered by Odoo” message from printed receipts — delivering a clean, branded, and professional POS experience.",
    'description': """How to remove Point of Sale title, logo, and 'Powered by Odoo' from the receipt and POS interface in Odoo? change odoo pos logo, 
     set pos logo as company logo, change pos logo as company logo
     change pos logo as company logo odoo png set pos logo as company logo odoo png
     odoo change pos logo, odoo change logo, odoo change logo pos,
     change odoo pos title nine,
    change odoo pos title ix,
    change odoo pos title company
    change odoo pos title companies,
    Remove powered by odoo from odoo pos receipt,
    How do I get rid of powered by Odoo pos receipt?,
    Remove powered by odoo from odoo pos receipt online
    Looking to customize Odoo POS and remove default branding?
     Replace Odoo POS Logo with Company Logo,
     Change POS Title from "Odoo POS" to "POS",
     Remove "Powered by Odoo" from POS Receipts,
     remove Odoo logo from POS,
     Odoo POS logo replace,
     customize Odoo POS receipt,
    Odoo POS Customization – Replace Logo, Change Title, Remove "Powered by Odoo
    """,
    'author': "A Cloud ERP",
    'website': "https://www.aclouderp.com",
    'category': 'Point Of Sale',
    'version': '18.0.0.1',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'depends': ['point_of_sale'],
    'price': 8.00,
    'currency': 'EUR',
    'live_test_url': 'https://www.youtube.com/watch?v=8jKQK3mYzHI',
    "images": ["static/description/banner.gif"],
    'data': [
        'views/point_of_sale.xml',
    ],
    'assets': {
        "point_of_sale.assets_prod": [
            "pos_logo_as_company_logo/static/src/xml/point_of_sale_navbar.xml",
            "pos_logo_as_company_logo/static/src/xml/order_receipt.xml",
        ],
    },
}
