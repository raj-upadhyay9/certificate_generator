from flask import Flask,request,send_file
from PIL import Image, ImageFont, ImageDraw


app = Flask(__name__)
 
 
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/getcert',methods=['GET'])
def getcert():    
    name = request.args.get("name")
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)
    
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name +".png")
    print('Saving Certificate of:', name)
    
    return send_file("./out" + name + ".png") 
    
    
    
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()