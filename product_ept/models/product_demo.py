# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductDemo(models.Model):
    _name = 'product.demo.ept'
    _description = 'product Demo'

    product_name = fields.Char(string="Name of Product", help="Product Name")
    SKU = fields.Char(string="SKU of Product", help="SKU of the Product")
    barcode = fields.Char(string="Barcode", help="Barcode of the Product")
    product_be_sold = fields.Boolean(string="can this product be sold")
    product_type = fields.Selection(selection=[('Storable', 'Storable'), ('Consumable', 'Consumable'), ('Service', 'Service')])
    sale_price = fields.Float(string="Sale Price", help="Sales Price", digits=(6, 2))
    cost_price = fields.Float(string="Cost Price", help="Cost Price", digits=(6, 2))
    active = fields.Boolean(string="Active", default=True)
    warehouse = fields.Char(string="Warehouse", help="Warehouse")
    product_image = fields.Image(string="Image", help="Product Image")
    website_description = fields.Html(string="Description", help="WebSite Description")
    internal_note = fields.Text(string="Internal Note", help="Internal Note")


