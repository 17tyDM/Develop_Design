import tkinter as tk
from tkinter import messagebox

def check_winner():
    # 勝者のチェック
    for a, b, c in win_conditions:
        if buttons[a]['text'] == buttons[b]['text'] == buttons[c]['text'] != "":
            messagebox.showinfo("勝者", f"{buttons[a]['text']}  Win!")
            reset_game()
            return

    if "" not in [button['text'] for button in buttons]:
        messagebox.showinfo("引き分け", "引き分けです！")
        reset_game()

def reset_game():
    # ゲームをリセット
    for button in buttons:
        button['text'] = ""
        button['state'] = 'active'

def button_click(idx):
    # ボタンがクリックされた時の処理
    if buttons[idx]['text'] == "":
        buttons[idx]['text'] = current_player
        buttons[idx]['state'] = 'disabled'
        check_winner()
        switch_player()

def switch_player():
    # プレイヤーの切り替え
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # 横
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # 縦
    (0, 4, 8), (2, 4, 6)              # 斜め
]

# GUIの設定
root = tk.Tk()
root.title("〇×ゲーム")

buttons = [tk.Button(root, text="", font=('Helvetica', 20), width=5, height=2, command=lambda idx=idx: button_click(idx)) for idx in range(9)]
for idx, button in enumerate(buttons):
    row = idx // 3
    col = idx % 3
    button.grid(row=row, column=col)

current_player = 'X'  # 最初はプレイヤーXから始める

root.mainloop()
