# -*- coding: utf-8 -*-

from odoo import fields, models

class EmployeeDemo(models.Model):
    _name = 'employee.demo.ept'
    _description = 'Employee Demo'

    employee_name = fields.Char(string="Name of Employee", help="Name of Employee")
    department = fields.Char(string="Department", help="Department Name of Employee")
    job_position = fields.Char(string="Job Position", help="Job Position of Employee")
    salary = fields.Float(string="Salary", help="Salary")
    hire_date = fields.Date(string="Hire Date", help="Employee's Hire Date")
    gender = fields.Selection(selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')])
    job_type = fields.Selection(selection=[('Permanent', 'Permanent'), ('Ad_Hoc', 'Ad_Hoc')])