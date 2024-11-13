{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
    'summary': 'A management system for veterinary clinics',
    'author': '<Juan Carlos> none',  
    'license': 'LGPL-3',
    'depends': [
        'base'
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/appointment.xml',
        'views/veterinary_pet.xml',
    ],
    'application': False,
    'installable': True,
}
