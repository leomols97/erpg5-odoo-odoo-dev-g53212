from odoo import fields, models

class ResPartner (models.Model):
    _inherit = 'res.partner'

    todo_ids = fields.Many2many('todo.task', string='Tâches de la teamSS') # One task can have many res.partner