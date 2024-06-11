from threading import Thread
import requests
from multiprocessing import Process
import json
import time

class imagedownloader(Process):
    def __init__(self, queries,images):
        super(imagedownloader, self).__init__()
        self.queries = queries
        self.prequires=None
        self.images=images
    def run(self):
        query = self.queries.get()
        print("Running query",query)
        while query is not None :
            if self.prequires == query:
                self.prequires=query
                print("Same query")
                query = self.queries.get()
                continue
            
            url=f'https://unsplash.com/napi/search/photos?page=1&query={query}'
        
            r =requests.get(url)
            
            
            if r.status_code == 200:
               
                response = json.loads(r.content)
                results=response['results']
                for image in results:
                    self.__download_images(image)
            else:
                print(f'Error: {r.status_code}')
            
            query = self.queries.get()
            self.prequires=query
            
            
            
    def __download_images(self,image):
        urls=image['urls']
        raw=urls['raw']
        print(raw)
        
        res = requests.get(raw,stream=True)
        if res.status_code == 200:
            res.raw.decode = True
            x=raw.split('?')
            name=x[0].split('/')[-1]
            
            file_name=f"images/{name}.jpg"
            with open(file_name,'wb') as f:
                f.write(res.content)
                
            self.images.put(file_name)
            print(f"Downloaded {file_name}")
        else:
            print(f'Error: {res.status_code}')