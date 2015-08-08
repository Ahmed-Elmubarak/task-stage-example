# -*- coding: utf-8 -*-
########################################################################
#  __openerp__.py
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
{
    'name': 'Project Stages',
    'version': '0.1',
    'author': 'Ahmed M.Elmubarak',
    'website': 'minmi9x@hotmail.com',
    'category': 'Project Management',
    'sequence': 111,
    'summary': 'Project Stages',
    'depends': ['project'],
    'description': """
This example will hide the oechatter depends on specific stage
==============================================================
""",
    'data': ['project_view.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
