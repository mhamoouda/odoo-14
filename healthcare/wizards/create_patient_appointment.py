from odoo import models , fields,api
class createAppointment(models.TransientModel):
    _name = 'create.appointment'


    patient_id = fields.Many2one('healthcare.patiant', string ="patient")
    appointment_date= fields.Date(string="Appointment Data")


