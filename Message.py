import pywhatkit as pwk
import pyautogui as pg
import sys

phoneNumber=sys.argv[1]
Num="+91"+sys.argv[1]
Message=sys.argv[2]

pwk.sendwhats_image(Num,"SRPNew.jpg", "Cuberreality is Inviting Sellers/Owners From Sobha Royal Pavilion,we have buyers Call Us : +919999999999, Visit https://cuberreality.com", 15, True, 10)
# try:
#      sending message in Whatsapp in India so using Indian dial code (+91)
     
#      pwk.sendwhats_image(" Team",
#       "cuber1.png", "Hi, This is  test message sent from pywhatkit")
 
#      pwk.sendwhats_image("+91 999999999", "CuberRealityLogo.svg", "Hi, This is  sent from pywhatkit", 23, 34)
#      pwk.sendwhats_image("+91 999999999","cuber1.png", "test", 10, True, 6)
#      pwk.sendwhatmsg("+91 999999999", "https://cuberreality.com", 20, 29)
#      Prints success message in console
     
#      print("Message Sent!") 
#      error message
# except: 
#      print("Error in sending the message")



 

 



