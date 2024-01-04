from flask import Flask,jsonify

app = Flask(__name__)
guests=[]

books=[
    {"id":1,"title":"Book1","author":"Author 1"},
    {"id":2,"title":"Book2","author":"Author 2"},
    {"id":3,"title":"Book3","author":"Author 3"}
]
@app.route("/books/<int:book_id>",methods=["GET"])

def Greet():
    return "<p>Welcome to book Management System</p>"
    # return guests

def get_all_book():
    return jsonify({"book":books})

def get_book(book_id):
    book = next((b for b in books if b["id"]==book_id),None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error":"Book not found"}),404
if __name__=="__main":
    app.run(host="0.0.0.0",port=6000,debug=True)
    