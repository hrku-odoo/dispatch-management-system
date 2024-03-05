from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class InheritInventory(models.Model):
    _inherit = 'stock.picking.batch'

    dock = fields.Many2one('model.dock',string="Dock")

    vehicle = fields.Many2one("fleet.vehicle",string="Vehicle")

    category = fields.Many2one("fleet.vehicle.model.category",string="Vehicle Category")
    partner_ids = fields.Many2one('res.partner')
    driver_id = fields.Many2one("fleet.vehicle.driver_id", string="Icon")
    # partner_image = fields.Binary(related='partner_ids.driver_id')
    
    weight = fields.Float(compute="_compute_weight", string="Weight", store=True)
    volume = fields.Float(compute="_compute_volume", string="Volume", store=True)
    transfers = fields.Integer(compute="_compute_transfers", string="Transfers", store="True")
    lines = fields.Integer(compute="_compute_lines", string="Lines", store="True")

    @api.depends('picking_ids.shipping_weight')
    def _compute_weight(self):
        for record in self:
            current_weight = 0
            for move_id in record.move_ids:
                current_weight = current_weight + move_id.product_qty*move_id.product_id.weight

            if record.category.max_weight >0:
                record.weight = (current_weight / record.category.max_weight)*100
            else:
                record.weight = 1
            
            if record.weight>100:
                record.weight = 100


    @api.depends('picking_ids.shipping_volume')
    def _compute_volume(self):
        for record in self:
            current_volume = 0
            for move_id in record.move_ids:
                current_volume = current_volume + move_id.product_qty*move_id.product_id.volume

            if record.category.max_volume >0:
                record.volume = (current_volume / record.category.max_volume)*100
            else:
                record.volume = 1
            
            if record.volume>100:
                record.volume = 100

    @api.depends('picking_ids')
    def _compute_transfers(self):
        for record in self:
            curr = len(record.picking_ids)
            record.transfers = curr
    
    @api.depends('move_line_ids')
    def _compute_lines(self):
        for record in self:
            curr = len(record.move_line_ids)
            record.lines = curr

