# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

from odoo import models, fields, api

class PosPartnerInherit(models.Model):
    _inherit = "res.partner"

    sh_enable_auto_invoice = fields.Boolean(string="Enable POS Auto Invoice ?")


    @api.model
    def _load_pos_data_fields(self, config_id):
        res =  super()._load_pos_data_fields(config_id)
        res.append('sh_enable_auto_invoice')
        return res
