import tkinter as tk
from run_button import run_forward, get_result


def frame():
    # Tkinterウィンドウを作成
    window = tk.Tk()
    window.geometry("400x300")

    # フレームを作成
    frame = tk.Frame(window, width=400, height=300, bg="white")
    frame.pack()

    # フレームにウィジェットを追加
    label = tk.Label(frame, text="時間を計測")
    label.pack()
    # 各種ウィジェットの作成
    start_time = tk.DoubleVar() #変数を作成
    start_time.set(-1)
    finish_time = tk.DoubleVar()
    finish_time.set(-1)
    start_button = tk.Button(frame, text="開始", command=lambda: run_forward(start_time))
    start_button.pack()
    finish_button = tk.Button(frame, text="終了", command=lambda: run_forward(finish_time))
    finish_button.pack()
    result_button = tk.Button(frame, text="時間を確認", command=lambda: get_result(start_time, finish_time))
    result_button.pack()
    # Tkinterウィンドウを開始
    window.mainloop()
    window.after(1000, check_condition(start_time, finish_button))


def check_condition(time, button):
    if time.get()<0:
        button.config(state="disabled")
    else:
        button.config(state="normal")
