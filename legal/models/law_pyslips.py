from odoo import models, fields, api
class presence(models.Model):

    _inherit =['hr.attendance' ,'hr.department']


    #dept= fields.Many2one('hr.department', string='Departement')
    #dept= fields.Boolean('Departement')
    emp = fields.Boolean()



