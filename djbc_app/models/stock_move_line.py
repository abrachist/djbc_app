from odoo import models, fields, api


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    picking_djbc_docs = fields.Selection(related='picking_id.djbc_docs', readonly=True)
    picking_djbc_date = fields.Datetime(related='picking_id.djbc_date', readonly=True)
    picking_djbc_approval = fields.Boolean(related='picking_id.djbc_approval')
    picking_djbc_note = fields.Text(related='picking_id.djbc_note')
    location_dest_usage = fields.Selection(related='location_dest_id.usage')
    location_source_usage = fields.Selection(related='location_id.usage')
    