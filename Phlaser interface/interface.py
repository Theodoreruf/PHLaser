from asyncio.windows_events import NULL
import tkinter as tk
from PIL import Image, ImageTk 
from PIL.Image import core as _imaging
import cv2
import numpy as np



class Interface(tk.Frame):
    def __init__(self,video_source=0):
        self.root = tk.Tk()
        super().__init__(self.root)
        
        self.root.geometry('1000x480')  #Width*Height

        #To change the background color of the window
        self.root['bg'] = '#d80000' 
    
        
        # ---------------------------------------------------------
        # Open the video source
        # ---------------------------------------------------------

        self.vcap = cv2.VideoCapture( video_source )
        self.width = self.vcap.get( cv2.CAP_PROP_FRAME_WIDTH )
        self.height = self.vcap.get( cv2.CAP_PROP_FRAME_HEIGHT )
        
        #
        
        #photo = ImageTk.PhotoImage(file="Iphone-xr-yellow.png")
        #photo2 = ImageTk.PhotoImage(file="iphone_x.jpg")
        #1 Canevas
        self.Canevas_t = tk.Canvas(self.root)
        self.Canevas_t.config(width= self.width, height=self.height)  # Règle la taille du canvas par rapport à la taille de l'image 
        self.Canevas_t.pack(side='left')

        #First Label
        label1_1 = tk.Label(self.root, text="Phlaser",font=("Courier", 30))
        label1_1['fg'] = '#d3c04d' #To change the frontground color of the label
        label1_1['bg'] = '#d80000' #To change the background color of the label
        label1_1.pack()

        #Scale 1
        #The Scale will give the value of the cursor to the function speed_control()
        Scale1 = tk.Scale(self.root, orient='horizontal', from_=0, to=100,resolution=1, tickinterval=10, length=350,label='Speed (%)',command=lambda value, name=tk.Scale: self.speed_control(value))
        Scale1['fg'] = '#d3c04d' #To change the frontground color of the label
        Scale1['bg'] = '#d80000' #To change the background color of the label
        Scale1.pack(pady = 20) #Distance between the inner box that contains the button and the button

        #First button
        btn1_1 = tk.Button(self.root, text="Température", command = self.create)
        btn1_1['bg'] = '#d3c04d' #To change the background color of the button
        btn1_1.pack(pady = 60) #Distance between the inner box that contains the button and the button

        #Start button
        btn1_2 = tk.Button(self.root, text="Start", command = self.start)
        btn1_2['bg'] = '#d3c04d' #To change the background color of the button
        btn1_2.pack( pady= 20) # pady -> Distance between the inner box that contains the button and the button

        #Stop button
        btn1_3 = tk.Button(self.root, text="Stop", command = self.stop)
        btn1_3['bg'] = '#d3c04d' #To change the background color of the button
        btn1_3.pack( pady= 20) # pady -> Distance between the inner box that contains the button and the button

        #Icon
        self.root.tk.call(
        'wm', 
        'iconphoto', 
        self.root._w, 
        tk.PhotoImage(file='laser.png')
        )
        self.reload_frame()
        


    

    def reload_frame(self):
       
        #Get a frame from the video source
        _, frame = self.vcap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))

        #self.photo -> Canvas
        self.Canevas_t.create_image(0,0, image= self.photo, anchor = tk.NW)

        self.master.after(15, self.reload_frame)


    
    
    
    


    def quit_win(self):#To close the second window
        self.win.destroy()

    def create(self):
        self.win = tk.Toplevel(self.root)
        self.win.geometry('1000x480')  #Width*Height
        self.win['bg'] = '#d80000'  #To change the background color of the window
        
        #First Label in the second window
        label2_1 = tk.Label(self.win, text=self.display_temp())
        label2_1['bg'] = '#d3c04d' #To change the background color of the label
        label2_1.pack()
        

        #First button on the second window
        btn2_1 = tk.Button(self.win, text="Retour", command = self.quit_win)
        btn2_1['bg'] = '#d3c04d' #To change the background color of the button              
        btn2_1.pack(side = tk.BOTTOM) #To put the button at the bottom 

        #Icon
        self.win.tk.call(
        'wm', 
        'iconphoto', 
        self.win._w, 
        tk.PhotoImage(file='laser.png')
        )

    def start(self):
        #PUT HERE THE CODE TO START THE PROCESS 
        print("Starting the process...")  

    def stop(self):
        #PUT HERE THE CODE TO STOP THE PROCESS 
        print("Stoping the process...")
    
    def display_temp(self):
        #PUT HERE THE CODE TO RETRIEVE THE TEMPERATURE
        print("40°C")

        return "ICI IL FAUT RECUPERER LA VALEUR QU'AFFICHE LE CAPTEUR DE TEMPERATURE"
    
    def speed_control(self,value):
        #PUT HERE THE CODE TO CHANGE THE SPEED
        print("Speed changed to", value ,"%" )




def main():
    
    app = Interface()#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()
