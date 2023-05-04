

from flask import Flask, render_template, request

import app1
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def index():
    if request.method == 'POST':
        p = request.form['popularity']
        a = request.form['acousticness']
        d = request.form['danceability']
        # du = request.form['duration_ms']
        # e = request.form['energy']
        i = request.form['instrumentalness']
        # k = request.form['key']
        # li = request.form['liveness']
        lo = request.form['loudness']
        m = request.form['mode']
        s = request.form['speechiness']
        # t = request.form['tempo']
        # o = request.form['obtained_date']
        v = request.form['valence']
        # arc = request.form['artist_code']
        arg = request.form['art_genre']
       
        
        y_pred = [[p,a,d,i,lo,m,s,v,arg]]
        
        # X_new = [[53,0.026400,0.888,187.207,0.6580,0.0000,9,0.1450,-6.037,1,0.2780,145.033,2,0.6260,3900,53]]

        value=app1.obtained_music(y_pred)

        # {'Alternative': 0, 'Anime': 1, 'Blues': 2, 'Classical': 3, 'Country': 4, 'Electronic': 5, 'Hip-Hop': 6, 'Jazz': 7, 'Rap': 8, 'Rock': 9}
    
        if value == 0:
            return render_template('index.html', Alternative='Alternative',show_modal=True)
        elif value == 1:
            return render_template('index.html', Anime='Anime',show_modal=True)
        elif value == 2:
            return render_template('index.html', Blues='Blues',show_modal=True)
        elif value == 3:
            return render_template('index.html', Classical='Classical',show_modal=True)
        elif value == 4:
            return render_template('index.html', Country='Country',show_modal=True)
        elif value == 5:
            return render_template('index.html', Electronic='Electronic',show_modal=True)
        elif value == 6:
            return render_template('index.html', Hip_Hop='Hip-Hop',show_modal=True)
        elif value == 7:
            return render_template('index.html', Jazz='Jazz',show_modal=True)
        elif value == 8:
            return render_template('index.html', Rap='Rap',show_modal=True)
        
        else:
            return render_template('index.html', Rock='Rock',show_modal=True) 

    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
