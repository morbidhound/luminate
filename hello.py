from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
   return render_template('hello.html',name=name)

@app.route('/cpick',methods=['GET','POST'])
def cpick():
   if request.method=='POST':
      print(request)
   return render_template('cpick.html')

if __name__ == '__main__':
   app.run('0.0.0.0',debug=True)
