from flask import Flask,jsonify,request
app=Flask(__name__)

Contacts= [{
    'id':1,
    'Name':u'Ji Maa',
    'description':u'My Mom',
    'done':False
},{
    'id':2,
    'Name':u'Papa',
    'description':u'My Father',
    'done':False
}
]

@app.route("/")

def hello_world():
    return "Fahim's Contacts"



@app.route("/add-data",methods=["POST"])

def add_data():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide the data',
        },400)
    Contact={
        'id':Contacts[-1]['id']+1,
        'Name':request.json['Name'],
        'description':request.json.get("description"," "),
        'done':False
    }
    
    Contacts.append(Contact)

    return jsonify({
        "status":"success",
        "message":"Contact added Successfully"
    })



@app.route("/get-data")

def get_task():
    return jsonify({
        'data':Contacts
    })

if __name__ == '__main__':
    app.run(debug=True)