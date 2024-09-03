from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
    ping = str(round(sp.results.ping, 2)) + " ms"
    
    lab_down.config(text=down)
    lab_up.config(text=up)
    lab_ping.config(text=ping)

# Initialize Tkinter window
sp = Tk()
sp.title("Internet Speed Tester")
sp.geometry("600x700")
sp.config(bg="#87CEEB")  # Set background to light blue

# Title label
lab_title = Label(sp, text="Internet Speed Test", font=("Arial", 30, "bold"), bg="#87CEEB", fg="#FF4500")
lab_title.place(x=100, y=30, height=50, width=400)

# Ping speed label
lab_ping_text = Label(sp, text="Ping", font=("Arial", 20, "bold"), bg="#87CEEB")
lab_ping_text.place(x=100, y=120, height=50, width=150)

lab_ping = Label(sp, text="0 ms", font=("Arial", 20), bg="#FFFFFF", relief="solid")
lab_ping.place(x=300, y=120, height=50, width=200)

# Download speed label
lab_down_text = Label(sp, text="Download Speed", font=("Arial", 20, "bold"), bg="#87CEEB")
lab_down_text.place(x=100, y=200, height=50, width=250)

lab_down = Label(sp, text="0 Mbps", font=("Arial", 20), bg="#FFFFFF", relief="solid")
lab_down.place(x=300, y=200, height=50, width=200)

# Upload speed label
lab_up_text = Label(sp, text="Upload Speed", font=("Arial", 20, "bold"), bg="#87CEEB")
lab_up_text.place(x=100, y=280, height=50, width=250)

lab_up = Label(sp, text="0 Mbps", font=("Arial", 20), bg="#FFFFFF", relief="solid")
lab_up.place(x=300, y=280, height=50, width=200)

# Button to trigger speed check
button = Button(sp, text="Check Speed", font=("Arial", 20, "bold"), bg="#32CD32", fg="#FFFFFF", command=speedcheck)
button.place(x=150, y=400, height=60, width=300)

# Start Tkinter main loop
sp.mainloop()
