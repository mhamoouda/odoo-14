# -*- coding: utf-8 -*-
# from odoo import http


# class Mat(http.Controller):
#     @http.route('/mat/mat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mat/mat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mat.listing', {
#             'root': '/mat/mat',
#             'objects': http.request.env['mat.mat'].search([]),
#         })

#     @http.route('/mat/mat/objects/<model("mat.mat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mat.object', {
#             'object': obj
#         })
