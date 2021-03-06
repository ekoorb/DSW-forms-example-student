from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/",methods=['GET'])
def render_main():
    return render_template('home.html')

@app.route("/response", methods=['POST'])
def render_response():
    color = request.form['color']
    #The request obj. stores info about the request sent to the server. 
    #The args is a multi dict,(like a doctionary) but it can have multiple values for the same key
    #The info in args is visible in the url for the pages being requested (ex.../response?color=blue)
    if color == 'lavender':
        reply = "That's my favorite color, too"
    else:
            reply = "My favorite color is lavender."
            return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
