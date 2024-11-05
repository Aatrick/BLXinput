import XInput 
import customtkinter
import random

print(XInput.get_connected())
for i in range(4):
    if XInput.get_connected()[i]:
        index = i
        break
print(XInput.get_state(index))
print(XInput.get_battery_information(index))


def randomize():
    l_slider.set(random.randint(0, 100))
    r_slider.set(random.randint(0, 100))
    XInput.set_vibration(index, l_slider.get()/100, r_slider.get()/100)
    print(f"Left: {l_slider.get()}, Right: {r_slider.get()}")


app = customtkinter.CTk()
app.geometry("475x300")
app.title("Vibrator Control")

title = customtkinter.CTkLabel(app, text="Vibrator Control")
title.grid(row=0, column=1)

#make two vertical sliders side by side
l_slider = customtkinter.CTkSlider(app, from_=0, to=100, orientation="vertical")
l_labl = customtkinter.CTkLabel(app, text="Left Vibrator")# place the label under the left slider
l_slider.grid(row=1, column=0, padx=50)
l_labl.grid(row=2, column=0, padx=50)

l_slider.bind("<ButtonRelease-1>", lambda event: XInput.set_vibration(index, l_slider.get()/100, r_slider.get()/100))

r_slider = customtkinter.CTkSlider(app, from_=0, to=100, orientation="vertical")
r_labl = customtkinter.CTkLabel(app, text="Right Vibrator")
r_slider.grid(row=1, column=2, padx=50)
r_labl.grid(row=2, column=2, padx=50)

r_slider.bind("<ButtonRelease-1>", lambda event: XInput.set_vibration(index, l_slider.get()/100, r_slider.get()/100))

random_button = customtkinter.CTkButton(app, text="Random", command=lambda: randomize())
random_button.grid(row=3, column=1)

l_slider.set(0)
r_slider.set(0)

app.mainloop()