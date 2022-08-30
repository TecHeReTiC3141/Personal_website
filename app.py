from flask import Flask, render_template

app = Flask(__name__)

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


@app.route('/')
def main_page():
    return render_template('main_page.html', title='Main page', projects=main_projects)


@app.route('/projects')
def project_list():
    return render_template('projects.html', title='Main page', projects=all_projects)

@app.route('/skills')
def skills():
    return render_template('skills.html', title='Skills')


if __name__ == '__main__':
    app.run()
