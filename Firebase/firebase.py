import pyrebase

class Firebase:

    firebaseConfig = { # Nằm trong General
        'apiKey': "AIzaSyANJLHv-MiuM-7ATuBGwOWiFoZtA9sBtCI",
        'authDomain': "pyqt5-demo.firebaseapp.com",
        'databaseURL': "https://pyqt5-demo-default-rtdb.firebaseio.com",
        'projectId': "pyqt5-demo",
        'storageBucket': "pyqt5-demo.appspot.com",
        'messagingSenderId': "106488053967",
        'appId': "1:106488053967:web:c94cb30d14833467bcb7ba",
        'measurementId': "G-WZQFKE14DS"
    }

    def __init__(self):
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.db = self.firebase.database()

    def get_led_value(self):
        self.led_value = self.db.child("control").child("led").get().val()
        return self.led_value

    def get_temp_value(self):
        self.temp_value = self.db.child("display").child("temperature").get().val()
        return self.temp_value
    
    def get_humi_value(self):
        self.humi_value = self.db.child("display").child("humidity").get().val()
        return self.humi_value

    def update_led(self, value):
        self.db.child("control").update({"led": value})

    def update_noti(self, text):
        self.db.child("notification").update({"text": text})