# -*- coding: utf-8 -*-

from odoo import fields, models

class StateDemo(models.Model):

    _name = 'res.state.demo.ept'
    _description = 'State Demo'

    name_of_state = fields.Char(string="Name of State", help="State Name")
    short_code_of_state = fields.Char(string="Short Code of State", help="Short Code")
    country_name = fields.Char(string="Country Name", help="Country Name", copy=False)
    active = fields.Boolean(string="Active", default=True)