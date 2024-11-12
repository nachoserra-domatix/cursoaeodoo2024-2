{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
  
    'summary': 'Mamanagement system for veterinary clinic',
    'author': '<Alex Casal G>',

    'license': 'LGPL-3',
  
    'depends': [
        'base'
    ],
    'data': [
       
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/veterinary_pet.xml',
        'views/veterinary_appointment.xml',
        
    ],


    'application': True,
    'installable': True,

}