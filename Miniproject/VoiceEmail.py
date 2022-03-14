# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:47:05 2021

@author: prashant sehrawat
"""

#Libraries


import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import easyimap as e

l =sr.Recognizer()
engine=pyttsx3.init()

# Email_List saved inside your system

email_list ={ 'Gaurav':'gauravsehrawat9813@gmail.com','Ankit':'ankitsharma97194@gmail.com','Ashok':'ashokumar3693@gmail.com'
}


# choice funtion 

def choice():
    talk('Hey there.....Do You want send email or Read a new email')
    
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=l.listen(source, phrase_time_limit=5)
            
            choice=l.recognize_google(voice)
            
            print(choice)
            if "send" in choice:
                talk('If you want to send email from existing list say....list or say new one for a new user ')
                try:
                    with sr.Microphone() as source:
                        print('listening...')
                        voice=l.listen(source,phrase_time_limit=3)
                        choice=l.recognize_google(voice)
                        print(choice)
                        if "list" in choice:
                            get_emailInfo()
                        if "new" in choice:
                            get_emailInfo1()
                except:
                    pass
            if "read" in choice:
                read_email()
    except:
        pass

#talk funtion using pyttsx3 module of python

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
#for getting a information from the user 

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=l.listen(source,phrase_time_limit=8)
            info=l.recognize_google(voice)
            print(info)
            return info
    except:
        pass


 #   for sending email to person of your own choice 
 
 
 
def get_emailInfo1():    
    talk('Please provide the email id of person to whom you want to send email')
    email_id=get_info()
    if "at the rate " in email_id:
        email_id=email_id.replace("at the rate","@" )
    email_id=email_id.replace(" ","")
    if 'dot' in email_id:
        email_id=email_id.replace("dot",".")
    talk('Please check the email id ')
    for i in email_id:
        talk(i)
    talk('Do You want to proceed with these Mail id say Yes or No')
    option=get_info()
    if(option=='yes'):
        print(email_id)
        talk('What Is The Subject Of Your Email')
        subject=get_info()
        talk('What Is The Message You Want To Send')
        message=get_info()
        send_email(email_id,subject,message)
        print('Email Sent Successfully')
        talk('Email Sent Successfully')
    if(option=='no'):
        get_emailInfo2()
        
 #Recieving information of person from the existing list
        
def get_emailInfo():    
    talk('To whom You Want To Send The Email')
    name=get_info()
    reciever=email_list[name]
    print(reciever)
    talk('What Is The Subject Of Your Email')
    subject=get_info()
    talk('What Is The Message You Want To Send')
    message=get_info()
    send_email(reciever,subject,message)
    print('Email Sent Successfully')
    talk('Email Sent Successfully')
    
  #for sending mail using the email Message module of python  
def send_email(reciever,subject,message):
    server=smtplib.SMTP('smtp.gmail.com',587)   #Port
    server.starttls()
    server.login('sehrawat.prashant1511@gmail.com','******Password****')
    email=EmailMessage()
    email['from']='sehrawat.prashant1511@gmail.com'
    email['to']=reciever
    email['subject']=subject
    email.set_content(message)
    server.send_message(email)

#function for reading mail from user's inbox

def read_email():
    password="***********"
    user="sehrawat.prashant1511@gmail.com"
    server=e.connect("imap.gmail.com", user, password)

    print(server.listids())
    email=server.mail(server.listids()[0])
    talk('you got a new email from')
    sender=email.from_addr
    print(sender)
    talk(sender)
    subject=email.title
    talk('Subject of the recieved mail is..')
    print(subject)
    talk(subject)
    talk('The Mail you Recieved is.....')
    message=email.body
    print(message)
    talk(message)


   
 #In case of wrong email id recognition by system
    
    
    
def get_emailInfo2():    
    talk('sorry.....Please enter email id again letter by letter...')
    email_id1=get_info1()
    if "at the rate " in email_id1:
        email_id1=email_id1.replace("at the rate","@")
    email_id1=email_id1.replace(" ","")
    if 'dot' in email_id1:
        email_id1=email_id1.replace("dot",".")
        talk('the email you entered is..')
        for i in email_id1:
            talk(i)
        talk('Do you Want to proceed with this email..Say yes Or No')
        option=get_info()
    if(option=='yes'):
            print(email_id1)
            talk('What Is The Subject Of Your Email')
            subject=get_info()
            talk('What Is The Message You Want To Send')
            message=get_info()
            send_email(email_id1,subject,message)
            print('Email Sent Successfully')
            talk('Email Sent Successfully')
    if(option=='no'):
            get_emailInfo2()
            
def get_info1():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=l.listen(source,phrase_time_limit=20)
            info=l.recognize_google(voice)
            print(info)
            return info
    except:
        pass
    
if __name__ == "__main__":
    choice()     
 
   
    






 







