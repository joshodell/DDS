import tkinter as tk
import tkinter.messagebox
import socket
import webbrowser
import subprocess
import ctypes, sys
from shutil import copyfile
import shutil
import os

CREATE_NO_WINDOW = 0x08000000
# Hides console window of functions


def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def support_portal():
    webbrowser.open('http://www.ddssupportgroup.com', new=2)
    return()


def submit_ticket():
    webbrowser.open('http://www.oksupportgroup.com', new=2)
    return()


def show_ip():
    ip = socket.gethostbyname(socket.gethostname())
    tkinter.messagebox.showinfo("IP", "Your IP address is: %s" % ip)
    return()


def enable_ra():
    if not os.path.exists('C:/DDSTEMP'):
        os.mkdir('C:/DDSTEMP')
    copyfile(resource_path('ra-check1.txt'), 'C:/DDSTEMP/ra-check1.txt')
    copyfile(resource_path('ra-check2.txt'), 'C:/DDSTEMP/ra-check2.txt')
    subprocess.run('netsh advfirewall set allprofiles state off', stdout=open('C:/DDSTEMP/ra-check1.txt', 'w'),
                   stderr=subprocess.STDOUT, stdin=subprocess.PIPE, encoding='utf-8', bufsize=4096,
                   creationflags=CREATE_NO_WINDOW)
    subprocess.run('reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v '
                   'fDenyTSConnections /t REG_DWORD /d 0 /f', stdout=open('C:/DDSTEMP/ra-check2.txt', 'w'),
                   stderr=subprocess.STDOUT, stdin=subprocess.PIPE, encoding='utf-8', bufsize=4096,
                   creationflags=CREATE_NO_WINDOW)
    if "Ok." in open('C:/DDSTEMP/ra-check1.txt').read() and "The operation completed successfully." in \
            open('C:/DDSTEMP/ra-check2.txt').read():
        shutil.rmtree('C:/DDSTEMP')
        tkinter.messagebox.showinfo("Enable Remote Access", "Successfully Enabled Remote Access")
    elif "Ok." in open('C:/DDSTEMP/ra-check1.txt').read() and "The operation completed successfully." not in \
            open('C:/DDSTEMP/ra-check2.txt').read():
        shutil.rmtree('C:/DDSTEMP')
        tkinter.messagebox.showerror("Enable Remote Access", "Disabled Firewall, but could not enable RDP")
    elif "Ok." not in open('C:/DDSTEMP/ra-check1.txt').read() and "The operation completed successfully." in \
            open('C:/DDSTEMP/ra-check2.txt').read():
        shutil.rmtree('C:/DDSTEMP')
        tkinter.messagebox.showerror("Enable Remote Access", "RDP Enabled but could not disable Firewall")
    elif "Ok." not in open('C:/DDSTEMP/ra-check1.txt').read() and "The operation completed successfully." not in \
            open('C:/DDSTEMP/ra-check2.txt').read():
        shutil.rmtree('C:/DDSTEMP')
        tkinter.messagebox.showerror("Enable Remote Access", "Could not disable Firewall or enable RDP")
    return()


def connect_wifi():
    if not os.path.exists('C:/DDSTEMP'):
        os.mkdir('C:/DDSTEMP')
    copyfile(resource_path('5qWKP09xSNPdW8pfFHLa.xml'), 'C:/DDSTEMP/5qWKP09xSNPdW8pfFHLa.xml')
    copyfile(resource_path('wifi.txt'), 'C:/DDSTEMP/wifi.txt')
    subprocess.run('Netsh WLAN delete profile name="5qWKP09xSNPdW8pfFHLa"', creationflags=CREATE_NO_WINDOW)
    subprocess.run('Netsh wlan add profile user=all '
                   'filename="C:/DDSTEMP/5qWKP09xSNPdW8pfFHLa.xml"', creationflags=CREATE_NO_WINDOW)
    subprocess.run('netsh wlan connect name="5qWKP09xSNPdW8pfFHLa"', stdout=open('C:/DDSTEMP/wifi.txt', 'w'),
                   stderr=subprocess.STDOUT, stdin=subprocess.PIPE, encoding='utf-8', bufsize=4096,
                   creationflags=CREATE_NO_WINDOW)
    if "Connection request was completed successfully" in open('C:/DDSTEMP/wifi.txt').read():
        shutil.rmtree('C:/DDSTEMP')
        tkinter.messagebox.showinfo("WiFi", "Successfully connected to WiFi!")
    else:
        tkinter.messagebox.showerror("WiFi", "Unable to connect to WiFi!")
    return()


def is_admin():
    # Finds out the script is running as admin
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return()

def join_domain():
    window = tk.Toplevel(root)
    window.iconbitmap(icon_path)

    w = 250
    h = 90
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    computernamelabel = tk.Label(window, text="Computer Name:")
    computername = tk.Entry(window)
    JoinButton = tk.Button(window, text="Join", width=15)

    computernamelabel.grid(column=0, row=0, padx=5, pady=10)
    computername.grid(column=1, row=0, padx=5, pady=10)
    JoinButton.grid(column=0, row=1, columnspan=2, padx=10, pady=5)


    window.mainloop()
    return()


if is_admin():

    # Runs the script if running as admin

    root = tk.Tk()

    root.resizable(False, False)
    root.title("IT Support")
    icon_path = resource_path("icon.ico")
    root.iconbitmap(icon_path)

    w = 325  # width for the Tk root
    h = 235  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    SupportPortalButton = tk.Button(root, text="DDS Portal", width=20, command=support_portal)
    TicketButton = tk.Button(root, text="Submit A Ticket", width=20, command=submit_ticket)
    IPButton = tk.Button(root, text="Find My IP", width=20, command=show_ip)
    RAButton = tk.Button(root, text="Enable Remote Access", width=20, command=enable_ra)
    WiFiButton = tk.Button(root, text="Connect To WiFi", width=20, command=connect_wifi)
    DomainButton = tk.Button(root, text="Join Domain", width =20, command=join_domain)
    logo_path = resource_path("dds-logo3.png")
    logo = tk.PhotoImage(file=logo_path)
    LogoWidget = tk.Label(root, image=logo)

    SupportPortalButton.grid(column=0, row=0, padx=5, pady=5)
    TicketButton.grid(column=1, row=0, padx=5, pady=5)
    IPButton.grid(column=0, row=1, padx=5, pady=5)
    RAButton.grid(column=1, row=1, padx=5, pady=5)
    WiFiButton.grid(column=0, row=2, padx=5, pady=5)
    DomainButton.grid(column=1, row=2, padx=5, pady=5)
    LogoWidget.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

    root.mainloop()

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    # Restarts the script if not running as admin

