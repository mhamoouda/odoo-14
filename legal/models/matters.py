from odoo import models, fields, api
class matters(models.Model):

    _inherit ='crm.lead'


    coloumns = fields.Char('nitesh' , required= True)




