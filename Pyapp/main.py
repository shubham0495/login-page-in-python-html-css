import streamlit as st

from streamlit_option_menu import option_menu

import form, home

st.set_page_config(
    page_title="Login Form",               
)

styles = {
    "container": {
        "padding": "5px !important"
    },
    "icon": {
        "color": "white",
        "font-size": "23px"
    }
    
}

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
        
    def run(self):  
        with st.sidebar:
            selected = option_menu(
                menu_title='Dashboard',
                options=[app['title'] for app in self.apps],
                icons=['house', 'person'],  
                styles=styles,  
                key='unique_option_menu'  
            )
        
        for app in self.apps:
            if app['title'] == selected:
                app['function']()

app = MultiApp()
app.add_app("Home", home.app)
app.add_app("Account", form.app)

if __name__ == '__main__':
    app.run()
