from odoo import api, fields, models, exceptions

import logging

_logger = logging.getLogger(__name__)

class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char('Name of the task', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    date_deadline = fields.Date('Deadline')
    user_id = fields.Many2one('res.users', 'Responsible')
    team_id = fields.Many2many('res.partner')

    def do_clear_done(self):
        for task in self:
            if task.active:
                task.active = False
                _logger.info('This task active field has been set to false')
            else:
                raise exceptions.Warning("La tache est déjà inacive")
        return True