# -*- coding: utf-8 -*-
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

app = dash.Dash(
    __name__,
    requests_pathname_prefix="/aspect/",
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Financial Report"
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/wun":
        return wun.create_layout(app)
    elif pathname == "/two":
        return two.create_layout(app)
    elif pathname == "/full-view":
        return (
            overview.create_layout(app),
            wun.create_layout(app),
            two.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    server = FastAPI()
    server.mount("/aspect/", WSGIMiddleware(app.server))
    uvicorn.run(server, port=8765, headers=[("server", "htsrv/3.1415")])

    # app.run_server(debug=False, port=8765)
