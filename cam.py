#follow Vivek_Codes for more intresting Tech memes and Projects

# importing module
import requests 
import cv2 
import numpy as np 

# your URL
url = "your URL HERE!!!" + "/shot.jpg" 

while True:
    response = requests.get(url) #send GET request to URL
    arr = np.array(bytearray(response.content),dtype=np.uint8) #converting response to numpy array
    img = cv2.imdecode(arr,-1)#decoding numpy array
    
    cv2.imshow("Vivek_Codes", img)# showing image
    if cv2.waitKey(1) == 27: #if usr press esc key thn break the while loop
        break
