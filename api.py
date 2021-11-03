from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [
    {
    "id":1,
    'title':U'Buy Groceries',
    'description':U'Milk,Pizza,Cheese,Fruit',
    'done':False
    },
    {
    "id":2,
    'title':U'Learn Python',
    'description':U'Need to find some good tutorials',
    'done':False
    }
]
@app.route('/')
def helloworld():
    return 'Hello World'
@app.route('/add-data',methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please Provide The Data'
        },400)
    task = {
        "id":tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False  
    }
    tasks.append(task)
    return jsonify({
            'status':'success',
            'message':'Task Added Successfully'
    })
@app.route('/getdata')
def gettask():
    return jsonify({
        'data':tasks
    })
if(__name__ == '__main__'):
    app.run(debug = True)