{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
    'description': 'A management system for a veterinary clinic',
    'summary': '',
    'author': '<Aleix Leon>, PlanetaTIC',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/veterinary_appointment.xml',
        'views/veterinary_pet.xml',
        'views/veterinary_menus.xml'
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
}
