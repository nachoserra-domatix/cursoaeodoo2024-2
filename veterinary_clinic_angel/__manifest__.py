{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
    'summary': 'A management system for veterinary clinics',
    'author': '<Ángel Larralde>, Zzircon',
    'license': 'LGPL-3',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/veterinary_pet.xml',
        'views/veterinary_appointment.xml',
    ],
    'application': False,
    'installable': True,
}