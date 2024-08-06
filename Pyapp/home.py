import streamlit as st
import streamlit.components.v1 as components

def app():
    # Define the HTML with CSS
    html_code = """
    <html>
    <head>
        <style>
            .custom-title {
                color: #FFFACD;
                font-size: 36px;
                text-align: center;
                margin-bottom: 20px;
            }
            .custom-description {
                color: #F0F8FF;
                font-size: 18px;
                text-align: center;
                margin: 0 auto;
                max-width: 600px;
                line-height: 1.5;
            }
        </style>
    </head>
    <body>
        <div class="custom-title">Welcome to the Login Page</div>
        <div class="custom-description">
            The login page allows a user to access a website or web application by entering their username and password or by authenticating with a social network login. In addition, the page allows you to enter both authorized users and those who first visited the site and need to register.
        </div>
    </body>
    </html>
    """

    # Render the HTML with CSS
    components.html(html_code, height=400)
