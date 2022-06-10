
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="RPG Game"):
    dpg.add_text("Enemy One stats")
    dpg.add_button(label="Choose")
    dpg.add_combo(label="Choose one option")
    dpg.add_input_text(label="say something")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()