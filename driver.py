import requests
import websocket
from time import sleep
import json

class Driver :
    def __init__(self,email,password,starting_coordinates):
        print('create new driver object')
        self.email = email
        self.password = password
        self.token = self.get_token(self.email,self.password)
        self.starting_coordinates = starting_coordinates
        self.start_ws_connection()

    def get_token(self,email,password):
        data = {'email':email,'password':password}
        headers = {'Content-Type':'application/json'}
        res = requests.post('http://127.0.0.1:8000/api/token/',data=json.dumps(data),headers=headers)
        token = res.json()['token']
        return token
    def start_ws_connection(self):
            def on_message(ws, message):
                print(message)

            def on_error(ws, error):
                print(error)

            def on_close(ws):
                print('closed')

            def on_open(ws):
                print('open connection')
                for i in range(20) :
                    ws.send(json.dumps({'coordinates':[str(self.starting_coordinates[0]),str(self.starting_coordinates[1])]}))
                    self.starting_coordinates[0] = self.starting_coordinates[0] + 0.05
                    sleep(1)
                ws.close()
                print('close connections')
            ws = websocket.WebSocketApp("ws://127.0.0.1:8000/ws/driver_delivery_company/?token="+self.token,
                                      on_open = on_open,
                                      on_message = on_message,
                                      on_error = on_error,
                                      on_close = on_close)

            ws.run_forever()


# class DriverManger(Thread):
#
#     def run():
#         self.driver_obj = Driver(email,password,starting_coordinates)
