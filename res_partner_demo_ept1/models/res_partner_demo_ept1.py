# -*- coding: utf-8 -*-

from odoo import fields, models

class PartnerDemo1(models.Model):

    _name = 'res.partner.demo.ept1'
    _description = "Partner Demo 1"

    name = fields.Char(string="Name", help="Name of the Partner")
    email = fields.Char(string="Email", help="Email Address")
    street1 = fields.Char(string="Street1", help="Street1")
    street2 = fields.Char(string="Street2", help="Street2")
    city = fields.Char(string="City", help="City")
    state = fields.Char(string="State", help="State")
    zip_code = fields.Char(string="Zip Code", help="Zip code")
    country = fields.Char(string="Country", help="Country")
    birthdate = fields.Datetime(string="Birth Date", help="Date of Birth")
    age = fields.Integer(string="Age", help="Age")
    weight = fields.Float(string="Weight", help="Weight")
    gender = fields.Selection(selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')])
    is_spectacles = fields.Boolean(string="Spectacles", help="Spectacles")
    photo = fields.Image(string="Image", help="Photo", max_width=128, max_height=128)
    # image_1920 = fields.Image("Image", related='employee_id.image_1920', compute_sudo=True)
    description = fields.Html(string="Description", help="Description")
    details = fields.Html(string="Details", help="Details")
