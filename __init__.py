bl_info = {
    "name": "Bone Straightener",
    "author": "Milk Man",
    "version": (1, 0),
    'blender': (3, 6, 18),
    "location": "View 3D > Tool Shelf > Bone Straightener",
    "description": "Straightens all selected bones while in edit mode.",
    "category": "Bones & Armatures",
}

import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )
from . import bone_straightener

class MySettings(PropertyGroup):

    AutoDisconnectBones : BoolProperty(
        name="AutoDisconnectBones",
        description="automatically disconnect bones, if you don't check this the result may not look good. (note, this will disconnect them. Not unparent them.",
        default = True
        )
    ShrinkBones : BoolProperty(
        name="ShrinkBones",
        description="automatically shrink bones to the size they would be if you exported a model from a heavy iron game.",
        default = False
    )
class VIEW3D_PT_my_custom_panel(bpy.types.Panel):
    
    #Where panel will be added in UI
    bl_space_type = "VIEW_3D" #3d Viewport
    bl_region_type = "UI" #Sidebar
    
    #Labels
    bl_category = "Bone Straightener"
    bl_label = "Bone Straightener"
    
    def draw(self, context):
        global mytool
        row = self.layout.row()
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        row.operator
        layout.label (text="Plugin by Milk Man.")
        layout.prop(mytool, "AutoDisconnectBones", text="Automatically disconnect bones")
        layout.prop(mytool, "ShrinkBones", text="Shrink bones to Heavy Iron's native size")
        layout.operator("straighten_bones.straightenbones", text="Straighten Bones")
        #row.operator("straighten_bones.straightenbones", text="fsdfsd")
        #layout.operator(mytool, "straighten_bones.bone_straightener", text="Straighten Bones")

class Straighten_Bones(bpy.types.Operator):
    bl_idname = "straighten_bones.straightenbones"
    bl_label = "StraightenAABones"
    bl_description = "Straightens bones to were they are all pointing straight up."
    bl_options = {'PRESET', 'UNDO'}
    
    def execute(self,context):
        bone_straightener.bone_straightener_main.execute(self,bpy.context.scene.my_tool.AutoDisconnectBones, bpy.context.scene.my_tool.ShrinkBones)
        return {'FINISHED'}
classes = (
    MySettings,
    Straighten_Bones,
    VIEW3D_PT_my_custom_panel,
    
)

def register(): #Registering classes (The settings and the panel itself)    
    from bpy.utils import register_class
    for class_ in classes:
        register_class(class_)

    bpy.types.Scene.my_tool = PointerProperty(type=MySettings)

    
    
def unregister():
    from bpy.utils import unregister_class
    for class_ in reversed(classes):
        unregister_class(class_)

    del bpy.types.Scene.my_tool
    
    
if __name__ == "__main__":
    register()