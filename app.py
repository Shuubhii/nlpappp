from tkinter import *
from tkinter import messagebox
from mydb import *
from myapi import *
class NLPApp :

    def __init__(self):
        #database ka object
        self.dbo= Database()

        #myapi object
        self.apio=API()

        #login ka gui
        self.root= Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x700')
        self.root.configure(bg='#7956A8')
        self.login()
        self.root.mainloop()


    def login(self):
        self.clear()

        heading= Label(self.root, text='NLPApp', bg='#7956A8')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',28,'bold','italic'))

        #email enter karo
        label1=Label(self.root,text="Enter Email:", bg="#7956A8")
        label1.pack(pady=(30,5),anchor='w')
        label1.configure(font=('verdana',15))
        #label1.configure(justify=["right"])  only works in case of multiple lines in a label
        self.email_input = Entry(self.root, width=56)
        self.email_input.pack(pady=(5,10),ipady=4)

        #pass enter karo
        label2=Label(self.root, text="Password: ", bg="#7956A8")
        label2.pack(pady=(10,5),anchor='w')
        label2.configure(font=('verdana', 15))
        self.pass_input=Entry(self.root, width=56,show='*')
        self.pass_input.pack(pady=(5, 10), ipady=4)

        #button banao
        btn1= Button(self.root, text='Login', width=30, height=2, command=self.perform_login)
        btn1.configure(bg=('#432F5F'),fg='white',font=(15))
        btn1.pack(pady=(10,10))

        #regist ke liye label
        label2= Label(self.root,text='Not registered?',anchor='e')
        label2.pack(pady=(10,10),anchor='e')
        label2.configure(font=('verdana',9,'underline'),bg='#7956A8',anchor='e')

        # button banao
        btn2=Button(self.root, text='Register Now', width=15, height=1,command=self.register)
        btn2.configure(bg=('#432F5F'), fg='white')
        btn2.pack(pady=(5, 10),padx=(20,5),anchor='e')

    def register(self):
        #clear karo gui ko
        self.clear()

        heading=Label(self.root, text='NLPApp', bg='#7956A8')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 28, 'bold', 'italic'))

        # email enter karo
        label1=Label(self.root, text="Enter Email:", bg="#7956A8")
        label1.pack(pady=(30, 5), anchor='w')
        label1.configure(font=('verdana', 15))
        # label1.configure(justify=["right"])  only works in case of multiple lines in a label
        self.email1_input=Entry(self.root, width=56)
        self.email1_input.pack(pady=(5, 10), ipady=4)

        # name enter karo
        label3=Label(self.root, text="Enter Name:", bg="#7956A8")
        label3.pack(pady=(30, 5), anchor='w')
        label3.configure(font=('verdana', 15))
        self.name_input=Entry(self.root, width=56)
        self.name_input.pack(pady=(5, 10), ipady=4)

        # pass enter karo
        label2=Label(self.root, text="Password: ", bg="#7956A8")
        label2.pack(pady=(10, 5), anchor='w')
        label2.configure(font=('verdana', 15))
        self.pass1_input=Entry(self.root, width=56, show='*')
        self.pass1_input.pack(pady=(5, 10), ipady=4)

        # button banao
        btn1=Button(self.root, text='Register', width=30, height=2,command=self.perform_register)
        btn1.configure(bg=('#432F5F'), fg='white', font=(15))
        btn1.pack(pady=(30, 10))

        # login ke liye label
        label2=Label(self.root, text='Already a member?', anchor='e')
        label2.pack(pady=(10, 10), anchor='e')
        label2.configure(font=('verdana', 9, 'underline'), bg='#7956A8', anchor='e')

        # button banao
        btn2=Button(self.root, text='Login Now', width=15, height=1,command=self.login)
        btn2.configure(bg=('#432F5F'), fg='white')
        btn2.pack(pady=(5, 10), padx=(20, 5), anchor='e')

    def perform_register(self):
        name = self.name_input.get()
        email=self.email1_input.get()
        password=self.pass1_input.get()
        res=self.dbo.add_data(name,email,password)
        if res:
            messagebox.showinfo('Success','reg successful. Login Now')
        else:
            messagebox.showerror('Error','User already exists.')


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_login(self):
        email=self.email_input.get()
        password=self.pass_input.get()
        res=self.dbo.search(email,password)
        if res:
            messagebox.showinfo('success','Login successful')
            self.home()
        else:
            messagebox.showerror('error','wrong email or password. Enter correct details')

    def home(self):
        # clear karo gui ko
        self.clear()

        heading=Label(self.root, text='NLPApp', bg='#7956A8')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 28, 'bold', 'italic'))

        # options show karo
        #option 1
        btn1=Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment)
        btn1.configure(bg=('#B2ACBB'), fg='black', font=(15))
        btn1.pack(pady=(30, 10),padx=(5,5))

        #option 2
        btn1=Button(self.root, text='Named entity Relation', width=30, height=4, command=self.ner)
        btn1.configure(bg=('#B2ACBB'), fg='black', font=(15))
        btn1.pack(pady=(30, 10),padx=(5,5))

        #option 3
        btn1=Button(self.root, text='Emotion Prediction', width=30, height=4, command=self.emotion)
        btn1.configure(bg=('#B2ACBB'), fg='black', font=(15))
        btn1.pack(pady=(30, 10),padx=(5,5))

    def ner(self):
        self.clear()

        heading=Label(self.root, text='Named Entity Relation', bg='#7956A8')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 18,'italic'))

        #text analyse wala likho
        label1= Label(self.root,text="Enter Text",bg='#7956A8')
        label1.pack(pady=(10,5), anchor='w')
        label1.configure(font=('verdana',10,'bold'))

        self.ner_input= Entry(self.root,width=40)
        self.ner_input.pack(pady=(5,5),padx=(8,8),ipady=4)

        #analyse ka button
        btn1=Button(self.root,text="Analyse", bg='#B2ACBB')
        btn1.pack(pady=(5,5))

        #analysed text show karo
        label2=Label(self.root, text="", bg='#7956A8')
        label2.pack(pady=(10, 5), anchor='w')
        label2.configure(font=('verdana', 18, 'bold'))

        #bhago wapas
        btn1=Button(self.root, text="Go Back", bg='#B2ACBB', command=self.home)
        btn1.pack(pady=(5, 5))

    def sentiment(self):
        self.clear()

        heading=Label(self.root, text='Sentiment Analysis', bg='#7956A8')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 18,'italic'))

        #text analyse wala likho
        label1= Label(self.root,text="Enter Text",bg='#7956A8')
        label1.pack(pady=(10,5), anchor='w')
        label1.configure(font=('verdana',10,'bold'))

        self.sentiment_input= Entry(self.root,width=40)
        self.sentiment_input.pack(pady=(5,5),padx=(8,8),ipady=4)

        #analyse ka button
        btn1=Button(self.root,text="Analyse", bg='#B2ACBB', command=self.do_analyse_sentiment)
        btn1.pack(pady=(5,5))

        #analysed text show karo
        label2=Label(self.root, text="", bg='#7956A8')
        label2.pack(pady=(10, 5), anchor='w')
        label2.configure(font=('verdana', 18, 'bold'))

        #bhago wapas
        btn1=Button(self.root, text="Go Back", bg='#B2ACBB', command=self.home)
        btn1.pack(pady=(5, 5))

    def do_analyse_sentiment(self):
        txt=self.sentiment_input.get()
        response=apio.analyse(txt)
        print(response)


    def emotion(self):
        self.clear()

        heading=Label(self.root, text='Emotion Prediction', bg='#7956A8')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 18,'italic'))

        #text analyse wala likho
        label1= Label(self.root,text="Enter Text",bg='#7956A8')
        label1.pack(pady=(10,5), anchor='w')
        label1.configure(font=('verdana',10,'bold'))

        self.emotion_input= Entry(self.root,width=40, )
        self.emotion_input.pack(pady=(5,5),padx=(8,8),ipady=4)

        #analyse ka button
        btn1=Button(self.root,text="Analyse", bg='#B2ACBB')
        btn1.pack(pady=(5,5))

        #analysed text show karo
        label2=Label(self.root, text="", bg='#7956A8')
        label2.pack(pady=(10, 5), anchor='w')
        label2.configure(font=('verdana', 18, 'bold'))

        #bhago wapas
        btn1=Button(self.root, text="Go Back", bg='#B2ACBB', command=self.home)
        btn1.pack(pady=(5, 5))
nlp=NLPApp()