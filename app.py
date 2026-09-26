from flask import Flask, render_template, request
import url_rules

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    url = None
    punkte = None
    feedback = None
    begruendung = None
    
    if request.method == "POST":

        url = request.form["theUrl"]
        begruendung = url_rules.pruefeURL(url)
        punkte = 0

        for i in begruendung:
            punkte += begruendung[i]

        if punkte >= 4:
            feedback = "Die URL ist sehr verdaechtig!!"
        elif punkte >= 2:
            feedback = "Die URL ist verdaechtig!!"
        elif punkte == 0:
            feedback = "Die URL ist sicher! :)"
        

    return render_template("index.html",
                            url = url,
                            punkte = punkte,
                            feedback = feedback,
                            begruendung = begruendung
    )

if __name__ == "__app__":
    app.run(debug= True)

