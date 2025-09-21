# bpy.ops.wm.console_toggle() to show console window
import bpy
import math

class bone_straightener_main():
    b1_idname = "bone_straightener"
    b1_label = "Bone Straigthener"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,autoconnect,smallbones):
        mybones = bpy.context.selected_editable_bones
        if autoconnect == True:
            print("disconnecting bones")
            for bone in mybones:
                bone.use_connect = False


        for bone in mybones:
            bone.roll = 0
            print("current bone - ", bone)
            tail_values = bone.tail
            head_values = bone.head
            x_values = [tail_values.x, head_values.x]
            x_values.sort
            y_values = [tail_values.y, head_values.y]
            y_values.sort
            z_values = [tail_values.z, head_values.z]
            z_values.sort
            x_difference = x_values[1] - x_values[0]
            y_difference = y_values[1] - y_values[0]
            z_difference = abs(z_values[1] - z_values[0])
            
            bonelength = x_difference**2 + y_difference **2 + z_difference **2
            bonelength = math.sqrt(bonelength)
            print(bonelength)
            if smallbones == True:
                print("shrinking bones")
                bone.tail.z =  head_values.z + .05
                bone.tail.x = head_values.x
                bone.tail.y = head_values.y
            else:
                bone.tail.z = head_values.z + bonelength
                bone.tail.x = head_values.x
                bone.tail.y = head_values.y
        return {'FINISHED'}