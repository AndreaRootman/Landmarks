import tkinter as tk

#Question data
question_text ="Question in English and Maori"
options = ["Multi question Englihs and Maori"]
correct_answer = "Answer"

#Function to check answer
def check_answer():
    selected = selected_option.get()
    if selected == correct_answer:
        feedback_label.config(text="Correct", fg="green")
    else:
        feedback_label.config(text=f"Incorrect, the answer is: {correct_answer}", fg="red")
#Create main window
root = tk.Tk()
root.title("Aotearoa Landmakrs")
root.geometry("400x450")
root.configure(bg="#d4f1f9")

#Title label
title_label = tk.Label(root, text="Aotearoa Landmarks", font=("Arial", 18, "bold"), bg="#d4f1f9")
title_label.pack(pady=15)

#Image placeholder
image_label = tk.Label(root, text="[Image goes here]", width=30, height=5, bg="lightgrey")
image_label.pack(pady=10)

#Question
question_label = tk.Label(root, text=question_text, font=("Arial", 12), wraplength=350, bg="#d4f1f9")
question_label.pack(pady=10)

#options
selected_option = tk.StringVar()
for option in options:
    tk.Radiobutton(root, text=option, variable=selected_option, value=option, bg="#d4f1f9").pack(anchor="w", padx=40)

#Submit button
submit_button = tk.Button(root, text="Check Answer", command=check_answer)
submit_button.pack(pady=15)

#Feedback
feedback_label = tk.Label(root, text="", font=("Arial", 12), bg="#d4f1f9")
feedback_label.pack(pady=10)

#Start the app
root.mainloop()

