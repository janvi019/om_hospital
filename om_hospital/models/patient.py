import datetime
from odoo import api,fields,models

class HospitalPatient(models.Model):
	_name = "hospital.patient"
	_inherit = ["mail.thread","mail.activity.mixin"]
	_description = "Hospital Patient"
	_rec_name = "name"

	name = fields.Char(string="Name",tracking=True)
	active = fields.Boolean(string="Active", default=True)
	dob = fields.Date(string="DOB")
	age = fields.Integer(string="Age")
	patient_age = fields.Integer(compute="_compute_patient_age", store=False)
	ref = fields.Char(string="Reference")
	gender = fields.Selection([('male','Male'),('female','Female')],string="Gender",tracking=True,default='female')
	appointment_id = fields.Many2one('hospital.appointment',string="Appointment")

	@api.depends("dob")
	def _compute_patient_age(self):
		print("\n\n\n\n\n")
		print("Compute Patient Age is called")
		print("Self is : ", self)

		for rec in self:
			print("\n\n")
			print("Rec is : ", rec)
			print("DOB is : ", rec.dob)
			if rec.dob:
				current_year = datetime.datetime.now().year
				print("Current Year is : ", current_year)
				print("Date of birth year is : ", rec.dob.year)
				rec.patient_age = current_year - rec.dob.year
			else:
				rec.patient_age = 0
			print("Age is : rec.patient_age")
			print("\n\n")
		
		print("\n\n\n\n\n")
