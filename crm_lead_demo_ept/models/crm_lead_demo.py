# -*- coding: utf-8 -*-

from odoo import fields, models


class crmLeadDemo(models.Model):
    _name = 'crm.lead.demo.ept'
    _description = 'Crm Lead Demo'

    name = fields.Char(string="Customer Name", help="Name of Customer", required=True)
    customer_email = fields.Char(string="Customer Email", help="Email of Customer", required=True)
    customer_phone = fields.Char(string="Customer Phone", help="Phone Number of Customer", required=True)
    expected_revenue = fields.Float(string="Expected revenue", help="Expected revenue", digits=(6, 2))
    sales_person = fields.Char(string="Sales Person", help="Sales Person", required=True)
    sales_team = fields.Char(string="Sales Team", help="Sales Team")
    # sales_team = fields.Char(string="Sales Team", help="Sales Team", default='Testing', readonly=True, store=True)
    campaign = fields.Char(string="Campaign", help="Campaign")
    channel = fields.Selection(selection=[('Facebook', 'Facebook'),
                                          ('Whatsapp', 'Whatsapp'),
                                          ('Email', 'Email'),
                                          ('Newspaper', 'Newspaper'),
                                          ('Television', 'Television'),
                                          ('PhoneCall', 'PhoneCall'),
                                          ('SMS', 'SMS'),
                                          ('GoogleAds', 'GoogleAds'),
                                          ], required=True)
    state = fields.Selection([
        ('New', 'New'),
        ('Qualified', 'Qualified'),
        ('Proposition', 'Proposition'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    ], string='State', default='New', tracking=True)
    next_followup_date = fields.Date(string="Next Follow Up Date", help="Next FollowUp Date", required=True)
    won_date = fields.Date(string="Won Date", help="Won Date")
    lost_reason = fields.Text(string="Lost Reason", help="Lost Reason")
