from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)
application = app

# create a list of dicts from a CSV
tvshows_list = convert_to_dict("tvshows.csv")

# create a list of tuples in which the first item is the number
# (Presidency) and the second item is the name (President)
pairs_list = []
for show in tvshows_list:
    pairs_list.append( (show['ID'], show['Name']) )

# first route

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="TV Shows Index")

# second route

@app.route('/tvshow/<num>')
def detail(num):
    try:
        tvshow_dict = tvshows_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Tv Show: {num}</h1>"
    # a little bonus function, imported on line 2 above
    ord = make_ordinal( int(num) )
    return render_template('tvshow.html', tv=tvshow_dict, ord=ord, the_title=tvshow_dict['Name'])


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
