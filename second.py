import customtkinter 

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("400x400")

root.title("Login")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx = 20 , pady=20, fill="both", expand = True)

def login(): 
    print("MISSION COMPLETE")

label = customtkinter.CTkLabel(master=frame, text="Login System" )
label.pack(padx = 12, pady = 10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(padx = 12, pady = 10 )

entry2 = customtkinter.CTkEntry(master = frame, placeholder_text="Password", show = "*")
entry2.pack(padx = 12, pady = 10)

button = customtkinter.CTkButton(master = frame, text = "Login", command = login) 
button.pack(padx = 12, pady = 10)

root.mainloop()

