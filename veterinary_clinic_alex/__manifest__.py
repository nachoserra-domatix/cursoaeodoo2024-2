{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
  
    'summary': 'Mamanagement system for veterinary clinic',
    'author': '<Alex Casal G>',

    'license': 'LGPL-3',
  
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        'data/ir_cron.xml',
        'data/ir_sequence.xml',
        'data/veterinary_species_data.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/veterinary_pet.xml',
        'views/veterinary_appointment.xml',
        'views/veterinary_appointment_line.xml',
        'views/veterinary_surgery.xml',
        'views/veterinary_veterinarian.xml',
        'views/veterinary_allergy.xml',
        'views/veterinary_insurance.xml',
        'wizard/veterinary_appointment_edit_state.xml',
        'wizard/veterinary_surgery_edit_state.xml',
        'wizard/veterinary_appointment_create.xml',
        'report/veterinary_appointment_report.xml',
        'report/veterinary_appointment_report_simple.xml',
        'report/veterinary_insurance_report.xml',
        'report/veterinary_surgery_report.xml',
        'views/veterinary_adoption.xml',
        
    ],


    'application': True,
    'installable': True,

}