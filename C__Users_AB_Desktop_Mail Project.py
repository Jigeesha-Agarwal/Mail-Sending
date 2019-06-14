import os
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from tkinter import *
from tkinter.filedialog import askopenfilename

#mail sending function
def pri():
    from1=tf1.get()
    to=tf4.get()
    password=tf2.get()
    subject=tf3.get()
    message=t1.get("1.0","end-1c")
    #msg=MIMEMultipart()
    msg["from"]=from1
    msg["to"]=to
    msg["subject"]=subject
    msg.attach(MIMEText(message,'plain'))

    #portion to attach file from inside
    '''filename="11.txt"
    attachment=open(filename,"rb")
    part=MIMEBase("application","octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("content-disposition","attachment; filename="+filename)
    msg.attach(part)'''


    text=msg.as_string()
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(from1,password)
    s.sendmail(from1,to,text)
    s.quit()
    time.sleep(1)



#clear finction
def clearall():
    tf1.set("")
    tf2.set("")
    tf3.set("")
    tf4.set("")
    tf5.set("")
    t1.delete("1.0","end-1c")



#attach file function
def attach():
    '''img=askopenfilename()
    img_data=open(img,"rb").read()
    image=MIMEImage(img_data,name=os.path.basename(img))
    #msg=MIMEMultipart()
    msg.attach(image)'''
    file=askopenfilename()
    attachment=open(file,"rb")
    part=MIMEBase("application","octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("content-disposition","attachment; filename="+file)
    msg.attach(part)
    tf5.set(file)


ob=Tk()
tf1=StringVar()
tf2=StringVar()
tf3=StringVar()
tf4=StringVar()
tf5=StringVar()
ob.title("Sending Email GUI")
#win.geometry("600x500")


win=Frame(ob,relief="raised")
win.grid()

msg=MIMEMultipart()

l1=Label(win,text="From:",font=("arial",20),fg="steel blue")
l1.grid(row=0,column=0,sticky=E)
e1=Entry(win,textvariable=tf1,font=("arial",20),bd=3,width=45,bg="bisque2")
e1.grid(row=0,column=1)

#l2=Label(win,text="                                        ")
#l2.grid(row=1,column=0)

l3=Label(win,text="Password:",font=("arial",20),fg="steel blue")
l3.grid(row=1,column=0,sticky=E)
e2=Entry(win,textvariable=tf2,font=("arial",20),bd=3,width=45,show="*",bg="bisque2")
e2.grid(row=1,column=1)

l4=Label(win,text="To:",font=("arial",20),fg="steel blue")
l4.grid(row=2,column=0,sticky=E)
e4=Entry(win,textvariable=tf4,font=("arial",20),bd=3,width=45,bg="bisque2")
e4.grid(row=2,column=1)

l5=Label(win,text="                                        ")
l5.grid(row=3,column=0)

l6=Label(win,text="Subject:",font=("arial",20),fg="steel blue")
l6.grid(row=4,column=0,sticky=E)
e3=Entry(win,textvariable=tf3,font=("arial",20),bd=3,width=45,bg="bisque2")
e3.grid(row=4,column=1)

l7=Label(win,text="                                        ")
l7.grid(row=5,column=0)

l8=Label(win,text="Message:",font=("arial",20,"bold"),fg="gray30")
l8.grid(columnspan=4)

l9=Label(win,text="                                        ")
l9.grid(row=7,column=0)

t1=Text(win,font=("arial",15,"italic"),bd=5,width=60,height=10,bg="darkgray")
t1.grid(row=8,column=1)

l10=Label(win,text="Attached files:",font=("arial",20,"italic"),fg="steel blue")
l10.grid(row=9,column=0,sticky=E)
e4=Entry(win,textvariable=tf5,font=("arial",20),bd=3,width=45,bg="bisque2")
e4.grid(row=9,column=1)

l11=Label(win,text="                                        ")
l11.grid(row=10,column=0)

b1=Button(win,text="Reset",bd=10,font=("arial",15,"italic"),command=clearall)
b1.grid(row=11,column=0)

b2=Button(win,text="Send Mail",bd=10,font=("arial",15,"italic"),command=pri)
b2.grid(row=11,column=1)

b3=Button(win,text="attachment",bd=10,font=("arial",15,"italic"),fg="red",command=attach)
b3.grid(row=11,column=2)


win.mainloop()

