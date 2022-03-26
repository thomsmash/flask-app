from flask_frozen import Freezer

# instead of "filename," below, use the name of the file that
# runs YOUR Flask app - omit .py from the filename
from index import app
from index import tvshows_list

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def tvshow():
        yield ('/tvshow/1')
        yield ('/tvshow/2')
        yield ('/tvshow/3')
        yield ('/tvshow/4')
        yield ('/tvshow/5')
        yield ('/tvshow/6')
        yield ('/tvshow/7')
        yield ('/tvshow/8')
        yield ('/tvshow/9')
        yield ('/tvshow/10')
        yield ('/tvshow/11')
        yield ('/tvshow/12')
        yield ('/tvshow/13')
        yield ('/tvshow/14')
        yield ('/tvshow/15')
        yield ('/tvshow/16')
        yield ('/tvshow/17')
        yield ('/tvshow/18')
        yield ('/tvshow/19')
        yield ('/tvshow/20')

if __name__ == '__main__':
    freezer.freeze()
