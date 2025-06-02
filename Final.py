import tkinter as tk
from PIL import Image, ImageTk

# List of questions
questions = [
    {
        "image": "pinnacleswellington.jpg",
        "question": "What is this famous Aotearoa landmark?/He aha tēnei tāone rongonui o Aotearoa?",
        "options": ["Wellington Pinnacles/Pūtangirua Pinnacles", "Moeraki Boulders", "The Pinnacles Grampians", "Pinnacle Erosion"],
        "answer": "Wellington Pinnacles/Pūtangirua Pinnacles"
    },
    {
        "image": "rotorua-geysers-te-puia-3.jpg",
        "question": "What is this famous  Aotearoa landmark?/He aha tēnei tāone rongonui o Aotearoa?",
        "options": ["Lake Taupo", "Sky Tower Auckland", "Rotorua Geyser/Pōhutu Geyser", "Mount Rushmore/Maunga Rūhirehu"],
        "answer": "Rotorua Geyser/Pōhutu Geyser"
    },
    {
        "image": "WRT_01b_Wairakei-Huka-Falls-1-1024x576.webp",
        "question": "What is this famous Aotearoa landmark?/He aha tēnei tāone rongonui o Aotearoa?",
        "options": ["Bowen Falls", "Huka Falls", "Āniwaniwa Falls", "Victoria Falls"],
        "answer": "Huka Falls"
    }
]

# Create main window
root = tk.Tk()
root.title("Aotearoa Landmarks Quiz")
root.geometry("900x750")
root.configure(bg="#d4f1f9")

# Frame for all questions
content_frame = None


#Create/reset selection variables—one StringVar per question
def reset_selection_vars():
    return [tk.StringVar() for _ in questions]


selection_vars = reset_selection_vars()


# Draw the quiz grid
def draw_quiz():
    global content_frame
    # Clear old frame if it exists
    if content_frame is not None:
        content_frame.destroy()
    # Create a fresh frame
    content_frame = tk.Frame(root, bg="#d4f1f9")
    content_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Loop through questions and place image + options in a grid
    for question_index, question_item in enumerate(questions):
        # --- Image column ---
        try:
            img_obj = Image.open(question_item["image"])
            img_resized = img_obj.resize((250, 150))
            photo = ImageTk.PhotoImage(img_resized)
            img_label = tk.Label(content_frame, image=photo, bg="#d4f1f9")
            img_label.image = photo  # keep reference
            img_label.grid(row=question_index, column=0, padx=10, pady=10)
        except:
            tk.Label(content_frame,
                     text="[Image Missing]",
                     width=30,
                     height=8,
                     bg="grey"
                     ).grid(row=question_index, column=0, padx=10, pady=10)

        # --- Question & options column ---
        question_frame = tk.Frame(content_frame, bg="#d4f1f9")
        question_frame.grid(row=question_index, column=1, sticky="nw", padx=10, pady=10)

        # Question text
        tk.Label(
            question_frame,
            text=f"Q{question_index + 1}. {question_item['question']}",
            font=("Arial", 12, "bold"),
            wraplength=400,
            justify="left",
            bg="#d4f1f9"
        ).pack(anchor="w", pady=(0, 8))

        # Radio buttons for options
        for option_text in question_item["options"]:
            tk.Radiobutton(
                question_frame,
                text=option_text,
                variable=selection_vars[question_index],
                value=option_text,
                bg="#d4f1f9"
            ).pack(anchor="w", pady=2)


# When the user clicks Submit
def submit_quiz():
    # Calculate score
    total_correct = 0
    for idx, question_item in enumerate(questions):
        if selection_vars[idx].get() == question_item["answer"]:
            total_correct += 1

    # Clear the window and show end screen
    for widget in root.winfo_children():
        widget.destroy()
    # Show end screen
    show_end_screen(total_correct)


# End screen (congratulates and shows score)
def show_end_screen(user_score):
    root.configure(bg="lightgrey")
    end_frame = tk.Frame(root, bg="lightgrey")
    end_frame.pack(fill="both", expand=True, pady=50)

    tk.Label(
        end_frame,
        text="Congratulations!",
        font=("Arial", 20, "bold"),
        bg="lightgrey"
    ).pack(pady=20)

    tk.Label(
        end_frame,
        text=f"You have completed the quiz.\nYour score: {user_score} / {len(questions)}",
        font=("Arial", 14),
        bg="lightgrey"
    ).pack(pady=10)

    tk.Button(
        end_frame,
        text="Play Again",
        font=("Arial", 12),
        command=restart_quiz
    ).pack(pady=20)


# Restart quiz to take again
def restart_quiz():
    global selection_vars
    selection_vars = reset_selection_vars()
    # Clear window
    for widget in root.winfo_children():
        widget.destroy()
    # Restore background and quiz
    root.configure(bg="#d4f1f9")
    draw_quiz()
    submit_button.pack(pady=20)


# initial draw
draw_quiz()
submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=submit_quiz)
submit_button.pack(pady=20)

# start app
root.mainloop()
