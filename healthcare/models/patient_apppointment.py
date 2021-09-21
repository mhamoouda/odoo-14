from odoo import fields , models, api
class patient_Appointment(models.Model):
    _name = 'patient.appointment'
    #_inherit = 'mail.thread'

    name = fields.Char(string="Appointment ID" )
    is_invoiced = fields.Boolean(string="Invoiced", copy=False, default=False)
    instituation_partner_ids = fields.Many2one('res.partner', domian=[('is_institution', '=', 'True')],
                                               string="healthcare center")

    # create moule medical.inpatient.registration
    # inpatient_registration_id = fields.Many2one('medical.inpatient.registration', string="Inpatient Registration")
    # patient_status = fields.Selection([
    #     ('ambulatory', 'Ambulatory'),
    #     ('outpatient', 'Outpatient'),
    #     ('inpatient', 'Inpatient'),
    # ], string='Patient status', sort=False, default='outpatient')
    patient_id = fields.Many2one('healthcare.patiant', string='Patient', required=True)
    urgency_level = fields.Selection([
        ('a', 'Normal'),
        ('b', 'Urgent'),
        ('c', 'Medical Emergency'),
    ], string='Urgency Level', sort=False, default="b")

    appointment_date = fields.Datetime('Appointment Date', required=True, default=fields.Datetime.now)
    appointment_end = fields.Datetime('Appointment End', required=True)
    # create new module nmedical physician
    # doctor_id = fields.Many2one('medical.physician', 'Physician', required=True)
    no_invoice = fields.Boolean(string='Invoice exempt', default=True)
    validity_status = fields.Selection([
        ('invoice', 'Invoice'),
        ('tobe', 'To be Invoiced'),
    ], string='Status', sort=False, readonly=True, default='tobe')

    appointment_validity_date = fields.Datetime('Validity Date')
    # res module called product.product  product with filed type service
    # consultations_id = fields.Many2one('product.product', string='Consultation Service', required=True)
    comments = fields.Text(string="Info")
# status bar in header
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirm'),
        ('cancel', 'Cancel'),
        ('done', 'Done')], string="State", default='draft')
    invoice_to_insurer = fields.Boolean('Invoice to Insurance')
    # creation new modle or class called medical.patient.psc
#     medical_patient_psc_ids = fields.Many2many('medical.patient.psc', string='Pediatrics Symptoms Checklist')
#     # creation new modle called mediacal prescription order
#     medical_prescription_order_ids = fields.One2many('medical.prescription.order', 'appointment_id', string='Prescription')
# # create new modle called medical insurance
    duration =fields.Integer(string='Duration')
    # insurer_id = fields.Many2one('medical.insurance' , string = "insurer")

    @api.onchange('patient_id')
    def onchange_name(self):
        ins_obj = self.env['medical.insurance']
        ins_record = ins_obj.search([('medical_insurance_partner_id', '=', self.patient_id.patient_id.id)])
        if len(ins_record) >= 1:
            self.insurer_id = ins_record[0].id
        else:
            self.insurer_id = False

























