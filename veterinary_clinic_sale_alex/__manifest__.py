{
    'name': 'Veterinary Clinic Sale',
    'version': '17.0.1.0.0',  
    'summary': 'Allows create orders from appointments',
    'author': '<Alex Casal G>',
    'license': 'LGPL-3',  
    'depends': [
        'veterinary_clinic_alex',
        'sale'
    ],    
    'data': [
        'views/veterinary_appointment.xml',
        'views/sale_order.xml',
    ],


    'application': True,
    'installable': True,

}