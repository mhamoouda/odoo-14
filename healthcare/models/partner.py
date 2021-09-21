
from odoo import models, fields, api
class res_partner(models.Model):
    _inherit = 'res.partner'

    is_patient = fields.Boolean(string='Patient')

