from flask import render_template, abort, request, g
from scripts.DB import DataBase
from app import *

app = Flask(__name__)
dbase: DataBase = None

main_projects = [
    [
        {'title': 'Platformetic', 'image': '/images/platformetic.png',
         'descr': 'Simple platformer with elements of bullet hell',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/PygamePlatformer',
                   'img': '/images/github.png'}]},
        {'title': 'Dungetic', 'image': '/images/dungetic.png',
         'descr': 'Rogue-like game with elements of RPG',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/Dungetic',
                   'img': '/images/github.png'}]}
    ],
]

all_projects = [
    [
        {'title': 'Platformetic', 'image': '/images/platformetic.png',
         'descr': 'Simple platformer with elements of bullet hell',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/PygamePlatformer',
                   'img': '/images/github.png'}]},
        {'title': 'Dungetic', 'image': '/images/dungetic.png',
         'descr': 'Rogue-like game with elements of RPG',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/Dungetic',
                   'img': '/images/github.png'}]},
        {'title': 'Platformetic', 'image': '/images/platformetic.png',
         'descr': 'Simple platformer with elements of bullet hell',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/PygamePlatformer',
                   'img': '/images/github.png'}]}
    ],

    [
        {'title': 'Platformetic', 'image': '/images/platformetic.png',
         'descr': 'Simple platformer with elements of bullet hell',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/PygamePlatformer',
                   'img': '/images/github.png'}]},
        {'title': 'Platformetic', 'image': '/images/platformetic.png',
         'descr': 'Simple platformer with elements of bullet hell',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/PygamePlatformer',
                   'img': '/images/github.png'}]},
        {'title': 'Platformetic', 'image': '/images/platformetic.png',
         'descr': 'Simple platformer with elements of bullet hell',
         'refs': [{'ref': 'https://github.com/TecHeReTiC3141/PygamePlatformer',
                   'img': '/images/github.png'}]}
    ],

]


project_descr = {}
descriptions = Path('descriptions')
for file in descriptions.glob('*.html'):
    with open(file) as f:
        project_descr[file.stem] = {
            'description': f.read().strip(),
            'img': f'/images/{file.stem}.png',
            'name': file.stem,
        }


def get_db() -> sqlite3.Connection:
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.before_request
def get_dbase():
    global dbase
    dbase = DataBase(get_db())


@app.route('/')
def main_page():
    return render_template('main_page.html', title='Main page', projects=main_projects)


@app.route('/projects')
def project_list():
    return render_template('projects_page.html', title='Main page', projects=all_projects)


@app.route('/projects/<name>')
def project_page(name: str):
    name = name.lower()
    if name not in project_descr:
        abort(404)
    return render_template(f'project_page.html', project=project_descr[name])


@app.route('/skills')
def skills():
    return render_template('skills.html', title='Skills')


@app.errorhandler(404)
def error404(error):
    return render_template('error404.html')


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run()