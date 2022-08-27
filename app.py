from flask import Flask, render_template

app = Flask(__name__)

main_projects = [
    [
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

all_projects = [
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
def main_page():  # put application's code here
    return render_template('main_page.html', title='Main page', projects=main_projects)

@app.route('/projects')
def project_list():  # put application's code here
    return render_template('projects.html', title='Main page', projects=all_projects)

if __name__ == '__main__':
    app.run()
