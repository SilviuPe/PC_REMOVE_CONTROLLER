import tkinter as tk
import os

from threading import Thread
from main import MainApp
from tkinter import scrolledtext, messagebox


DOCUMENT_PATH = "documentation.md"
app_thread = None
app = MainApp()

def run_client():
    try:
        global app_thread
        app_thread = Thread(target=app.start_server).start()
        messagebox.showinfo("Server", "Server is now running...")

    except Exception as error:
        print("Error occurred trying to start the server", str(error))

def show_documentation():
    if not os.path.exists(DOCUMENT_PATH):
        messagebox.showerror("Error", f"File not found: {DOCUMENT_PATH}")
        return

    with open(DOCUMENT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    doc_window = tk.Toplevel()
    doc_window.title("Documentation Viewer")
    doc_window.geometry("600x500")

    text_area = scrolledtext.ScrolledText(doc_window, wrap=tk.WORD)
    text_area.insert(tk.END, content)
    text_area.configure(state='disabled')
    text_area.pack(expand=True, fill='both')



def main():
    win = tk.Tk()
    win.title("Client App")
    win.geometry("300x150")

    def on_close():
        app.server.close()
        app.monitor.stop_listeners()
        win.destroy()

    win.protocol("WM_DELETE_WINDOW", on_close)

    tk.Button(win, text="Run Server", command=run_client, height=2, width=20).pack(pady=10)
    tk.Button(win, text="Show Documentation", command=show_documentation).pack()

    win.mainloop()

if __name__ == "__main__":
    main()
