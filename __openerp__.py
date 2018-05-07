# -*- coding: utf-8 -*-
{
    'name': "dietfacts",

    'summary': """
        Dietfacts module""",

    'description': """
        Extra data for products
    """,

    'author': "Mahdy",
    'website': "https://github.com/mfathei",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}