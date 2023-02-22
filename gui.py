import tkinter as tk


def frame():
    # Tkinterウィンドウを作成
    window = tk.Tk()
    window.geometry("400x300")

    # フレームを作成
    frame = tk.Frame(window, width=400, height=300, bg="white")
    frame.pack()

    # フレームにウィジェットを追加
    label = tk.Label(frame, text="Hello, World!")
    label.pack()

    # Tkinterウィンドウを開始
    window.mainloop()