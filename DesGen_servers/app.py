from dash import Dash, dcc, html, Input, Output, State
import requests 
from TextFilesMod import TextFilesModClass

ORCHESTRATOR_URL = "http://localhost:8071" #url to the orchestrator
# Initialize Dash app
app = Dash(__name__)
# Layout of the html
app.layout = html.Div(
    [
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
            [
                html.H1("Make their story come to life!"),
                html.P("AI Generated Descriptions for your Furry Friends"),
                html.Div(
                    [
                        #part to receive inputs from the users
                        #type
                        html.Label("Type of Pet"),
                        dcc.Dropdown(
                            id="pet-type",
                            options=[{"label": "Dog", "value": "Dog"}, {"label": "Cat", "value": "Cat"}],
                            value="Dog",
                            style={"width": "100%", "height": "40px","margin-bottom":"5px"},
                        ),
                        #breed
                        html.Label("Breed"),
                        dcc.Input(id="breed", type="text", placeholder="Enter breed here", style={"width": "100%", "height": "40px","margin-bottom":"5px"}),
                        #pet's name
                        html.Label("Your Pet's Name"),
                        dcc.Input(id="pet-name", type="text", placeholder="Enter name here", style={"width": "100%", "height": "40px","margin-bottom":"5px"}),
                        #sex
                        html.Label("Sex"),
                        dcc.Dropdown(
                            id="sex",
                            options=[{"label": "Male", "value": "Male"}, {"label": "Female", "value": "Female"}],
                            value="Male",
                            style={"width": "100%", "height": "40px","margin-bottom":"5px"},
                        ),
                        #age
                        html.Label("Age"),
                        dcc.Input(id="age", type="number", placeholder="Enter age here", style={"width": "100%", "height": "40px","margin-bottom":"5px"}),
                        #color
                        html.Label("Color"),
                        dcc.Input(id="color", type="text", placeholder="Enter color here", style={"width": "100%", "height": "40px","margin-bottom":"5px"}),
                        #vaccination
                        html.Label("Vaccination"),
                        dcc.Dropdown(
                            id="vaccination",
                            options=[
                                {"label": "Up to Date", "value": "Up to Date"},
                                {"label": "Not Up to Date", "value": "Not Up to Date"},
                            ],
                            value="Up to Date",
                            style={"width": "100%", "height": "40px","margin-bottom":"5px"},
                        ),
                        #generate description part
                        html.Button("Generate Description", id="generate-button", style={"padding": "10px 20px", "fontSize": "1em", "backgroundColor": "#f48cb7", "border": "none", "borderRadius": "20px", "cursor": "pointer",}),
                        html.Div(
                            id="description-output",
                            style={
                                "background-color": "#ffe6e6",
                                "border": "2px solid #ff9999",
                                "padding": "10px",
                                "border-radius": "10px",
                                "margin-top": "10px",
                            },
                        ),
                        html.Div(
                            [
                                #edit description
                                html.Label("Edit Generated Description"),
                                dcc.Textarea(
                                    id="edit-description",
                                    style={
                                        "width": "90%",
                                        "height": "100px",
                                        "margin-top": "10px",
                                        "padding": "10px",
                                        "border": "1px solid #ccc",
                                        "border-radius": "5px",
                                    },
                                ),
                                html.Button(
                                    #update the edited description
                                    "Update Description",
                                    id="update-description-button",
                                    style={"padding": "10px 20px", "fontSize": "1em", "backgroundColor": "#f48cb7", "border": "none", "borderRadius": "20px","cursor": "pointer",},
                                ),
                            ],
                            style={"margin-top": "20px"},
                        ),
                        html.Div(
                            #this part is to save the updated description and go the next stage of uploading
                            id="final-description-output",
                            style={
                                "margin-top": "20px",
                                "padding": "10px",
                                "background-color": "#e6ffe6",
                                "border": "2px solid #99ff99",
                                "border-radius": "10px",
                            },
                        ),
                        html.Button(
                            #save description
                                    "Save Description",
                                    id="save-description",
                                    style={"margin-top" :"10px","padding": "10px 20px", "fontSize": "1em", "backgroundColor": "#f48cb7", "border": "none", "borderRadius": "20px","cursor": "pointer",},
                        ),
                        html.P(
                            #massage of successful saving
                            id="submit-text",
                            children=(
                                ""
                            ),
                        ),
                        html.A(
                            #next page button
                            "Next",
                            id="next-page",
                            href="http://localhost:8073/",        
                            style={"margin-top" :"10px","padding": "10px 20px", "fontSize": "1em", "backgroundColor": "#f48cb7", "border": "none", "borderRadius": "20px","cursor": "pointer","text-decoration":"none",},
                        ),
                    ],
                    style={
                        "background-color": "white",
                        "border-radius": "10px",
                        "padding": "20px",
                        "box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)",
                        "max-width": "600px",
                        "margin": "0 auto",
                        "display": "flex",
                        "flex-direction": "column",  # Ensures vertical stacking
                        "align-items": "stretch",   # Aligns all elements
                    },
                ),
            ],
            style={"padding": "20px", "text-align": "center"},
        ),
        
     
    ]
)
# Callback to handle generated description. It will update the part of description after the description is generated
@app.callback(
    Output("description-output", "children"),
    Output("edit-description", "value"),
    Input("generate-button", "n_clicks"),
    [
        State("pet-type", "value"),
        State("breed", "value"),
        State("pet-name", "value"),
        State("sex", "value"),
        State("age", "value"),
        State("color", "value"),
        State("vaccination", "value"),
    ],
)
def generate_description(n_clicks, pet_type, breed, pet_name, sex, age, color, vaccination):
    #this function receives the input from the pet's details and give to the orchestrator and then AI to make a description based on this information
    if not n_clicks:
        return "", "" #do not update the description part yet
    #first it sends the info to the orchestrator then to the description generator model server
    response = requests.post(
        f"{ORCHESTRATOR_URL}/generate",
        json={
            "pet_details": {"pet_type": pet_type, "breed": breed, "pet_name": pet_name, "sex": sex, "age": age, "color": color, "vaccination": vaccination}
        }
    )
    #ERROR HANDLING
    if response.status_code == 200:
        description = response.json().get("description", "Error in response")
        return description, description
    else:
        return "Error generating description.", ""
        
# part of the code that uses callbak to edit and update the description generated
@app.callback(
    Output("final-description-output", "children"),
    Input("update-description-button", "n_clicks"),
    State("edit-description", "value"),
)
def update_description(n_clicks, edited_text):
    if not n_clicks or not edited_text:
        return ""
    return f"Final Description: {edited_text}"
    
#part of the code to save the updated description
@app.callback(
    Output("submit-text", "children"),
    Input("save-description", "n_clicks"),
    [State("pet-name", "value"),
    State("final-description-output", "children"),],
)
def submit_description(n_clicks,pet_name,text):
    if not n_clicks or not text:
        return ""
    text=text.replace("Final Description: ","")
    text=text.replace("\n","")
    pet_name=pet_name.upper()
    text=pet_name+"\n"+text
    TextFileEdit=TextFilesModClass()
    valid_path="DescGenerHist.txt"
    #TextFileEdit.OpenTextFile(valid_path)
    TextFileEdit.WriteTextFile(text,valid_path)
    return "description submitted!"
    
if __name__ == "__main__":
    app.run_server(debug=True, port=8070)
