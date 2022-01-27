# -*- coding: utf-8 -*-

from odoo import fields, models

class CityDemo(models.Model):

    _name = 'res.city.demo.ept'
    _description = 'city Demo'

    name_of_city = fields.Char(string="Name of City", help="City Name")
    state_name = fields.Char(string="State Name", help="State Name", copy=False)
    active = fields.Boolean(string="Active", default=True)
