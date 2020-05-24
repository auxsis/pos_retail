# -*- coding: utf-8 -*-
{
    'name': 'Concession Product',
    'version': '1.0.0',
    'author': 'Mattobell Nigeria Limited',
    'summary': 'Concession Product',
    'license': 'AGPL-3',
    'description': """
    Management of Sales
    """,

    'data': [
        'views/concession_product_menu.xml',
        'views/product_view.xml',
        # 'views/res_company_view.xml',
        'views/account_invoice_view.xml',
        'views/return_product_view.xml',


    ],
    'version': '0.0.1',
    'category': 'Human Resources',
    'website': 'https://www.mattobell.com',
    'depends': ['base', 'sale', 'purchase', 'sale_management', 'account', 'point_of_sale'],
    'application': True,
    'auto_install': False,
}
