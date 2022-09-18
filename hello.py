from flask import Flask,request,render_template
from custom import hex_to_rgb
from examples import *
import sys
app = Flask(__name__)

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

@app.route('/<name>')
def hello_world(name):
   print("euri",flush=True)
   return render_template('hello.html',name=name)

@app.route('/cpick',methods=['GET','POST'])
def cpick(last_color="#a38d50",solid="checked",flash=""):
   if request.method=='POST':
      last_color=request.form['col']
      if request.form['flexRadioDefault'] == 'flash':
         flash='checked'
         solid=''
      else:
         flash=''
         solid='checked'
      print(hex_to_rgb((last_color.split('#')[1]).upper()),flush=True)
      return render_template('cpick.html', last_color=request.form['col'], solid=solid, flash=flash)
      
   return render_template('cpick.html',solid=solid,flash=flash)

@app.route('/base',methods=['GET','POST'])
def bases():
   return render_template('test.html')

if __name__ == '__main__':
   app.run('0.0.0.0',debug=True)
