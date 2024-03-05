from odoo import models, fields

class Dock(models.Model):
    _name = "model.dock"
    _description = "Dock"

    name = fields.Char("Name", required=True)