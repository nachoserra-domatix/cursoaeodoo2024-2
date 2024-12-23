{
    'name': 'Veterinary Clinic Sale',
    'version': '17.0.1.0.0',
    'summary': 'Allows to create orders from appointments',
    'author': '<Nacho Serra>, Domatix',
    'license': 'LGPL-3',
    'depends': [
        'veterinary_clinic_nacho','sale',
    ],
    'data': [
             'views/veterinary_appointment.xml',
             'views/product_template.xml',
             'views/sale_order.xml'
             ],
    'application': False,
    'installable': True,
}