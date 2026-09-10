from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    name=request.form['name']
    email=request.form['email']
    Student_id=request.form['Student_id']
    year=request.form['year']
    
    return render_template('successfull.html',name=name,email=email,Student_id=Student_id,year=year)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    