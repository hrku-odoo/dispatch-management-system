from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    _stock_transport = fields.Boolean(string="Install Stock Transport Module", default=False, config_parameter='my_module.stock_transport')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('my_module.stock_transport', self._stock_transport)

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            _stock_transport=self.env['ir.config_parameter'].sudo().get_param('my_module.stock_transport', default=False)
        )
        return res
