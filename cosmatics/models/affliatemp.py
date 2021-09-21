from odoo import models, fields, api
class lawyers(models.Model):
    # _inherit = ['hr.employee','hr.contract']

    _inherit = 'hr.employee'

    is_affliate = fields.Boolean(string='is Affiliate')
    marketer_id = fields.Many2one('res.users', 'lawyer', default=lambda self: self.env.user)



