# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

from odoo import models, fields

class ResConfigSettiongsInhert(models.TransientModel):
    _inherit = "res.config.settings"

    pos_sh_is_default_invoice = fields.Boolean(
        related="pos_config_id.sh_is_default_invoice", readonly=False)
    pos_sh_pos_default_invoice = fields.Selection(
        related="pos_config_id.sh_pos_default_invoice", readonly=False)
