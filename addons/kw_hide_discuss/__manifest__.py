{
    'name': 'Hide discuss',
    'summary': 'Hide Discuss menu from user not in "Discuss user" group',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Discuss',
    'license': 'LGPL-3',
    'version': '18.0.1.3.1',

    'depends': [
        'mail',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/security.xml',
        'views/menu_view.xml',
    ],
    'demo': [
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',

}
