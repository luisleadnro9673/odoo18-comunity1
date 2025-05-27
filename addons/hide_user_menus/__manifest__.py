# -*- coding: utf-8 -*-
{
    'name': 'Hide User Menus (Top Right Corner)',
    'author': 'Odoo Hub',
    'category': 'Tools',
    'summary': 'This module hides the user menu from the top right corner of the Odoo interface, removing options like Documentation, Support, Shortcuts for a cleaner and more focused UI.',
    'description': """
        This module modifies the Odoo user interface by removing or hiding elements in the top right user menu. 
        The menu items that will be hidden include:
        - Documentation
        - Support
        - Shortcuts
        - Onboarding
        - My Odoo.com account
        
        The main goal of this module is to streamline the user interface and make it less cluttered, particularly 
        for users who do not need these features in their daily use.
    """,
    'maintainer': 'Odoo Hub',
    'version': '1.0',
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'hide_user_menus/static/src/js/user_menus.js',
        ],
    },
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
