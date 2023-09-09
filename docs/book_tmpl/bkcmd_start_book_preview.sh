###########################################################
# START HTTP server to preview the book
#
###########################################################



# #NOTE DO NOT USE THIS, but python http server - this one: `mkdoks serve`

# #FIXME use mkdocs build with params like explained here `https://www.mkdocs.org/user-guide/cli/#mkdocs-get-deps`

# #TODO for live preview:
#   - the site build is supposed to be already done (`mkdocs build --site-dir ...`)
#   - use `mkdocs serve --no-livereload` to start local HTTP server without monitorig file changes


# --------------------------
# LINUX version:
# start serving from local directory on port 8000
python3 -m http.server #TODO consider to launch in backgroud with `&` but use `named run` to know what to kill




