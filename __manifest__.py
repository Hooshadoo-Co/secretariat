{
    'name': 'Secretariat',
    'version': '1.0',
    'summary': 'Document/Letter Management System',
    'sequence': 10,
    'description': 'Manage documents and letters effectively within Odoo',
    'category': 'Tools',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'hr'],
    'data': [
        'views/secretariat_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/icon.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
