from flask import Flask,request,render_template
from custom import hex_to_rgb
import sys
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
   print("euri",flush=True)
   return render_template('hello.html',name=name)

@app.route('/cpick',methods=['GET','POST'])
def cpick(last_color="#a38d50"):
   if request.method=='POST':
      last_color=request.form['col']
      print(hex_to_rgb((last_color.split('#')[1]).upper()),flush=True)
      return render_template('cpick.html', last_color=request.form['col'])
      
   return render_template('cpick.html')

@app.route('/base',methods=['GET','POST'])
def bases():
   return render_template('base.html')

if __name__ == '__main__':
   app.run('0.0.0.0',debug=True)
