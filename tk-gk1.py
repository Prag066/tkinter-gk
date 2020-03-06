import requests
from tkinter import *

api = requests.get('https://opentdb.com/api.php?amount=10&category=9&type=boolean')

json_data = api.json()
list_data = json_data['results']
# for q in list_data:
#     print(q['question'],q['correct_answer'])

window = Tk()
window.title('GK App')


app_title = "General GK"
app_msg = Message(window,text=app_title)
app_msg.config(bg='lightgreen')
app_msg.pack()

qus = ""
ans = ""
for q in list_data:
        qus = q['question']
        ans = q['correct_answer']
        qus_var = Message(window,text=qus)
        qus_ans = Message(window,text=ans)
        Message(window,text="")

        qus_var.config(bg='white')
        qus_ans.config(bg='red')

        qus_var.pack(side=LEFT)
        qus_ans.pack(side=LEFT)


window.minsize(500,300)
window.config(bg='black')
window.mainloop()