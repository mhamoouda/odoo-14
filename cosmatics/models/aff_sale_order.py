from datetime import timedelta
from odoo import models, fields, api, exceptions, _

#create the frist class callled courses
class affiliate(models.Model):
    # _name = 'sale.order.marketer'
    _inherit = 'sale.order'
    _description = "affiliate marketers"
    aff_name = fields.Many2one('res.users', string='Marketer Name', ondelete='cascade', index=True)
    x = fields.Many2many('cosmatics.affiliate')
    client_address = fields.Many2one('res.country', string="client address", required=True)
    client_phone1 = fields.Integer(string="phone number1",  required=True)
    client_phone2 = fields.Integer(string="phone number2", required=True)



