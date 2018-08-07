from manhole import Manhole
from flask import Flask,render_template, request,send_file,redirect
from forms import ManholeForm
import os
from flask_wtf import FlaskForm

app=Flask(__name__)
app.debug = True
app.secret_key = '1q2w3e4r5t6y'
@app.route('/',methods = ['GET', 'POST'])
def mainpage():
   form=ManholeForm()
   return render_template('/index.html',form=form)

@app.route('/result',methods=['GET', 'POST'])
def resultpage():
   if request.method=='POST':
      name=request.form.get('name')
      gl=float(request.form.get('gl'))
      il=float(request.form.get('il'))
      x=float(request.form.get('x'))
      y=float(request.form.get('y'))
      manhole=Manhole(name,gl,il,x,y)
      parca=manhole.Parcahesap()
      manhole.Ciz()
      link="/dxf/"+name+".dxf"
      return render_template('result.html', manhole=manhole,parca=parca,link=link)
   else:
      return redirect('/')


@app.route("/dxf/<path:path>")
def get_file(path:None):
      return send_file('dxf/'+path, as_attachment=True)


@app.route('/download',methods=['GET'])
def download():
   result=[]
   for file in os.listdir(os.getcwd()+"\\dxf"):
      link="/dxf/"+file
      result.append((file,link))
   return render_template('download.html',result=result)

if __name__ == '__main__':
   app.run()