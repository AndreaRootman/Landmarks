from tkinter import *
from PIL import Image, ImageTk

#List of questions
questions = [
    {
        "image": "pinnacleswellington.jpg",
        "question": "What is this famous landmark?",
        "options": ["Options1", "Options2", "Option3", "Option4"],
        "answer": "Answer"
    },
    {
        "image": "rotorua-geysers-te-puia-3.jpg",
        "question": "What is this famous landmark?",
        "options": ["Options1", "Options2", "Option3", "Option4"],
        "answer": "Answer"
    },
    {
        "image": "R.jfif",
        "question": "What is this famous landmark?",
        "options": ["Options1", "Options2", "Option3", "Option4"],
        "answer": "Answer"
    }
]

#Create window
root = Tk()
root.title("Aotearoa Landmarks")
root.geometry("600x1200")
root.configure(bg="#d4f1f9")

#Title
Label(root, text="Aotearoa Landmarks", font=("Arial", 22, "bold"), bg="#d4f1f9").pack(pady=15)

#Function to check answers
def check_answer(selected_option, answer, feedback_label):
    if selected_option.get() == answer:
        feedback_label.config(text="Tika!  Correct!", fg="green")
    else:
        feedback_label.config(text=f"He!  Incorrect, the correct answer: {answer}", fg="red")

#Render each question
for question in questions:
    try:
        img = Image.open(question["image"])
        img = img.resize((500, 250))
        photo = ImageTk.PhotoImage(img)
        img_label = Label(root, image=photo, bg="#d4f1f9")
        img_label.image = photo #Keep reference
        img_label.pack(pady=10)
    except:
        Label(root, text="[Image missing]", width=60, height=10, bg="grey").pack(pady=10)

    # Question text
    Label(root, text=question["question"], font=("Arial", 13, "bold"), wraplength=550, bg="#d4f1f9").pack(pady=5)

    # Options
    selected_option = StringVar()
    for option in question["options"]:
        Radiobutton(root, text=option, variable=selected_option, value=option, bg="#d4f1f9").pack(anchor="w", padx=40)

    # feedback label
    feedback = Label(root, text="", font=("Arial", 13, "bold"), wraplength=550, bg="#d4f1f9")
    feedback.pack(pady=5)

    # check answer button
    Button(root, text="Check Answer", command=lambda so=selected_option, ans=question["answer"], fl=feedback: check_answer(so, ans, fl)).pack(pady=10)



#Start app
root.mainloop()












