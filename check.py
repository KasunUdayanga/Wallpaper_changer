from threading import Thread
import requests
import json
from multiprocessing import Process
import time

class check(Process):
    def __init__(self,key,city,queries,delay=5):
        super(check, self).__init__()
        self.key = key
        self.city=city
        self.delay=delay
        self.queries=queries
        
    def run(self):
        while True: 
            weather = self.__get_weather_report(self.key,self.city)
           # self.__update_weather(weather)
            self.queries.put(weather)
            time.sleep(self.delay)
            
    def __update_weather(self,weather):
        for attr in  ['id', 'main', 'description', 'icon']:
            self.weather[attr]=weather[attr]
       
    def __get_weather_report(self,api,city):
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
        response=requests.get(url)
        if response.status_code==200:
            json_content=json.loads(response.content)
            weather=json_content['weather']
            if weather:
                return weather[0]
            print (weather)
