
import tkinter
import subprocess

class MainWindow(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.centerWindow()
        self.setButtons()

    def centerWindow(self):
        self.w = 350
        self.h = 150
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()        
        x = (sw - self.w) / 2
        y = (sh - self.h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))
    
    def setButtons(self):
        self.pack(side="top", fill="both", expand=True)

        description_label = tkinter.Label(self, text="""
        This GUI allows to enable or disable HyperV feature on Windows.
        This may be especially useful to run VMWare (which requires to disable HyperV).
        """, wraplength=self.w)
        description_label.pack(side="top", fill="x", expand=False)

        enable_button = tkinter.Button(self, text="Enable", command=self.enable_hyperv)
        enable_button.pack(side="left", fill="x", expand=True)
        disable_button = tkinter.Button(self, text="Disable", command=self.disable_hyperv)
        disable_button.pack(side="right", fill="x", expand=True)

    def enable_hyperv(self):
        subprocess.call(["bcdedit", "/set", "hypervisorlaunchtype", "auto"])
        print("HyperV enabled")

    def disable_hyperv(self):
        subprocess.call(["bcdedit", "/set", "hypervisorlaunchtype", "off"])
        print("HyperV disabled")

def main():
    root = tkinter.Tk()
    root.wm_title("HyperV manager")
    mainWindow = MainWindow(root)
    mainWindow.mainloop()

if __name__ == "__main__":
    main()
