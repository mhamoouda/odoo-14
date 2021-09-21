# -*- coding: utf-8 -*-
# from odoo import http


# class Cosmatics(http.Controller):
#     @http.route('/cosmatics/cosmatics/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cosmatics/cosmatics/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cosmatics.listing', {
#             'root': '/cosmatics/cosmatics',
#             'objects': http.request.env['cosmatics.cosmatics'].search([]),
#         })

#     @http.route('/cosmatics/cosmatics/objects/<model("cosmatics.cosmatics"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cosmatics.object', {
#             'object': obj
#         })
