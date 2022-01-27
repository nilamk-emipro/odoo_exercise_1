# -*- coding: utf-8 -*-

from odoo import fields, models

class CountryDemo(models.Model):

    _name = 'res.country.demo.ept'
    _description = 'Country Demo'

    name_of_country = fields.Char(string="Name of Country", help="Country Name")
    short_code_of_country = fields.Char(string="Short Code of Country", help="Short Code")
    active = fields.Boolean(string="Active", default=True)
