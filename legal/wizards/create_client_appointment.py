from odoo import models , fields,api
class createAppointment(models.TransientModel):
    _name = 'client.appointment'
    _inherit = 'mail.thread'


    client_id = fields.Many2one('legal.law', string ="client")
    appointment_date= fields.Date(string="Appointment Data")
    gender = fields.Selection([('m', ',,male'),
        ('f', 'female')])

    def action_create_appointment(self):
        # search methods in odoo
        for rec in self:
            clients = self.env['client.appointment'].search([('gender', '=' ,'f')])
            print("female clients.........", clients)
            clients = self.env['client.appointment'].search([('gender', '=', 'm')])
            print(" male clients.........", clients)
            # odoo saerch count
            client_count = self.env['client.appointment'].search_count([])
            print("count clients.........", client_count)
            # female count
            client_count = self.env['client.appointment'].search_count([('gender', '=' ,'f')])
            print("female count clients.........", client_count)
            #male counr
            client_count = self.env['client.appointment'].search_count([('gender', '=', 'm')])
            print(" Male count clients.........", client_count)

            # odoo ref mathod
            # ref_clients = self.env.ref['external id ']
            # print("ref clients.........", ref_clients)

            #browse method in odoo
            result_browse = self.env['client.appointment'].browse([(5)])
            print("result_browse........." , result_browse)
            # browse with exists fuction
            if result_browse.exists():
                print("extistsssssssssssssssssssssss")
            else:
                print("notttttttttttttttttttttt extistsssssssssssssssssssssss")

            # function create
            # vals={
            #
            #     'client_id': 500,
            #
            # }
            #
            # created_record= self.env['client.appointment'].create(vals)
            # print("created_record       ", 'created_record')





