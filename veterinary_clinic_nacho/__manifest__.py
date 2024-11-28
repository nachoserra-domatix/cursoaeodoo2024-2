{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
    'summary': 'A management system for veterinary clinics',
    'author': '<Nacho Serra>, Domatix',
    'license': 'LGPL-3',
    'depends': [
        'base','sale','hr'
    ],
    'data': [
             'data/veterinary_species_data.xml',   
             'security/res_groups.xml',
             'security/ir.model.access.csv',
             'security/ir_rule.xml',
             'views/veterinary_pet.xml',
             'views/veterinary_appointment.xml',
             'views/veterinary_appointment_line.xml',
             'views/veterinary_species.xml',
             'views/veterinary_surgery.xml',
             'views/veterinary_allergy.xml',
             'views/veterinary_insurance.xml',
             'views/veterinary_adoption.xml',
             'wizard/veterinary_appointment_edit_state.xml',
             'wizard/veterinary_surgery_edit_state.xml',
             'report/veterinary_appointment_report.xml',
             'report/veterinary_appointment_report_simple.xml',
             'report/veterinary_insurance_report.xml',
             'data/ir_cron.xml'
             ],
    'application': False,
    'installable': True,
}