{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
  
    'summary': 'Mamanagement system for vererinary clinic',
    'author': '<Alex Casal G>',

    'license': 'LGPL-3',
  
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/veterinary_pet.xml',
        'views/veterinary_appointment.xml',
    ],


    'application': True,
    'installable': True,

}