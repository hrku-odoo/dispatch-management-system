from odoo import models, fields, api

class TransportManagementSystem(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string="Max Weight (Kg)")
    max_volume = fields.Float(string="Max Volume (m3)")


    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight},{record.max_volume})"