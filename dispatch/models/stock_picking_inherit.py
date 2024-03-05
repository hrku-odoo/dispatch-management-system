from odoo import models, fields, api

class InheritStockPicking(models.Model):
    _inherit = "stock.picking"

    shipping_volume = fields.Float(compute="_compute_shipping_volume", string="Volume")
    shipping_weight = fields.Float(compute="_compute_shipping_weight", string="Weight")

    @api.depends('product_id.weight','product_id.volume','move_line_ids.quantity')
    def _compute_shipping_volume(self):
        for record in self:
            curr=0
            for move_id in record.move_ids:
                curr = curr + move_id.product_qty*move_id.product_id.volume
                record.shipping_volume = curr


    @api.depends('product_id.weight','product_id.volume','move_line_ids.quantity')
    def _compute_shipping_weight(self):
        for record in self:
            curr=0
            for move_id in record.move_ids:
                curr = curr + move_id.product_qty*move_id.product_id.weight
                record.shipping_weight = curr