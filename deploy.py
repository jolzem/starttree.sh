#!/usr/bin/env python

import yaml

with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
        #print(config)
    except yaml.YAMLError as exc:
        print(exc)
        exit

startpage = f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <link href="style.css" rel="stylesheet" type="text/css" />
        <title>New Tab</title>
        <!--THEME-->
        <link href="themes/{config[0]["theme"]}.css" rel="stylesheet" type="text/css" />
    </head>
    <body>"""

if config[1]['clock']:
    startpage += """
        <div id="clock"></div>
        <script src="clock.js"></script>"""

prompt = '#' if config[2]['username'] == 'root' else '$'

startpage += f"""
        <div id="parent">
            <h4>
                <span class="cmd-dir">[{config[2]['username']}@{config[3]['hostname']}:~] </span>
                <span class="cmd-dollar">{prompt}</span>
                <span class="cmd-cmd">./startpage.sh</span>
            </h4>
            <div id="trees">
"""

i = 0

while i < int(config[4]['num_trees']) * 2:
    startpage += f"""
                <div class="title" style="grid-column: {i+1}">
                    <h4>
                        <!--TREE TITLE-->
                        <span class="cmd-cmd">{config[5]['trees'][i]['title']}:</span>
                    </h4>
                </div>
                <div class="tree" style="grid-column: {i+1}">
                    <ul>
    """

    i += 1

    for j in range(len(config[5]['trees'][i]['items'])):
        for name, url in (config[5]['trees'][i]['items'][j]).items():
            startpage += f"<li><a href='{url}'>{name}</a></li>\n"

    startpage += "</ul>\n</div>\n"

    i += 1

startpage += "</div>"

if config[6]['search']:
    startpage += f"""
            <h4>
                <span class="cmd-dir">[{config[2]['username']}@{config[3]['hostname']}:~]</span>
                <span class="cmd-dollar">{prompt}</span>
                <span class="cmd-cmd">./search.sh -e {config[7]['search_name']}</span>
            </h4>
            <form action="{config[8]['search_url']}" method="GET" class="search-form">
                <h4 class="search-title"> Search: </h4>
                <input type="text" name="{config[9]['search_query']}" autofocus class="search-input" />
            </form>"""

startpage += """
        </div>
    </body>
</html>
"""

f = open("index.html", "w")
f.write(startpage)
f.close()
