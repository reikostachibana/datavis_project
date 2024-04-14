import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Define slide content
slides = {
    'Title Page': html.Div([
    html.H1('Exploratory Analysis of Ribosome Profiling Data', style={'textAlign': 'center'}),
    html.H2('Reiko Tachibana', style={'textAlign': 'center'}),
    html.P('Elements of Data Visualization', style={'textAlign': 'center'}),
    html.P('Spring 2024', style={'textAlign': 'center'}),
    ]),
    'Ribosome Profiling': html.Div([
        html.H1('Ribosome Profiling'),
        html.P('Content for Slide 2 goes here...'),
        html.Img(src='/wsl.localhost/Ubuntu/home/reiko/cs329e/ribosome_profiling.jpg')
    ]),
    'Goal': html.Div([
        html.H1('Slide 2'),
        html.P('Content for Slide 2 goes here...'),
    ]),
}

# Define dropdown menu options
dropdown_options = [{'label': slide, 'value': slide} for slide in slides]

# Define layout
app.layout = html.Div([
    dcc.Dropdown(
        id='slide-dropdown',
        options=dropdown_options,
        value=dropdown_options[0]['value']
    ),
    html.Div(id='slide-content')
])

# Define callback to update slide content
@app.callback(
    Output('slide-content', 'children'),
    [Input('slide-dropdown', 'value')]
)
def update_slide_content(selected_slide):
    return slides[selected_slide]

if __name__ == '__main__':
    app.run_server(debug=True)
