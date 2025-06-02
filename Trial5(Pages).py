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

# Function to check answers
def check_answer(index_num, chosen_option, feedback_label):
    correct = questions[index_num]["answer"]
    if chosen_option.get() == correct:
        feedback_label.config(text=" Tika! Correct", fg="green")
    else:
        feedback_label.config(text=f" Hē! Correct: {correct}", fg="red")

#Create window
root = tk.Tk()
root.title("Aotearoa Landmarks Quiz")
root.geometry("1000x1600")
root.configure(bg="#d4f1f9")

# Title
tk.Label(root, text="Aotearoa Landmarks Quiz", font=("Arial", 22, "bold"), bg="#d4f1f9").grid(row=0, column=0, columnspan=2, pady=20)

# Rendering questions
question_number = 1
row_index = 1

for question_info in questions:
    # Try load image
    try:
        img_opened = Image.open(question_info["image"])
        img_resized = img_opened.resize((300, 180))
        img_display = ImageTk.PhotoImage(img_resized)
        image_label = tk.Label(root, image=img_display, bg="#d4f1f9")
        image_label.image = img_display
        image_label.grid(row=row_index, column=0, padx=20, pady=10)
    except:
        tk.Label(root, text="[Image Missing]", width=40, height=10, bg="grey").grid(row=row_index, column=0, padx=20, pady=10)

    # Question and options on the right
    content_frame = tk.Frame(root, bg="#d4f1f9")
    content_frame.grid(row=row_index, column=1, sticky="w")

    tk.Label(content_frame, text=f"Q{question_number}. {question_info['question']}", font=("Arial", 12, "bold"),
             wraplength=400, justify="left", bg="#d4f1f9").pack(anchor="w", pady=5)

    chosen = tk.StringVar()
    for option_text in question_info["options"]:
        tk.Radiobutton(content_frame, text=option_text, variable=chosen, value=option_text,
                       bg="#d4f1f9").pack(anchor="w", padx=10)

    result_label = tk.Label(content_frame, text="", font=("Arial", 11), bg="#d4f1f9")
    result_label.pack(pady=5)

    tk.Button(content_frame, text="Check Answer",
              command=lambda index=question_number - 1, selected=chosen, label=result_label:
              check_answer(index, selected, label)).pack()

    # Move to next row
    row_index += 1
    question_number += 1

# Start app
root.mainloop()
