# -*- coding: utf-8 -*-
import os
import dash
from dash import dcc
from dash import html
import uvicorn as uvicorn
from dash.dependencies import Input, Output
from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware

from pages import (
    overview,
    wun,
    two,
)

URL_PATH_SEP = '/'
HOST = os.getenv('REPORT_HOST', 'localhost')
PORT = os.getenv('REPORT_PORT', '8765')
URL_BASE_PATHNAME = os.getenv('REPORT_URL_BASE', URL_PATH_SEP)
if URL_BASE_PATHNAME[-1] != URL_PATH_SEP:
    URL_BASE_PATHNAME += URL_PATH_SEP

app = dash.Dash(
    __name__,
    url_base_pathname=URL_BASE_PATHNAME,
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Some Report"
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == f'{URL_BASE_PATHNAME}wun':
        return wun.create_layout(app)
    elif pathname == f'{URL_BASE_PATHNAME}two':
        return two.create_layout(app)
    elif pathname == f'{URL_BASE_PATHNAME}full-view':
        return (
            overview.create_layout(app),
            wun.create_layout(app),
            two.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    server = FastAPI()
    server.mount(URL_PATH_SEP, WSGIMiddleware(app.server))
    uvicorn.run(server, host=HOST, port=PORT, headers=[("server", "server/1")])

    # app.run_server(debug=False, port=8765)
