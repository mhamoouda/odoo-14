# -*- coding: utf-8 -*-

from odoo import models, fields, api


class legal(models.Model):
    _name = 'legal.law'
    _rec_name = 'client_id'

    @api.onchange('client_id')
    def _onchange_client(self):

        address_id = self.client_id
        self.partner_address_id = address_id

    def action_to_in_progress(self):
        for rec in self:
            rec.write({'state': 'in_progress'})

    def action_to_finished(self):
        for rec in self:
            rec.write({'state': 'finished'})

    def action_to_cancelled(self):
        for rec in self:
            rec.write({'state': 'cancelled'})

    def action_return_to_draft(self):
        for rec in self:
            rec.write({'state': 'draft'})


    date =fields.Date(string="Date",default=fields.Datetime.now)
    client_id = fields.Many2one('res.partner', domain=[('is_client', '=', True)], string = "client", required = True)
    photo= fields.Binary('client image')
    partner_address_id= fields.Many2one('res.partner', string= 'address')
    lawyer_ids = fields.Many2one('res.users', 'lawyer', default=lambda self: self.env.user)
    contact_no= fields.Integer(string="contact us", required= True)
    services = fields.Many2one('product.product', string='services')
    email = fields.Char(string="user@email.com")
    matter_details = fields.Text()
    matteer_type = fields.Selection([
        ('a', 'Criminal Law'),
        ('b', 'Civil Rights Law'),
        ('c', 'Environmental Law'),
        ('d', 'familly law '),
        ('f', 'Admiralty (Maritime) Law.'),
        ('g', 'Bankruptcy Law'),
        ('h', 'Entertainment Law'),
        ('i', 'Business (Corporate) Law'),
    ], string='Mtter Type', sort=False, default='a')
    brief_descr= fields.Text()
    documentations=fields.Char('Matter Documentations')
    file = fields.Binary(string='file', attachment=True)
    file_name = fields.Char("File Name")
    state = fields.Selection([('draft', 'Draft'), ('in_progress', 'Progress'), ('finished', 'Finished'), ('cancelled', 'Cancelled')], string="Status", readonly=True, default="draft")




    def opining_matters(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'client meetings',
            'view_mode': 'form,tree',
            'res_model': 'legal.law',
            'domain': [('product.id', '=', self.lawyer_ids)],
            'context': "{'create': False}"
        }

    def open_client_meeting(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'client meetings',
            'view_mode': 'form,tree',
            'res_model': 'client.meeting',
            'domain': [('client_id', '=', self.id)],
            'context': "{'create': False}"
        }









