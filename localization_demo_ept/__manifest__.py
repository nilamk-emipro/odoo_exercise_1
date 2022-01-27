# -*- coding: utf-8 -*-
{
    'name': 'country demo',
    'version': '1.1',
    'category': 'Utility',
    'author': 'Emipro Technologies Pvt. Ltd.',
    'description': """
    the module is for exercise 1
    """,
    'depends': ['sales_team'],
    'data': ['views/country.xml', 'security/ir.model.access.csv','views/state.xml','views/city.xml'],
    'demo': ['data/demodata_country.xml','data/demodata_state.xml','data/demodata_city.xml'],
    'installable': True,
    'auto_install': False,
}
