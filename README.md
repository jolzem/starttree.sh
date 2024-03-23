# starttree.sh
A simple configurable tree style startpage in HTML and CSS with interchangeable and customisable themes.

![Preview](preview.png)

## Installation

### Chrome / Chromium
1. Clone git repo
2. Go to extensions
3. Toggle Developer mode on
4. Click on Load Unpacked
5. Select the directory you cloned the git repo

### Firefox
1. Clone git Repo
2. Find instructions on how to install further [here](https://redd.it/ge86z4).

### Safari
1. Clone git Repo
2. Generate a startpage and open it with Safari
3. Go to `Settings` > `General`
4. Under *Homepage* click `Set to Current Page`

## Configuration

### General
Configure your starttree in the `config.yml` file like so:

```yaml
- theme: "black"
- clock: true
- username: "root"
- hostname: "startpage"
- num_trees: 3
- trees:
  - title: "General"
  - items:
    - gmail: "https://mail.google.com"
    - github: "https://github.com"
  - title: "Entertainment"
  - items:
    - youtube: "https://www.youtube.com/"
    - reddit: "https://reddit.com/"
  - title: "Work"
  - items:
    - git: "https://git.work.org"
    - homepage: "https://www.work.org"
- search: true
- search_name: "startpage-search"
- search_url: "https://www.startpage.com/sp/search"
- search_query: "query"
```

You can find all themes in the `themes/` directory.

### Search
To configure your search, search for something in your favorite search engine. The URL will look something like this:

`https://www.startpage.com/sp/search?query=something`

In this case the `search_url` would be `https://www.startpage.com/sp/search` and the `search_query` would be `query`.

