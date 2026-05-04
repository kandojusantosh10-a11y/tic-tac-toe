import tkinter as tk
from tkinter import messagebox

# Initialize window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x420")
root.config(bg="#1e1e2f")

# Variables
current_player = "X"
board = [""] * 9
buttons = []


def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False


def check_draw():
    return "" not in board


def on_click(index):
    global current_player

    if board[index] != "":
        return

    board[index] = current_player
    buttons[index].config(text=current_player)

    if check_winner(current_player):
        messagebox.showinfo("Game Over", f"🎉 Player {current_player} wins!")
        reset_game()
        return

    if check_draw():
        messagebox.showinfo("Game Over", "🤝 It's a Draw!")
        reset_game()
        return

    # Switch player
    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"Player {current_player}'s Turn")


def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    status_label.config(text="Player X's Turn")
    for btn in buttons:
        btn.config(text="")


# Title
title = tk.Label(root, text="Tic Tac Toe", font=("Arial", 18, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Player X's Turn", font=("Arial", 12),
                        bg="#1e1e2f", fg="#00ffcc")
status_label.pack(pady=5)

# Frame for grid
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

# Create buttons
for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 20, "bold"),
                    width=5, height=2, bg="#2d2d44", fg="white",
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Restart Button
restart_btn = tk.Button(root, text="Restart Game", font=("Arial", 12),
                        bg="#00adb5", fg="white", command=reset_game)
restart_btn.pack(pady=15)

# Run app
root.mainloop()