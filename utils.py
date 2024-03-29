import os
from dash import dcc, html

URL_PATH_SEP = '/'
URL_BASE_PATHNAME = os.getenv('REPORT_URL_BASE', URL_PATH_SEP)
if URL_BASE_PATHNAME[-1] != URL_PATH_SEP:
    URL_BASE_PATHNAME += URL_PATH_SEP


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.A(
                        html.Img(
                            src=app.get_asset_url("example-logo.png"),
                            className="logo",
                        ),
                        href="https://example.com/home/",
                    ),
                    html.A(
                        html.Button(
                            "Something Else",
                            id="learn-more-button",
                            style={"margin-left": "-10px"},
                        ),
                        href="https://example.com/learn/",
                    ),
                    html.A(
                        html.Button("Still Different", id="learn-more-button"),
                        href="https://github.com/sthagen/example-app-report/",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Report Main Title")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href=f"{URL_BASE_PATHNAME}full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href=f"{URL_BASE_PATHNAME}overview",
                className="tab first",
            ),
            dcc.Link(
                "Details Wun",
                href=f"{URL_BASE_PATHNAME}wun",
                className="tab",
            ),
            dcc.Link(
                "Details Two",
                href=f"{URL_BASE_PATHNAME}two",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """Return a dash definition of an HTML table for a Pandas dataframe"""
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
