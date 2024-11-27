from dash import Dash, html, dcc, Input, Output, State
from flask import Flask, request, jsonify
import requests
# Initialize Dash app
app = Dash(__name__)

# Layout of the html
app.layout = html.Div(
    style={
        "margin": "0",
        "fontFamily": "'Arial', sans-serif",
        "backgroundColor": "#e7f2f4",
        "color": "#ffffff",
        "textAlign": "center",
    },
    children=[
        #Header part of the website
        html.Header(
            [
                html.H1("Marley&Me", style={"color": "white", "margin": 0}),
                html.Nav(
                    [
                        html.A("About Us", href="#", style={"color": "white", "margin": "0 10px"}),
                        html.A("Contact Us", href="#", style={"color": "white", "margin": "0 10px"}),
                        html.A("My Animals", href="#", style={"color": "white", "margin": "0 10px"}),
                    ],
                    style={"text-align": "right"},
                ),
            ],
            style={
                "background-color": "black",
                "color": "white",
                "padding": "10px 20px",
                "display": "flex",
                "justify-content": "space-between",
                "align-items": "center",
            },
        ),
        # Main part of the website
        html.Div(
            style={
                "backgroundColor": "#9d8189",
                "margin": "20px auto",
                "padding": "20px",
                "width": "90%",
                "maxWidth": "600px",
                "borderRadius": "15px",
                "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            },
            children=[
                
                html.Div(
                    style={"display": "flex", "justifyContent": "center", "gap": "15px", "marginBottom": "20px"},
                    children=[
                    html.Img(
                            src="assets/img/Artemis1.jpg",
                            alt="Baxter Image 1",
                            style={"width": "45%", "borderRadius": "10px"},
                        ),
                    html.Img(
                            src="assets/img/Artemis2.jpg",
                            alt="Baxter Image 2",
                            style={"width": "45%", "borderRadius": "10px"},
                        ),
                    ],
                ),
                # Name of the pet
                html.Div(
                    "Artemis",
                    style={"fontSize": "2em", "fontWeight": "bold", "margin": "10px 0"},
                ),
                # Description to be translated by the NMT model
                html.Div(
                    id="description-container",
                    children=[
                        html.P(
                            id="description-p1",
                            children=(
                                "She is a captivating Turkish Angora with a unique charm. "
                                "She is 3 years old. Her mesmerizing eyes, one a deep blue and the other a vibrant green, "
                                "draw you in. With her long, silky fur and elegant posture, she exudes a sense of grace and mystery."
                            ),
                        ),
                        html.P(
                            id="description-p2",
                            children=(
                                "Artemis is a curious and playful cat, always eager to explore her surroundings and engage in interactive play. "
                                "She’s a true gem, adding a touch of magic to any home."
                            ),
                        ),
                    ],
                ),
                html.Div(
                    style={"marginTop": "20px", "display": "flex", "justifyContent": "center", "gap": "50px"},
                    children=[
                        html.Button(
                            "Adopt Now!",
                            style={
                                "padding": "10px 20px",
                                "fontSize": "1em",
                                "backgroundColor": "#f48cb7",
                                "border": "none",
                                "borderRadius": "20px",
                                "cursor": "pointer",
                            },
                            id="adopt-now",
                        ),
                        # Translate button
                        html.Button(
                            "Nederlands",
                            style={
                                "padding": "10px 20px",
                                "fontSize": "1em",
                                "backgroundColor": "#f48cb7",
                                "border": "none",
                                "borderRadius": "20px",
                                "cursor": "pointer",
                            },
                            id="translate-button",
                        ),
                        
                    ],
                ),
            ],
        ),
    ],
)

# Callback to handle translation. It will update the description after the description is translated and then replace the english description with the dutch description
@app.callback(
    [Output("description-p1", "children"), Output("description-p2", "children")],
    [Input("translate-button", "n_clicks")],
    [State("description-p1", "children"), State("description-p2", "children")],
)
def translate_text(n_clicks, text1, text2):
    
    # This function will return the translation and update the description part of the website
    if not n_clicks:
        return text1, text2  # No translation yet, so do not update the description part

    # Function to send text for translation, first it sends the description to the orchestrator then to the NMT model server
    def translate(text):
        response = requests.post("http://127.0.0.1:8051/translate", json={"text": text})
        if response.status_code == 200:
            return response.json().get("translated_text", text)
        else:
            return "Error: Translation failed"

    # Translate both paragraphs, only for testing whether NMT can handle to requests, can only send one long paragraph as well 
    translated_text1 = translate(text1)
    translated_text2 = translate(text2)
    #return the translation
    return translated_text1, translated_text2


if __name__ == "__main__":
    app.run_server(debug=True,port=8050)