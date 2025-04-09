import tkinter as tk
from tkinter import messagebox

import udpclient
from udpserver import UDPServer

#Handles all the code that is run when the change UDP address button is pressed
#DOES NOT handle displaying the button to the screen
class UDPButton:

    #default constructor, get root from display
    def __init__(self, root):
        self.root = root

        #creating instance for the udp server to work.
        self.udp_server = UDPServer()

    #udp port functions

    def change_udp_client_inter(self):
        self.change_udp_client()

    def change_udp_client(self):
        self.udp_server_popup()

    def udp_server_popup(self):
        udp_ip_address = "None"

        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Change UDP Server")
        popup.geometry("400x200")  # Set window size

        # Center the popup window
        popup.update_idletasks()  # Ensure the window size is calculated before positioning
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        window_width = 400
        window_height = 200

        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Label for the UDP server IP input
        tk.Label(popup, text="Enter new UDP Server IP \nExample: 192.168.1.100", font=("Arial", 12)).pack(pady=10)

        # Entry field for UDP server IP 
        udp_ip_address_var = tk.StringVar()
        udp_ip_address_entry = tk.Entry(popup, textvariable=udp_ip_address_var, font=("Arial", 12))
        udp_ip_address_entry.pack(pady=5)

        # Function to handle submission
        def submit_udp_server():
            nonlocal udp_ip_address
            udp_ip_address = udp_ip_address_var.get()
            try:
                udpclient.set_udp_config(udp_ip_address)
                #updating server along with client.
                self.udp_server.update_and_restart_server(udp_ip_address)
            except ValueError:
                messagebox.showerror(title="Error", message="Invalid address number! Please re-enter a valid integer.")
                udp_ip_address = "None"
            popup.destroy()  # Close the popup

        # Submit button
        submit_button = tk.Button(popup, text="Submit", command=submit_udp_server, font=("Arial", 12))
        submit_button.pack(pady=10)

        # Keep the popup focused until closed
        popup.transient(self.root)  # Make it modal (disable interaction with main window)
        popup.grab_set()
        self.root.wait_window(popup)

        return udp_ip_address

    def udp_error_popup(self, message):
        messagebox.showerror(title="Error", message=message)