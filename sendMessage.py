import pywhatkit as pwk
import pyautogui as pg
import sys

try:
  
     # sending message in Whatsapp in India so using Indian dial code (+91)
     
     #pwk.sendwhats_image("Team", "test.png", "Hi, This is  test message sent from pywhatkit")

     phoneNumber=sys.argv[1]
     Num="+91"+sys.argv[1]
     Message=sys.argv[2]
     pwk.sendwhats_image(Num,"SRP.jpg", "Inviting Sellers/Owners From Sobha Royal Pavilion,we have buyers Call Us : +91 99999999 . visit "test.com", 15, True, 25)
     #pwk.sendwhats_image(Num, "SRP1.png")
    
     print("Message Sent!") 
     # error message
except: 
     print("Error in sending the message")



 

 



