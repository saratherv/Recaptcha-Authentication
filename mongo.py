import requests
import hashlib



def get_db():
    from pymongo import MongoClient
    client = MongoClient('mongodb://admin:sarathe26@ds149806.mlab.com:49806/imagekit')
    db = client.imagekit
    return db

def verifyToken(data):
    URL = "https://www.google.com/recaptcha/api/siteverify"
    PARAMS = {'secret' : '6LdX_aQUAAAAAPXsOz6HCUVyrtfH8csp3xBax3EX', 'response' : data['token']} 
    r = requests.get(url = URL, params = PARAMS) 
    response = r.json()
    print(response)
    return response['success']
    

def saveToIp(data):
    db = get_db()
    a =  db.ip.find_one_and_update( { "ip" : data['ip'] },
    { '$inc': { "count" : 1 } })
    print('inserted')
    if a == None:
        db.ip.insert_one({"ip":data['ip'], "count" : 1})
        return False
    if a['count'] >= 3:
        return True
    return False

def createUser(data):
    h = hashlib.md5(data['password'].encode())
    data['password'] = h.hexdigest()
    db = get_db()
    a = db.users.find_one({'email' : data['email']})
    print('val of a', a)
    if a==None:
        db.users.insert_one({'email' :data['email'],'username' : data['username'], 'password':data['password']})
        return 'user successfully registered'
    else:
        return 'user alreadt exist try other email id'
