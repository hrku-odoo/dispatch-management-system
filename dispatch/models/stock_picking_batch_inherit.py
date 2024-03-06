from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class InheritInventory(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('model.dock',string="Dock")

    vehicle_id = fields.Many2one("fleet.vehicle",string="Vehicle")

    category_id = fields.Many2one("fleet.vehicle.model.category",string="Vehicle Category")
    partner_id = fields.Many2one('res.partner')

    total_weight = fields.Float(string="Weight",readonly=True)
    total_volume = fields.Float(string="Volume", readonly=True)
    
    weight = fields.Float(compute="_compute_weight", store=True)
    volume = fields.Float(compute="_compute_volume", store=True)
    transfers = fields.Integer(compute="_compute_transfers", string="Transfers", store="True")
    lines = fields.Integer(compute="_compute_lines", string="Lines", store="True")

    @api.depends('picking_ids.shipping_weight')
    def _compute_weight(self):
        for record in self:
            current_weight = 0
            for move_id in record.move_ids:
                current_weight = current_weight + move_id.product_qty*move_id.product_id.weight
                record.total_weight = current_weight

            if record.category_id.max_weight >0:
                record.weight = (current_weight / record.category_id.max_weight)*100
            
            if record.weight>100:
                record.weight = 100


    @api.depends('picking_ids.shipping_volume')
    def _compute_volume(self):
        for record in self:
            current_volume = 0
            for move_id in record.move_ids:
                current_volume = current_volume + move_id.product_qty*move_id.product_id.volume
                record.total_volume = current_volume

            if record.category_id.max_volume >0:
                record.volume = (current_volume / record.category_id.max_volume)*100
            
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

    @api.depends('weight','volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name + ":" + str(round(record.weight)) + " kg / " + str(round(record.volume)) + " m^3"
