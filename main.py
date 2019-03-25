from driver import Driver
import threading

def new_driver(email,password,coordinate):
    Driver(email,password,coordinate)
d1 = threading.Thread(target=new_driver,args=('driver@gmail.Com','driverdriver',[10,12]))
d2 = threading.Thread(target=new_driver,args=('zied@gmail.com','ziedzied',[17,13]))
d1.start()
d2.start()
d1.join()
d2.join()
