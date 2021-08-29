# firebase imports
import pyrebase
import uuid
import random

def init():
	firebaseConfig = {
		"apiKey": "AIzaSyDxEfgarWakUpDHQDu1Ws1BD1KzstbZSEY",
		"authDomain": "olas-f3ad7.firebaseapp.com",
		"databaseURL": "https://olas-f3ad7-default-rtdb.firebaseio.com/",
		"projectId": "olas-f3ad7",
		"storageBucket": "olas-f3ad7.appspot.com",
		"messagingSenderId": "184572869633",
		"appId": "1:184572869633:web:b52415d0c3b28302b31400",
		"measurementId": "G-BC3KP5NQ37"
	}

	firebase = pyrebase.initialize_app(firebaseConfig)

	global db
	db = firebase.database()
	# items = db.get()
	# for person in items.each():
	# 	# print(person.val())
	# 	print(person.key())
	# 	db.child(person.key()).remove()
	# 	# print(person.val())

	# for i in range(50):
	# 	data = {
	# 		"user_id": str(uuid.uuid1()),
	# 		"upload_date": str(random.randint(0, 1000)),
	# 	}
	# 	db.push(data)

if __name__ == '__main__':
	init()

# # Push data
# data = {
# 	"name": "gaming",
# 	"age": "20"
# }

# db.push(data)
# user = db.child("-MiFKdihsM65wW-WWHeU").get()
# print(user.val())