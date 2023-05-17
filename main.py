import random, tkinter as tk

root = tk.Tk()
root.title('Function Machine')
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]

def setup():
    global answerLabel,entryField
    root.geometry('325x100')
    answerLabel = tk.Label(root, text='Answer:', bg='grey51', anchor = "center")
    answerLabel.grid(row=0, column=0, columnspan=80, sticky='ew')
    entryField = tk.Entry(root, justify = 'center')
    entryField.grid(row=1, column=0, columnspan=80, sticky='ew')
    submitBtn = tk.Button(root, text='Submit', command=submit)
    submitBtn.grid(row=2, column=0, columnspan=80, sticky='ew')

roc = random.randint(1,5)

def submit():
    global inputint, roc, l1, l2, l3, l4, l5
    try:
        inputint = int(entryField.get())
    except:
        answerLabel.config(text='Error: Please enter a number')
        submit()
    generate_numbers()
    answerLabel.config(text='Answer: '+str(l1)+' '+str(l2)+' '+str(l3)+' '+str(l4)+' '+str(l5))
    

def generate_numbers():
  global inputint, roc, l1, l2, l3, l4, l5
  try:
    mutation()
    l1 = [0,inputint]
    l2 = [l1[0]+roc,l1[1]+roc]
    l3 = [l2[0]+roc,l2[1]+roc]
    l4 = [l3[0]+roc,l3[1]+roc]
    l5 = [l4[0]+roc,l4[1]+roc]
  except:
    answerLabel.config(text='Error: Please try again')
    generate_numbers()
     
def mutation():
  global change,choosen
  mutation = random.randint(1,100)
  if mutation == 1 or mutation == 2:
    change = random.randint(-3,3)
    choosen = random.randint(1,5)
    applyMutation()

def applyMutation():
    if choosen == 1:
        randCord = random.randint(1,2)
        if randCord == 1:
             l1[0] += change
        elif randCord == 2:
            l1[1] += change
    elif choosen == 2:
        randCord = random.randint(1,2)
        if randCord == 1:
            l2[0] += change
        elif randCord == 2:
            l2[1] += change
    elif choosen == 3:
        randCord = random.randint(1,2)
        if randCord == 1:
            l3[0] += change
        elif randCord == 2:
            l3[1] += change
    elif choosen == 4:
        randCord = random.randint(1,2)
        if randCord == 1:
            l4[0] += change
        elif randCord == 2:
            l4[1] += change
    elif choosen == 5:
        randCord = random.randint(1,2)
        if randCord == 1:
            l5[0] += change
        elif randCord == 2:
            l5[1] += change

try:
  setup()
except:
  setup()
root.mainloop()