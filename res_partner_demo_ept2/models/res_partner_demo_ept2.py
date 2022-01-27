# -*- coding: utf-8 -*-

from odoo import fields, models

class PartnerDemo2(models.Model):

    _name = 'res.partner.demo.ept2'
    _description = 'Partner Demo 2'

    name = fields.Char(string="Name", help="Name of Partner")
    email = fields.Char(string="Email", help="Email")
    street1 = fields.Char(string="Street1", help="Street1")
    street2 = fields.Char(string="Street2", help="Street2")
    city = fields.Char(string="City", help="City")
    state = fields.Char(string="State", help="State")
    zip_code = fields.Char(string="Zip_code", help="Zip_code")
    country = fields.Char(string="Country", help="Country")
    birthdate = fields.Datetime(string="Birth Date", help="Date Of Birth")
    age = fields.Integer(string="Age", help="age")
    weight = fields.Float(string="Weight", help="Weight")
    description = fields.Html(string="Description", help="Description")
    gender = fields.Selection(selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')])
    details = fields.Html(string="Details", help="Details")
    is_spectacles = fields.Boolean(string="Spectacles", help="Spectacles")
    photo = fields.Image(string="Image", help="Photo", max_width=128, max_height=128)

