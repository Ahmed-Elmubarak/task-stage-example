# -*- coding: utf-8 -*-
########################################################################
#  __project__.py
#  
#  Copyright 2015 Ahmed M.Elmubarak <minmi9x@hotmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
########################################################################

from openerp.osv import fields, osv

class task(osv.osv):
    _inherit = 'project.task'

    def on_change_stage(self, cr, uid, ids, stage, context=None):
        res = {}
        if stage:
            stage_name = self.pool['project.task.type'].browse(cr, uid, stage, context=context).name
            res['value'] = {'stage_name': stage_name}
        else:
            res['value'] = {'stage_name': ''}
        return res

    _columns = {
        'stage_name': fields.char('Stage Name'),
    }

    def write(self, cr, uid, ids, vals, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]

        # stage change: update stage_name
        if 'stage_id' in vals:
            vals['stage_name'] = self.pool['project.task.type'].browse(cr, uid, vals['stage_id'], context=context).name
        return super(task, self).write(cr, uid, ids, vals, context=context)
