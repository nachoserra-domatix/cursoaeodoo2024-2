{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
    'summary': 'A management system for veterinary clinics',
    'author': '<Nacho Serra>, Domatix',
    'license': 'LGPL-3',
    'depends': [
        'base','sale'
    ],
    'data': ['security/res_groups.xml',
             'security/ir.model.access.csv',
             'security/ir_rule.xml',
             'views/veterinary_pet.xml',
             'views/veterinary_appointment.xml',],
    'application': False,
    'installable': True,
}