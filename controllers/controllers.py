# -*- coding: utf-8 -*-
# from odoo import http


# class DjbcApp(http.Controller):
#     @http.route('/djbc_app/djbc_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/djbc_app/djbc_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('djbc_app.listing', {
#             'root': '/djbc_app/djbc_app',
#             'objects': http.request.env['djbc_app.djbc_app'].search([]),
#         })

#     @http.route('/djbc_app/djbc_app/objects/<model("djbc_app.djbc_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('djbc_app.object', {
#             'object': obj
#         })
