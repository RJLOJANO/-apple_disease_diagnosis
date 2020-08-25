import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import predecir

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './image'
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]
app.config["IMAGE_UPLOADS"] = ""

@app.route('/')
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]
            

            if image.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_image(image.filename):
                return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("home.html")

#Button_p = 0
#@app.route('/class/upload', methods=["GET", "POST"])
#def button_p():
 #   os.system('python predecir.py')
  #  return render_template("home.html", Button_p = Button_p)

@app.route("/predecimiento",methods=["GET","POST"])
def predec():
    if request.method == 'POST':
        image = request.files['image']
        filename = secure_filename(image.filename)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'filename')
        
        op=int(predecir.predict(filename))
        
        
        if op==0:
            upload_oxido()
        
            return render_template("costra.html")
            
        if op==1:
            upload_costra()
            return render_template("oxido.html")
    
        if op==2:
            upload_podrir()
            return render_template("saludable.html")
            
        if op==3:
            upload_saludable()
            return render_template("podrir.html")
    #return render_template("home.html")

        

@app.route("/entrena/oxido",methods=["GET", "POST"])
def upload_oxido():
    image = request.files["image"]

    filename = secure_filename(image.filename)

    print("Image Guardada")
    return render_template("oxido.html")


@app.route("/entrena/podrir",methods=["GET", "POST"])
def upload_podrir():
    image = request.files["image"]
    filename = secure_filename(image.filename)


    print("Image Guardada")
    return render_template("podrir.html")


@app.route("/entrena/costra<image>",methods=["GET", "POST"])
def upload_costra():
    image = request.files["image"]

    filename = secure_filename(image.filename)
      
    

    print("Image Guardada")
    return render_template("costra.html")


@app.route("/entrena/saludable",methods=["GET", "POST"])
def upload_saludable():
    image = request.files["image"]

    filename = secure_filename(image.filename)
    print("Image Guardada")
    return render_template("saludable.html")


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def home():
    return render_template('home.html')
if __name__=="__main__":
    app.run(debug=True)
