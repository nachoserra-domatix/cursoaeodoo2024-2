{
    'name': 'Veterinary Clinic',
    'version': '17.0.1.0.0',
    'summary': ' A management system for veterinary clinics',
    'author': '<Borja Gimeno> Som Connexió SCCL',
    'license': 'LGPL-3',
    'depends': [
        'base', 'sale', 'hr'
    ],
    "data": [
                "security/res_groups.xml",
                "security/ir_rule.xml",
                "security/ir.model.access.csv",
                "views/veterinary_menu.xml",
                "views/veterinary_species.xml",
                "views/veterinary_pet.xml",
                "views/veterinary_appointment.xml",
                "views/veterinary_allergy.xml",
                "views/veterinary_insurance.xml",
                "views/veterinary_surgery.xml",
                "views/veterinary_appointment_line.xml",
                "views/veterinary_pet_adoption.xml",
                "data/veterinary_species_data.xml",
                "data/ir_cron.xml",
             ],
    'application': False,
    'installable': True,
}