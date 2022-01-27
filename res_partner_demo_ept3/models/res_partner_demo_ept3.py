# -*- coding: utf-8 -*-

from odoo import fields, models

class PartnerDemo3(models.Model):

    _name = 'res.partner.demo.ept3'
    _description = 'Partner Demo 3'

    name = fields.Char(string="Name", help="Partner Name")
    email = fields.Char(string="Email", help="Partner Email Address")
    street1 = fields.Char(string="Street1", help="Partner Address line 1")
    street2 = fields.Char(string="Street2", help="Partner Address Line 2")
    city = fields.Char(string="City", help="Partner City")
    state = fields.Char(string="State", help="Partner State")
    zip_code = fields.Char(string="Zip Code", help="Partner ZipCode")
    country = fields.Char(string="Country", help="Partner country")
    birthdate = fields.Datetime(string="BirthDate", help="Date of Birth")
    age = fields.Integer(string="Age", help="Partner Age")
    weight = fields.Float(string="Weight", help="Partner Weight")
    description = fields.Html(string="Description", help="Description")
    gender = fields.Selection(selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')])
    details = fields.Html(string="Details", help="Details")
    is_spectacles = fields.Boolean(string="Spectacles", help="Spectacles")
    photo = fields.Image(string="Image",help="Photo")