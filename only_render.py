# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Only Render",
    "author" : "Kevan Cress",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from bpy.types import Panel, Operator


def ui(self, context):
    layout = self.layout
    row = layout.row()
    row.operator("ui.onlyrender", text="Show only Render", icon='RESTRICT_RENDER_ON')

class OnlyRender(Operator):
    bl_idname = "ui.onlyrender"
    bl_label = "Expand or Collapse"
    bl_description = "Expand or Collapse all measure properties"
    bl_category = 'MeasureitArch'

    def execute(self, context):
        for obj in bpy.context.blend_data.objects:
            if obj.hide_render:
                obj.hide_viewport = True
            else:
                obj.hide_viewport = False
        return{'FINISHED'}


def register():
    bpy.types.VIEW3D_PT_view3d_properties.append(ui)
    bpy.utils.register_class(OnlyRender)

def unregister():
    bpy.types.VIEW3D_PT_view3d_properties.remove(ui)
    bpy.utils.unregister_class(OnlyRender)