import check
import image_downloader
from multiprocessing import Queue
import engine




city='Galle'
api='47c6a200841b1d4a6720b31e29dff310'

if __name__ == "__main__":
    print("Running")
    queries=Queue()
    images=Queue()
    weathers={}
    
    weather=check.check(api, city,queries)
    weather.start()
    downloader=image_downloader.imagedownloader(queries,images)
    downloader.start()
    engine=engine.Engine(images)
    engine.start()
    weather.join()
    downloader.join()
    engine.join()
    
