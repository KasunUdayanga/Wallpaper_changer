from multiprocessing import Process
import os
import ctypes
import time
from os import path

SPI_SETDESKWALLPAPER=20
class Engine(Process):
    def __init__(self,images):
        super(Engine, self).__init__()
        self.images = images
    
    def run(self):
        image = self.images.get()
        while True:
            file_name= image.split("/")[-1]
            image = path.join(os.getcwd(), "images",file_name)
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, image, 0
                )
            print("set walpper")
            time.sleep(5)
            image = self.images.get()
            
            
            (20, 0, "absolute path" , 0)