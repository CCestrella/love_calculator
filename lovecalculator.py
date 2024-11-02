import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
from tkinter import font as tkfont

def calculate_love_score(name_1, name_2):
    """Calculate love score based on letter occurrences in 'TRUE' and 'LOVE'."""
    combined_names = name_1 + name_2
    true_score = sum(combined_names.lower().count(letter) for letter in "true")
    love_score = sum(combined_names.lower().count(letter) for letter in "love")
    total_score = int(f"{true_score}{love_score}")
    return true_score, love_score, total_score


def display_result():
    """Calculate and display the love score and corresponding message."""
    name_1 = entry_name_1.get().strip()
    name_2 = entry_name_2.get().strip()

    if not name_1 or not name_2:
        label_result.config(text="⚠️ Please enter both names!", fg="red")
        final_message_label.place_forget()
        return

    _, _, total_score = calculate_love_score(name_1, name_2)
    result_text = f"✨ Your True Love Score is: {total_score} ✨\n\n"
    label_result.config(fg="white")

    
    final_message_label.place_forget()

    
    if total_score > 80:
        result_text += "💘 You are a match made in heaven! 💘"
    elif 50 <= total_score <= 80:
        result_text += "💞 You have a strong connection! 💞"
    elif 30 <= total_score < 50:
        result_text += "💫 There's some potential here! 💫"
    else:
        final_message_label.config(text="😅 Maybe better as friends! 😅")
        final_message_label.place(x=label_result.winfo_x(), y=label_result.winfo_y() + 50)

    label_result.config(text=result_text)


root = tk.Tk()
root.title("Love Calculator 💖")
root.geometry("600x500")


background_image = Image.open("lovecalculator.png").resize((600, 500), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(background_image)
Label(root, image=bg_image).place(relwidth=1, relheight=1)


custom_font = tkfont.Font(family="Itim", size=12)


center_x = 120
start_y = 180


label_name_1 = tk.Label(root, text="Enter your name:", font=("Itim", 16), fg="white", bg="#800080")
label_name_1.place(x=center_x - 75, y=start_y)

entry_name_1 = tk.Entry(
    root, font=("Itim", 12), bg="#e9c4e1", relief="solid", bd=2,
    highlightthickness=2, highlightbackground="#8A2BE2", highlightcolor="#D173F3"
)
entry_name_1.place(x=center_x - 75, y=start_y + 30, width=150)

label_name_2 = tk.Label(root, text="Enter his/her name:", font=("Itim", 16), fg="white", bg="#800080")
label_name_2.place(x=center_x - 75, y=start_y + 80)

entry_name_2 = tk.Entry(
    root, font=("Itim", 12), bg="#e9c4e1", relief="solid", bd=2,
    highlightthickness=2, highlightbackground="#8A2BE2", highlightcolor="#D173F3"
)
entry_name_2.place(x=center_x - 75, y=start_y + 110, width=150)


button_calculate = tk.Button(
    root, text="Calculate Love Score ❤️", command=display_result, font=("Itim", 12),
    bg="#D173F3", relief="flat"
)
button_calculate.place(x=center_x - 75, y=start_y + 160)


label_result = tk.Label(
    root, text="", font=("Itim", 12), fg="white", justify="left", wraplength=150, bg="#800080"
)
label_result.place(x=center_x - 75, y=start_y + 210)


final_message_label = tk.Label(
    root, text="", font=("Itim", 15), fg="#F1F6E1", bg="#800080", justify="left", wraplength=180
)

root.mainloop()
