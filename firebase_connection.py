import pyrebase

config = {
   "apiKey": "AIzaSyA2aLLP-4XMFhiYVGBU_QfUoIjXuNqZurg",
    "authDomain": "iet1-5ddc6.firebaseapp.com",
    "databaseURL": "https://iet1-5ddc6.firebaseio.com",
    "projectId": "iet1-5ddc6",
    "storageBucket": "iet1-5ddc6.appspot.com",
    "messagingSenderId": "819459300721",
    "appId": "1:819459300721:web:73ab2382ecbbb785"
  };

firebase = pyrebase.initialize_app(config)

db = firebase.database()
t = "10"
e = "12"
data = {"temperature":t,"ecg":e}
db.push(data)
k = {"name": "Ketan", "University": "VIT"}
a= {"name":"Afreen", "University":"VIT"}
db.child("students").child("Ketan").set(k)
db.child("students").child("Afreen").set(a)
        
