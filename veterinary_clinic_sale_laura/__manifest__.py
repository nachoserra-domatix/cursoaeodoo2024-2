{
    'name': 'Clinica Veterinary Clinic Sale',
    'version': '17.0.2.1.0',
    'description': '',
    'summary': 'Allows to create order from appointments',
    'author': '<Laura Elorriaga>, Goi',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'veterinary_clinic_laura','sale'
    ],
    'data':[ 'views/veterinary_appointment.xml',
            'views/sale_order.xml',
            'views/product_template.xml',
            'views/veterinary_insurance.xml',
    ],
    'application': False,
    'installable':True,
    'assets': {
        
    }
}