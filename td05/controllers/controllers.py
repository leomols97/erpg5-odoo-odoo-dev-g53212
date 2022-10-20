# -*- coding: utf-8 -*-
# from odoo import http


# class Td05(http.Controller):
#     @http.route('/td05/td05/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/td05/td05/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('td05.listing', {
#             'root': '/td05/td05',
#             'objects': http.request.env['td05.td05'].search([]),
#         })

#     @http.route('/td05/td05/objects/<model("td05.td05"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('td05.object', {
#             'object': obj
#         })
