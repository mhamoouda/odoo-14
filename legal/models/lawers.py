from odoo import models, fields, api
class lawyers(models.Model):
    # _inherit = ['hr.employee','hr.contract']

    _inherit = 'hr.employee'

    is_lawyer = fields.Boolean(string='is lawyers')
    lawyer_id = fields.Many2one('res.users', 'lawyer', default=lambda self: self.env.user)
    given_matters = fields.Many2one('product.product', string='Given Matters')


