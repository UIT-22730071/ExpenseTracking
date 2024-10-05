import customtkinter
from customtkinter import CTkFrame, CTkButton
from GUI.styles import button_color, frame_options_color, frame_main_color
from PIL import Image


# Option Button
class OptionsButton(customtkinter.CTkButton):
    def __init__(self, master, button_text, image_path, active_color = None):
        image = customtkinter.CTkImage(light_image=Image.open(image_path),
                                       dark_image=Image.open(image_path),
                                       size=(40,40))

        self.active_color = button_color

        super().__init__(master, text=button_text, image=image, fg_color="transparent", font=("Helvetica", 15, "bold"),
                         corner_radius=10, width=130, height=60, anchor="w", border_color=button_color, border_width=2, hover_color=button_color)
        self.image = image


class InformationFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, value):
        super().__init__(master, width=200, height=80, fg_color=frame_options_color, corner_radius=10)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.value = value
        self.title = title

        image = customtkinter.CTkImage(light_image=Image.open("assets/logo.png"),
                                       dark_image=Image.open("assets/logo.png"),
                                       size=(20,20))
        text = customtkinter.CTkLabel(self, text=title, font=("Helvetica", 20, "bold"), image=image, compound="left", padx=10)
        text.grid(column=0, row=0, padx=20, pady=10)
        value = customtkinter.CTkLabel(self, text=value, font=("Helvetica", 25), text_color="green")
        value.grid(column=0, row=1, padx=10, pady=(0,10))







class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Expense Tracking")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # Options Frame
        options_frame = CTkFrame(self, fg_color=frame_options_color)
        options_frame.grid(column=0, row=0, rowspan=2 ,sticky="nsw")

        # Buttons
        accounts_btn = OptionsButton(options_frame, "Accounts", "assets/accounting.png")
        accounts_btn.grid(column=0, row=0, padx = 10, pady = 15)
        # accounts_indicator = customtkinter.CTkLabel(options_frame, text="", font=("Helvetica", 20, "bold"), fg_color=button_color, width=130, height=60, corner_radius=10)
        # accounts_indicator.grid(column=0, row=0, padx = 10, pady = 15)

        debts_btn = OptionsButton(options_frame, "Debts", "assets/debt.png")
        debts_btn.grid(column=0, row=1, padx = 10, pady = 15)

        economy_summary_btn = OptionsButton(options_frame, "Economy", "assets/analytics.png")
        economy_summary_btn.grid(column=0, row=2, padx = 10, pady = 15)
        # logo_img_path = customtkinter.CTkImage(light_image=Image.open("assets/logo.png"), dark_image=Image.open("assets/logo.png"), size=(60,60))
        # logo_image = customtkinter.CTkLabel(options_frame, text="Expense Tracking", image=logo_img_path, anchor="center", compound="top", pady=20, font=("Helvetica", 15, "bold"))
        # logo_image.grid(column=0, row=3, sticky="s", pady=(80,0))

        # Information Frame
        economy_summary = InformationFrame(self, "Economy Summary", "123,456,789đ")
        economy_summary.grid(column=1, row=0, sticky="nw", pady=10, padx=(20,0))
        add_img = customtkinter.CTkImage(light_image=Image.open("assets/plus.png"),
                                         dark_image=Image.open("assets/plus.png"),
                                         size=(40,40))
        add_account_button = CTkButton(self, text="Add Accounts", image=add_img, fg_color="transparent", anchor="center", font=("Helvetica", 20, "bold"))
        add_account_button.grid(column=2, row=0)



        # Main Frame
        main_frame = CTkFrame(self, fg_color=frame_main_color)
        main_frame.grid(column=1, row=1, columnspan=4 ,sticky="nsew", padx=20, pady=(0,20))


app = App()
app.mainloop()