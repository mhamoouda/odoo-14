from odoo import models, fields, api
import calendar
import datetime
from datetime import datetime
class mettings(models.Model):
    _name ='client.meeting'
    _rec_name = 'client_id'

    @api.onchange('client_id')
    def _onchange_client(self):
        address_id = self.client_id
        self.partner_address_id = address_id

    client_id = fields.Many2one('res.partner', domain=[('is_client', '=', True)], string="client", required=True)
    calend = fields.Datetime (string="date" , default=datetime.now())
    partner_address_id = fields.Many2one('res.partner', string='address')
    meeting_info= fields.Char(string="meeting Details" , required=True)
    datee= fields.Date(default=fields.Date.today())



    def opining_client_meetings(self):
        print("operating")



