from odoo import models, fields, api

class InheritInventory(models.Model):
    _inherit = 'stock.picking.batch'

    dock = fields.Many2one('model.dock',string="Dock")

    vehicle = fields.Many2one("fleet.vehicle","Vehicle",plceholder="Opel GJ45XC1234")

    category = fields.Many2one("fleet.vehicle.model.category",String="Vehicle Category")

    category_weight = fields.Float(related="category.max_weight",store=True)
    category_volume = fields.Float(related="category.max_volume",store=True)

    weight = fields.Float(compute="_compute_weight", string="Weight", store=True)

    @api.depends('move_ids')
    def _compute_weight(self):
        for record in self:
            current_weight = 0
            for move_id in record.move_ids:
                current_weight = current_weight + move_id.product_qty*move_id.product_id.weight

            if record.category_weight >0:
                record.weight = (current_weight / record.category_weight)*100
            else:
                record.weight = 1
            
            if record.weight>100:
                record.weight = 100

