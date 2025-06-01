from tkinter import *
from PIL import Image, ImageTk

#List of questions
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
        "image": "mt-maunganui-the-mount-sunrise-tauranga-north-island-new-zealand.avif",
        "question": "What is this famous Aotearoa landmark?/He aha tēnei tāone rongonui o Aotearoa?",
        "options": ["Mount Aspiring / Tititea", "Tauranga Mount Maunganui", "Aoraki / Mount Cook", "Mount Tasman"],
        "answer": "Tauranga Mount Maunganu"
    },
    {
        "image": "WRT_01b_Wairakei-Huka-Falls-1-1024x576.webp",
        "question": "What is this famous Aotearoa landmark?/He aha tēnei tāone rongonui o Aotearoa?",
        "options": ["Bowen Falls", "Huka Falls", "Āniwaniwa Falls", "Victoria Falls"],
        "answer": "Huka Falls"
    },
    {
        "image": "R.jfif",
        "question": "What is this famous Aotearoa landmark?/He aha tēnei tāone rongonui o Aotearoa?",
        "options": ["Westland Tai Poutini National Park", "Piopiotahi Fiordland National park", "Whanganui National Park", "Arthur's Pass National Park"],
        "answer": "Piopiotahi Fiordland National park"
    },
    {
        "image": "OIP.jfif",
        "question": "What is this famous Aotearoa landmark?/He aha tēnei tāone rongonui o Aotearoa?",
        "options": ["Kawarau Bridge-Queenstown", "Waiohine Gorge Suspension Bridge", "Mangapohue Natural Bridge Walk", "Arapuni Swing Bridge"],
        "answer": "Kawarau Bridge-Queenstown"
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

#Scrollable interface
canvas = Canvas(root, bg="#d4f1f4")
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)

#Frame insdie the interface
frame = Frame(canvas, bg="#d4f1f4")
canvas.create_window((0,0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)




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

#pack canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

#Make sure scrolling works with content size
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

#Start app
root.mainloop()