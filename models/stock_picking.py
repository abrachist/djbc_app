# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    djbc_docs = fields.Selection([('bc2.3', 'BC 2.3 (PIB)'), ('bc3.0', 'BC 3.0 (PEB)'), ('bc2.5', 'BC 2.5'), ('bc2.6', 'BC 2.6'), ('bc2.7', 'BC 2.7'), ('bc4.0', 'BC 4.0')],
                                    string='DJBC Docs', copy=False, help="Kind of document transfer item")
    djbc_date = fields.Datetime('DJBC Date', copy=False,
        help="Submission date djbc when items going to transfer to other place")
    djbc_approval = fields.Boolean('DJBC Checked', copy=False)
    djbc_note = fields.Text('DJBC Note', copy=False)

    
