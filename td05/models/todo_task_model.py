from odoo import fields, models

class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char('Name of the task', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    date_deadline = fields.Date('Deadline')
    user_id = fields.Many2one('res.users', 'Responsible')
    team_id = fields.Many2one('res.partner', 'Team')