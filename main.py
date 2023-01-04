from tkinter import *
from Circle import Circle


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

#def returnPressed(event):
  #calculate()


def calculate(event):
    # print('Button clicked')  # Test
   radius = user_input.get()
   if is_float(radius):
        user_input.delete(0, END)  # Clear input
        radius = float(radius)
        circle = Circle(radius)
        txt_field['state'] = 'normal'  # Txt field able
        txt_field.delete('1.0', END)  # Clear txt field
        txt_field.insert(END, 'Radius: ' + str(circle.radius) + '\n' + 'Diameter: ' + str(circle.get_diameter()) + '\n'
                         + 'Perimeter: ' + str(circle.get_perimeter()) + '\n' + 'Area: ' + str(circle.get_area()) + '\n')
        txt_field['state'] = 'disabled'  # Txt field is disabled


# Main window properties
window = Tk()
window.title('Geometry - Circle')  # Title text
# window.geometry('330x520')  # Window measures
window.resizable(False, False)

# Frames
frame_top = Frame(window, bg='#89CFF0', height=50)
frame_top.pack(fill='both')

frame_bottom = Frame(window, bg='#90EE90', height=50)
frame_bottom.pack(fill=BOTH)

# First line in top frame
lbl = Label(frame_top, text='Circle radius', bg='#89CFF0')
lbl.pack(side=LEFT)

user_input = Entry(frame_top)
user_input.pack(side=LEFT)
user_input.focus()

btn_calc = Button(frame_top, text='Calculate', command=lambda: calculate(0))
btn_calc.pack(side=LEFT, padx=4, pady=4)

# Bind Entry key
window.bind('<Return>', lambda event: calculate(event))
# window.bind('<Return>', returnPressed)

# Large text field on green
txt_field = Text(frame_bottom, state=DISABLED)
txt_field.pack(side=LEFT, padx=4, pady=4)



# No MVC last line
window.mainloop()
