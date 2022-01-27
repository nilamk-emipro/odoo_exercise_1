# -*- coding: utf-8 -*-

from odoo import fields, models

class PartnerDemo4(models.Model):
    _name = 'res.partner.demo.ept4'
    _description = 'Partner Demo 4'

    name = fields.Char(string="Name", help="Name")
    email = fields.Char(string="Email", help="Email Address")
    street1 = fields.Char(string="Street1", help="Address1")
    street2 = fields.Char(string="Street2", help="Address2")
    city = fields.Char(string="city", help="city")
    state = fields.Char(string="State", help="state")
    zip_code = fields.Char(string="Zip Code", help="ZipCode")
    country = fields.Char(string="Country", help="Country")
    birthdate = fields.Datetime(string="Birth Date", help="Date of Birth")
    age = fields.Integer(string="Age", help="Age")
    weight = fields.Float(string="Weight", help="Weight")
    description = fields.Html(string="Description", help="Description")
    gender = fields.Selection(selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')])
    details = fields.Html(string="Details", help="Details")
    is_spectacles = fields.Boolean(string="Spectacles", help="Spectacles")
    photo = fields.Image(string="Image", help="Photo")

