from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import time
from TextFilesMod import TextFilesModClass
import os.path
app = Dash(__name__)
#html using dash
app.layout = html.Div(
    children=[
        # Header
        html.Header(
            style={
                "backgroundColor": "#000",
                "color": "white",
                "display": "flex",
                "justifyContent": "space-between",
                "alignItems": "center",
                "padding": "15px 30px",
            },
            children=[
                html.H1(
                    "Marley&Me",
                    style={"fontFamily": "'Georgia', serif", "margin": "0"},
                ),
                html.Nav(
                    style={"display": "flex", "gap": "15px"},
                    children=[
                        html.A(
                            "Home",
                            href="homepage.html",
                            style={
                                "color": "white",
                                "textDecoration": "none",
                                "fontWeight": "bold",
                                "padding": "5px 10px",
                                "borderRadius": "5px",
                            },
                            className="active",
                        ),
                        html.A(
                            "About Us",
                            href="aboutus.html",
                            style={
                                "color": "white",
                                "textDecoration": "none",
                                "fontWeight": "bold",
                                "padding": "5px 10px",
                                "borderRadius": "5px",
                            },
                        ),
                        html.A(
                            "Contact Us",
                            href="contactus.html",
                            style={
                                "color": "white",
                                "textDecoration": "none",
                                "fontWeight": "bold",
                                "padding": "5px 10px",
                                "borderRadius": "5px",
                            },
                        ),
                        html.A(
                            "My Account",
                            href="myaccount.html",
                            style={
                                "color": "white",
                                "textDecoration": "none",
                                "fontWeight": "bold",
                                "padding": "5px 10px",
                                "borderRadius": "5px",
                            },
                        ),
                    ],
                ),
            ],
        ),
        # Main Content
        html.Div(
            style={
                "backgroundColor": "#d9c2c6",
                "margin": "20px auto",
                "padding": "20px",
                "width": "90%",
                "maxWidth": "600px",
                "borderRadius": "15px",
                "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            },
            children=[
                # Image Container
                html.Div(
                    style={
                        "display": "flex",
                        "justifyContent": "center",
                        "gap": "15px",
                        "marginBottom": "20px",
                    },
                    children=[
                        html.Img(
                            src="img/Baxter1.jpg",  # Replace with actual image URL
                            alt="Baxter Image 1",
                            style={"width": "45%", "borderRadius": "10px"},
                        ),
                        html.Img(
                            src="img/Baxter2.jpg",  # Replace with actual image URL
                            alt="Baxter Image 2",
                            style={"width": "45%", "borderRadius": "10px"},
                        ),
                    ],
                ),
                # Title
                html.Div(
                    id="pet-name",
                    style={
                        "fontSize": "2em",
                        "fontWeight": "bold",
                        "margin": "10px 0",
                    },
                    children=[]
                ),
                # Description
                html.Div(
                    children=[
                    html.P(id='dynamic-text'),
                    dcc.Interval(id='interval', interval=500),  # Check file every 2 seconds
                        ]
                ),
                # Actions
                html.Div(
                    style={
                        "marginTop": "20px",
                        "display": "flex",
                        "justifyContent": "center",
                        "gap": "20px",
                    },
                    children=[
                        html.A(
                            "Submit",
                            id="submit button",
                            href="assets/html/adminpage3.html",        
                            style={"margin-top" :"10px","padding": "10px 20px", "fontSize": "1em", "backgroundColor": "#f48cb7", "border": "none", "borderRadius": "20px","cursor": "pointer","text-decoration":"none","color":"black",},
                        ),
                    ],
                ),
            ],
        ),
    ],
)

#part to update the Name of the pet every interval based on the saved description in dataset/textfile
@app.callback(
    Output('pet-name', 'children'),
    [Input('interval', 'n_intervals')]  # Triggers every interval
)
def update_name(n_intervals):
    f = open("DescGenerHist.txt", "r")
    data=f.readlines()
    if not n_intervals or len(data)<2:
        return ""
    
    name=data[0]
    description=data[1]
    TextFileEdit=TextFilesModClass()
    return name
    
#part to update the description of the pet every interval based on the saved description in dataset/textfile
@app.callback(
    Output('dynamic-text', 'children'),
    [Input('interval', 'n_intervals')]  # Triggers every interval
)
def update_text(n_intervals):
    f = open("DescGenerHist.txt", "r")
    data=f.readlines()
    if not n_intervals or len(data)<2:
        return ""
    
    name=data[0]
    description=data[1]
    TextFileEdit=TextFilesModClass()
    return description
    
if __name__ == "__main__":
    app.run_server(debug=True, port=8073)
