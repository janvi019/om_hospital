from odoo import api,fields,models

class StudentResult(models.Model):
	_name = "student.result"
	_description = "Student Result"
	_rec_name = 'student_id'

	student_id = fields.Many2one('school.student',string="Name")
	declaration_date = fields.Date(string="Declaration Date",default=fields.Date.context_today)
	

	cla_ss = fields.Char(string="Class")
	roll_no = fields.Integer(string="Roll No")
	percentage = fields.Float(string="Percentage")
	chemistry = fields.Integer(string="Chemistry")
	math = fields.Integer(string="Mathes")
	physics = fields.Integer(string="Physics")
	english = fields.Integer(string="English")