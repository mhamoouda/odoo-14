from odoo import models, fields, api
class partner(models.Model):
    _inherit = 'res.partner'
    instructor = fields.Boolean("instructor", default = False)
    session_ids= fields.Many2many('mat.sessions',  string ="attended sessions", readonly=True)
    youtube = fields.Char(string="youTub Channel")
    state = fields.Many2one('res.country', string="state")





