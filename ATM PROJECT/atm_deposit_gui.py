import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")




window = ctk.CTk()
window.geometry("400x800")
window.resizable(width=False, height=False)
window.title("LUX BANK")

frame = ctk.CTkFrame(master=window, width=400, height=100)
frame.pack(fill="both")
frame_label = ctk.CTkLabel(frame, text="Deposit", height=100, width=200, font=("Arial", 30))
frame_label.grid()

#frame = ctk.CTkFrame(master=window, width=200, height=50)
#frame.pack( padx= 30, fill="both")


frame = ctk.CTkFrame(window)
frame.pack(padx= 30, pady=50, fill="both")
frame2 = ctk.CTkFrame(frame)
frame2.pack(padx= 30, pady=50, fill="both", side="top")
frame_label = ctk.CTkLabel(frame2, text="$24,000", font=("Arial", 30), justify="left")
frame_label.pack(padx=10, pady=20, side="top")
amount_entry = ctk.CTkEntry(frame, placeholder_text="Amount", font=("Arial", 20))
amount_entry.pack(pady=20, padx=10, ipady=5, ipadx=5, fill="both",side="bottom")
 


frame = ctk.CTkFrame(master=window, width=200, height=60)
frame.pack(pady=5, padx= 30, fill="both")
deposit_button = ctk.CTkButton(frame, text="Deposit", font=("Arial", 20), width=100, height=50, hover_color="black", border_width=1, text_color="white")
deposit_button.pack(pady=10, padx=10, side="bottom", fill="both")


window.mainloop()