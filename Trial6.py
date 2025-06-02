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
root.geometry("900x700")
root.configure(bg="#d4f1f9")

# Frame for all questions
content_frame = tk.Frame(root, bg="#d4f1f9")
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Prepare a StringVar for each question
selected_vars = [tk.StringVar() for _ in questions]

# Render all questions in a grid
for idx, q in enumerate(questions):
    # Load image
    try:
        img = Image.open(q["image"])
        img = img.resize((250, 150))
        photo = ImageTk.PhotoImage(img)
        img_lbl = tk.Label(content_frame, image=photo, bg="#d4f1f9")
        img_lbl.image = photo
        img_lbl.grid(row=idx, column=0, padx=10, pady=10)
    except:
        tk.Label(content_frame, text="[Image Missing]", width=30, height=8, bg="grey")\
          .grid(row=idx, column=0, padx=10, pady=10)

    # Question + options
    q_frame = tk.Frame(content_frame, bg="#d4f1f9")
    q_frame.grid(row=idx, column=1, sticky="nw", padx=10, pady=10)

    tk.Label(
        q_frame,
        text=f"Q{idx+1}. {q['question']}",
        font=("Arial", 12, "bold"),
        wraplength=400,
        justify="left",
        bg="#d4f1f9"
    ).pack(anchor="w", pady=(0,10))

    for opt in q["options"]:
        tk.Radiobutton(
            q_frame,
            text=opt,
            variable=selected_vars[idx],
            value=opt,
            bg="#d4f1f9"
        ).pack(anchor="w", pady=2)

# Submit button
def submit_quiz():
    # Remove everything
    for widget in root.winfo_children():
        widget.destroy()
    show_end_screen()

submit_btn = tk.Button(root, text="Submit", font=("Arial", 12), command=submit_quiz)
submit_btn.pack(pady=20)

# End screen
def show_end_screen():
    root.configure(bg="lightgrey")
    end_frame = tk.Frame(root, bg="lightgrey")
    end_frame.pack(expand=True)

    tk.Label(
        end_frame,
        text="Congratulations!",
        font=("Arial", 20, "bold"),
        bg="lightgrey"
    ).pack(pady=20)

    tk.Label(
        end_frame,
        text="You have completed the quiz.",
        font=("Arial", 14),
        bg="lightgrey"
    ).pack(pady=10)

    tk.Button(
        end_frame,
        text="Play Again",
        font=("Arial", 12),
        command=restart_quiz
    ).pack(pady=20)

def restart_quiz():
    # Clear end screen
    for widget in root.winfo_children():
        widget.destroy()
    # Rebuild quiz interface
    root.configure(bg="#d4f1f9")
    content_frame.pack(fill="both", expand=True, padx=20, pady=20)
    # Re-render questions
    for idx, q in enumerate(questions):
        try:
            img = Image.open(q["image"])
            img = img.resize((250, 150))
            photo = ImageTk.PhotoImage(img)
            img_lbl = tk.Label(content_frame, image=photo, bg="#d4f1f9")
            img_lbl.image = photo
            img_lbl.grid(row=idx, column=0, padx=10, pady=10)
        except:
            tk.Label(content_frame, text="[Image Missing]", width=30, height=8, bg="grey")\
              .grid(row=idx, column=0, padx=10, pady=10)
        q_frame = tk.Frame(content_frame, bg="#d4f1f9")
        q_frame.grid(row=idx, column=1, sticky="nw", padx=10, pady=10)
        tk.Label(
            q_frame,
            text=f"Q{idx+1}. {q['question']}",
            font=("Arial", 12, "bold"),
            wraplength=400,
            justify="left",
            bg="#d4f1f9"
        ).pack(anchor="w", pady=(0,10))
        for opt in q["options"]:
            tk.Radiobutton(
                q_frame,
                text=opt,
                variable=selected_vars[idx],
                value=opt,
                bg="#d4f1f9"
            ).pack(anchor="w", pady=2)
    submit_btn.pack(pady=20)

root.mainloop()
