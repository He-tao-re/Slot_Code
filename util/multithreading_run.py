import time
import random
from multiprocessing import Process


class Run(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print('%s runing' %self.name)
        time.sleep(random.randrange(1,5))
        print('%s runing end' %self.name)

p1=Run('anne')
p2=Run('alex')
p3=Run('ab')
p4=Run('hey')
if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主线程')