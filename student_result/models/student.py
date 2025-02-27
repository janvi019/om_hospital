from odoo import api,fields,models

class SchoolStudent(models.Model):
	_name = "school.student"
	_inherit = ["mail.thread","mail.activity.mixin"]
	_description = "School Student"

	name = fields.Char(string="Name",tracking=True)
	roll_no = fields.Integer(string="Roll No",tracking=True)
	percentage = fields.Float(string="Percentage",tracking=True)
	cla_ss = fields.Char(string="Class",tracking=True)

	result_ids = fields.One2many('student.result','student_id',string="Result")