from odoo import models, fields, api
class partner(models.Model):
    _inherit = 'res.partner'

    is_client = fields.Boolean(string='Client Id')
    # lawer = fields.Boolean("instructor", default=False)
    # matter_ids = fields.Many2many('legal.law', string="given matters", readonly=True)


# class lawers(models.Model):
#     # _inherit = ['hr.employee','hr.contract']
#     _inherit = 'hr.employee'
#     is_lawyer = fields.Boolean(string='Client Id')
#     employee = fields.Char('Employee')
#     given_matters = fields.One2many('hr.employee', 'legal.law', string='Given Matters')