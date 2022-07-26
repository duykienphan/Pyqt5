from typing_extensions import Self
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

  def get_data(self):
    temperature = self.db.child("display").child("temperature").get().val()
    print(temperature)
    humidity = self.db.child("display").child("humidity").get().val()
    print(humidity)

  def update_data(self, value):
    self.db.child("control").update({"led": value})

if __name__ == "__main__":
    database = Firebase()
    database.get_data()
    database.update_data(31)
