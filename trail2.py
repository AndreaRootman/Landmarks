import tkinter as tk
from PIL import Image, ImageTk

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

#load and show image
try:
    img_path = "/mnt/data/866be6b0-a7eb-4388-4388-b9fe-a7d54412786d.png"
    image = Image.open(img_path)
    image = image.resize((400,120))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo, bg="#d4f1f9")
    image_label.image = photo

except Exception as e:
    image_label = tk.Label(root, text="[Image]", width=30, height=5, bg="lightgrey")
    image_Label.pack(pady=10)

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