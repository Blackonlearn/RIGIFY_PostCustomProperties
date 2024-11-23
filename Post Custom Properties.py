import bpy

Bone = "Properties"
# New block of code to insert in place of `if is_selected({'Properties'}):`
new_code = f'''
# Custom Properties of {Bone} Bones
        if is_selected({{'{Bone}'}}):
            emit_rig_separator()
            
            #Dynamics
            row = layout.row()
            row.label(text= "Dynamic Bone Settings", icon = 'IPO_ELASTIC')
            row = layout.row()
            
            #Dynamics sliders
            layout.prop(pose_bones['Properties'], '["prop"]', text='Ponytail', slider=True)
            layout.prop(pose_bones['Properties'], '["prop1"]', text='Front Bangs', slider=True)
            
            #Clothing
            row = layout.row()
            group1 = layout.row(align=True)
            row.label(text= "Clothing Switches", icon = 'MOD_CLOTH')
            
            #Clothing Sliders
            props = layout.prop(pose_bones['Properties'],'["prop2"]', text='Mask', slider=True)
            props = layout.prop(pose_bones['Properties'],'["prop3"]', text='Skin', slider=True)
            
            #Mechanisms
            row = layout.row()
            group1 = layout.row(align=True)
            row.label(text= "Visibility", icon = 'HIDE_OFF')
            
            #Mechanisms Sliders
            props = layout.prop(pose_bones['Properties'],'["prop4"]', text='Hair', slider=True)
            props = layout.prop(pose_bones['Properties'],'["prop5"]', text='Head', slider=True)
'''

# Find the A.py text block (renamed rig_ui.py in this context)
a_text = bpy.data.texts.get("rig_ui.py")
if a_text is None:
    print("rig_ui.py text block not found.")
else:
    # Read the lines of rig_ui.py
    a_lines = a_text.as_string().splitlines()

    # Find the location of the `if is_selected({'Properties'}):` block
    insertion_point = None
    for index, line in enumerate(a_lines):
        if line.strip() == f"if is_selected({{'{Bone}'}}):":  # Use the value of Bone dynamically
            insertion_point = index  # The `if is_selected({'Properties'}):` line itself
            break

    # If the block is found, replace the whole block with the new code
    if insertion_point is not None:
        # Find the block's end by checking for indentation (next unindented line)
        block_end = insertion_point + 1
        while block_end < len(a_lines) and a_lines[block_end].startswith(" "):
            block_end += 1

        # Remove the entire block (from `if is_selected({'Properties'}):` to the next unindented line)
        del a_lines[insertion_point:block_end]

        # Insert the new block of code
        a_lines.insert(insertion_point, new_code.strip())

        # Update the content of rig_ui.py
        a_text.clear()
        a_text.write("\n".join(a_lines))

        print("Code replaced in rig_ui.py.")
    else:
        print(f"if is_selected({{'{Bone}'}}): block not found.")
