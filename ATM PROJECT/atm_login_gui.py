import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.geometry("500x500")
window.resizable(width=False, height=False)
window.title("LUX BANK")
window.configure(bg="#fff")


whole_frame = tk.Frame(window, bg="#333", width=500, height=500)
whole_frame.pack(fill="both", expand=True)

def log_in():

    username = "berndtgwapo"
    password = "123456"

    if atm_username_entry.get()==username and atm_pass_entry.get()==password:
        messagebox.showinfo(title="LOG IN SUCCESSFUL", message="You have successfully logged in!")
    else:
        messagebox.showinfo(title="LOG IN INVALID", message="USERNAME AND PASSWORD DOESN'T EXIST!")

frame = tk.Frame(whole_frame, bg="#333")
frame.pack()


#gets user info
user_info_frame = tk.LabelFrame(frame, text="LUX BANK", font=("monospace", 30), bg="#333", fg="#fff")
user_info_frame.grid(row=0, column=0, padx=20, pady=100, columnspan=2)

#creating widgets
#user name
atm_username = tk.Label(user_info_frame, text="USERNAME:", bg="#333", fg="#fff", font=("Monospace", 10))
atm_username_entry = tk.Entry(user_info_frame)

#password
atm_pass = tk.Label(user_info_frame, text="PASSWORD:", bg="#333", fg="#fff", font=("Monospace", 10))
atm_pass_entry = tk.Entry(user_info_frame, show="*")

#widget placement
atm_username.grid(row=0, column=0, padx=10, pady=10)
atm_username_entry.grid(row=0, column=1, pady=10, padx=10)
atm_pass.grid(row=1, column=0, padx=10, pady=10)
atm_pass_entry.grid(row=1,column=1, padx=10, pady=10)


#button
atm_login_button = tk.Button(frame, text="LOG IN", bg="#333", fg="#fff", font=("Monospace0", 12), command=log_in)
atm_login_button.grid(row=1, column=0, padx=20, pady=10, sticky="news", columnspan=2)


window.mainloop()