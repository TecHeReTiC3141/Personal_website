from flask import render_template, abort,\
    request, g, flash, redirect, url_for
from scripts.DB import *
from scripts.Forms import *

from app import *

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
    project_descr[file.stem]['images'] = [f'/images/{file.stem}/{i.name}'
                                          for i in Path(f'static/images/{file.stem}').glob('*.png')]
    print(project_descr[file.stem]['images'])


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
    return render_template('projects_page.html', title='Projects', projects=all_projects)


@app.route('/projects/<name>', methods=['POST', 'GET'])
def project_page(name: str):
    name = name.lower()
    if name not in project_descr:
        abort(404)
    form = CommentForm()
    comments = dbase.get_comments(name.capitalize())
    if form.validate_on_submit():
        print('valid')
        user_name, mark, text = form.name.data, form.mark.data, form.text.data
        res = dbase.add_comment(name.capitalize(), user_name, mark, text)
        flash(res, category='success' if res == 'Successfully added' else 'error')
        return redirect(url_for('project_page', name=name, comments=comments))

    return render_template('project_page.html', project=project_descr[name],
                           form=form, title=name.capitalize(), comments=comments)


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
