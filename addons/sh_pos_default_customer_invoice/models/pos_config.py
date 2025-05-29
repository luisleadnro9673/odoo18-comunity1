# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

from odoo import models, fields

class PosConfig(models.Model):
    _inherit = "pos.config"

    sh_is_default_invoice = fields.Boolean(string="Is Default Invoice ? ")
    sh_pos_default_invoice = fields.Selection([('customer_wise_invoice', "Individual Customer Wise Invoice"), ('global_default_invoice', "Invoice For All Customers")], string="Default Invoice ?", default="global_default_invoice")

