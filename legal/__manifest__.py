# -*- coding: utf-8 -*-
{
    'name': "legal",

    'summary': """
        legal consultation services """,

    'description': """
        consultation services for client 
    """,

    'author': "mahmoud hamouda",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'crm', 'report_xlsx'],
    'images': ["static/images/law.png"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/matters.xml',
        'views/lawers.xml',
        'views/law_attandance.xml',
        'views/law_pyslips.xml',
        'views/partner.xml',
        'views/meetings.xml',
        'views/templates.xml',
        'reports/report.xml',
        'reports/clients_card.xml',
        'wizards/create_client_appointment.xml'
        #'reports/clients_card.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,

}
