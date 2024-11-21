{
    'name': 'Clinica Veterinaria Laura',
    'version': '17.0.1.0.0',
    'description': '',
    'summary': 'A management system for veterinary clinic',
    'author': '<Laura Elorriaga>, Goi',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base','hr'
    ],
    'data':[ 
        'security/res_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'views/veterinary_pet.xml',
        'views/veterinary_species.xml',
        'views/veterinary_appointment_line.xml',
        'views/veterinary_appointment.xml',
        'views/veterinary_surgery.xml',
        'views/veterinary_allergy.xml',
        'views/veterinary_insurance.xml',
        'data/veterinary_species_data.xml',
        'views/veterinary_adoption.xml'
    ],
    'application': False,
    'installable':True,
    'assets': {
        
    }
}