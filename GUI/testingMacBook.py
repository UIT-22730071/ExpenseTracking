import customtkinter
from styles import frame_options_color, frame_main_color, button_color
from PIL import Image


class OptionsButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, button_names, image_paths):
        super().__init__(master, fg_color="transparent")
        self.button_names = button_names
        self.image_paths = image_paths
        self.currently_pressed = None
        self.buttons = []
        images = []

        for image_path in self.image_paths:
            image = customtkinter.CTkImage(light_image=Image.open(image_path),
                                           dark_image=Image.open(image_path),
                                           size=(40, 40))
            images.append(image)

        for i, name in enumerate(self.button_names):
            button = customtkinter.CTkButton(self, text=name, height=60, width=180, fg_color="transparent",
                                             border_color=button_color, border_width=2, hover_color=button_color,
                                             image=images[i], font=("Helvetica", 15, "bold"),
                                             corner_radius=10, command=lambda index=i: self.activate_buttons(index))
            button.grid(row=i, column=0, sticky="w", padx=10, pady=(0, 20))
            self.buttons.append(button)

    def activate_buttons(self, button_index):
        # Reset previously pressed button (if any)
        if self.currently_pressed is not None:
            self.currently_pressed.configure(fg_color="transparent")  # Change back to regular color

        # Update currently pressed button and highlight it
        self.currently_pressed = self.buttons[button_index]
        self.currently_pressed.configure(fg_color=button_color)  # Change to pressed color

        # (Optional) Add additional actions here, like displaying specific content based on the pressed button
        print(f"Button {button_index+1} ({self.buttons[button_index].cget('text')}) pressed")


class ExpenseTrackingApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Expense Tracking')
        self.geometry('800x600')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        options_frame = customtkinter.CTkFrame(self, fg_color=frame_options_color)
        options_frame.grid(row=0, column=0, sticky="nsw", padx=10, pady=10)
        self.options_button_frame = OptionsButtonFrame(options_frame, ["Accounts", "Debts", "Economy"],
                                                       ["assets/accounting.png", "assets/debt.png", "assets/analytics.png"])
        self.options_button_frame.grid(row=0, column=0, sticky="nsew", pady=(20, 10))


app = ExpenseTrackingApp()
app.mainloop()
