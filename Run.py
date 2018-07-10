import tkinter as tk
import tkinter.messagebox
import socket
import webbrowser
import subprocess
import ctypes
import sys
from shutil import copyfile
import shutil
import os

CREATE_NO_WINDOW = 0x08000000


# Hides console window of functions


def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class MainWindow():
    # Runs the script if running as admin
    def __init__(self, master):

        self.master = master
        self.master.resizable(False, False)
        self.master.title("IT Support")
        icon_path = resource_path("icon.ico")
        self.master.iconbitmap(icon_path)

        w = 325
        h = 235
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.SupportPortalButton = tk.Button(root, text="DDS Portal", width=20, command=MainWindow.support_portal)
        self.TicketButton = tk.Button(root, text="Submit A Ticket", width=20, command=MainWindow.submit_ticket)
        self.IPButton = tk.Button(root, text="Find My IP", width=20, command=self.show_ip)
        self.RAButton = tk.Button(root, text="Enable Remote Access", width=20, command=self.enable_ra)
        self.WiFiButton = tk.Button(root, text="Connect To WiFi", width=20, command=self.connect_wifi)
        self.DomainButton = tk.Button(root, text="Join Domain", width=20, command=self.domain_window)
        self.logo_path = resource_path("dds-logo3.png")
        self.logo = tk.PhotoImage(file=self.logo_path)
        self.LogoWidget = tk.Label(root, image=self.logo)

        self.SupportPortalButton.grid(column=0, row=0, padx=5, pady=5)
        self.TicketButton.grid(column=1, row=0, padx=5, pady=5)
        self.IPButton.grid(column=0, row=1, padx=5, pady=5)
        self.RAButton.grid(column=1, row=1, padx=5, pady=5)
        self.WiFiButton.grid(column=0, row=2, padx=5, pady=5)
        self.DomainButton.grid(column=1, row=2, padx=5, pady=5)
        self.LogoWidget.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

    def support_portal():
        webbrowser.open('http://www.ddssupportgroup.com', new=2)

    def submit_ticket():
        webbrowser.open('http://www.oksupportgroup.com', new=2)

    def show_ip():
        ip = socket.gethostbyname(socket.gethostname())
        tkinter.messagebox.showinfo("IP", "Your IP address is: %s" % ip)

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

    def domain_window(self):
        self.DWindow = tk.Toplevel(self.master)
        self.GUI = DomainWindow(self.DWindow)


class DomainWindow:
    CN = ' '
    UN = ' '
    PW = ' '

    def __init__(self,master):
        self.master = master
        icon_path = resource_path("icon.ico")
        self.master.iconbitmap(icon_path)

        w = 250
        h = 135
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.computernamelabel = tk.Label(self.master, text="Computer Name:")
        self.computernameentry = tk.Entry(self.master)
        self.usernamelabel = tk.Label(self.master, text="Domain User:")
        self.usernameentry = tk.Entry(self.master)
        self.passwordlabel = tk.Label(self.master, text="Domain Pass:")
        self.passwordentry = tk.Entry(self.master)
        self.joinbutton = tk.Button(self.master, text="Join", width=15)

        self.computernamelabel.grid(column=0, row=0, padx=5, pady=5)
        self.computernameentry.grid(column=1, row=0, padx=5, pady=5)
        self.usernamelabel.grid(column=0, row=1, padx=5, pady=5)
        self.usernameentry.grid(column=1, row=1, padx=5, pady=5)
        self.passwordlabel.grid(column=0, row=2, padx=5, pady=5)
        self.passwordentry.grid(column=1, row=2, padx=5, pady=5)
        self.joinbutton.grid(column=0, row=3, columnspan=2, padx=5, pady=5)


def is_admin():
    # Finds out the script is running as admin
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return ()


if is_admin():
    root = tk.Tk()
    GUI = MainWindow(root)
    root.mainloop()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    # Restarts the script if not running as admin
