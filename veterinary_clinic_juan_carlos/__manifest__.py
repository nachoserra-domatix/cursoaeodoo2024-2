{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
    'summary': 'A management system for veterinary clinics',
    'author': '<Juan Carlos> none',  
    'license': 'LGPL-3',
    'depends': [
        'base','hr'
    ],
    'data': [
        'data/animalspecies_data.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/veterinary_pet.xml',
        'views/appointment.xml',
        'views/allergy.xml',
        'views/animalspecies.xml',
        'views/insurance.xml',
        'views/surgeries.xml',
    ],
    'application': False,
    'installable': True,
}
