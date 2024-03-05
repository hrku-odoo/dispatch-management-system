from odoo import fields, models
class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    module_dispatch = fields.Boolean("Dispatch Management System")