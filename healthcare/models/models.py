

from odoo import models,fields, api

class healthcare(models.Model):
    _name = 'healthcare.patiant'
    _rec_name = 'patient_id'

    @api.onchange('patient_id')
    def _onchange_patient(self):
        '''
        The purpose of the method is to define a domain for the available
        purchase orders.
        '''
        address_id = self.patient_id
        self.partner_address_id = address_id



    _description = 'healthcare patient management '
    patient_id = fields.Many2one('res.partner', domain=[('is_patient', '=', True)], string="Patient", required=True)
    name = fields.Char(string='patient name', required="True")
    photo = fields.Binary(string="Picture")
    partner_address_id = fields.Many2one('res.partner', string="Address", )
    date_of_birth =fields.Datetime(string="Date of Birthday")
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')], string='Marital Status')
    sex = fields.Selection([('male','Male'),('female','Female'),('other','other')], string="SEX", required="True")
    patiant_age = fields.Integer(string="Age")
    address= fields.Char(string ="Address ")
    blood_type = fields.Selection([
        ('a', 'A'), ('a+', 'A+'),
        ('b', 'B'), ('b+', 'B+'),
        ('ab', 'AB'), ('ab+', 'AB+'),
        ('o', 'O'), ('o+', 'O+'),
        ('other', 'Other')], string='Blood type', required=True)
    ethnitic_group= fields.Char(string="Ethentic group ")
    insurance = fields.Many2one('res.partner', string="insurance campany")
    rh = fields.Char(string="RH")
    familly= fields.Char("familly")
    Recievable= fields.Float(string="Reciavable")
    primary_care_doc = fields.Many2one('res.partner', string="Primary Care Doctor")



