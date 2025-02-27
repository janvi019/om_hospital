{	
	'name':'Hospital Management ',
	'letest version': '17.1.0',
	'category': 'Hospital',
	'auther': 'Odoo Mate',
	'summary': 'Hospital management system',
	'description': 'Hospital management system',
	'depends': ['mail','product'],
	'data': [
		'security/ir.model.access.csv',
		'views/menu.xml',
		'views/patient_view.xml',
		'views/female_patient_view.xml',
		'views/appointment_view.xml'
	],
	'demo': [],
	'application': True,
	'auto_install': False,
	'License': 'LGPL-3',
}