import streamlit as st

def app():
    
    st.markdown(
        """
        <style>
        .login-page-title {
            color:#F08080;
            text-align: center;
        }
        .select-box, .text-input, .button {
            width: 100%;
            margin-top: 10px;
        }
        .error-message {
            color: red;
        }
        .success-message {
            color: green;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="login-page-title"></h1>', unsafe_allow_html=True)
    choice = st.selectbox('Login/Signup', ['Login', 'Signup'], key='select-box', help='Choose Login or Signup')
    
    if choice == 'Login':
        email = st.text_input('Email Address', key='email-input', help='Enter your email address')
        password = st.text_input('Password', type='password', key='password-input', help='Enter your password')
        
        if st.button('Login', key='login-button'):
            if len(password) < 8:
                st.markdown('<p class="error-message">Password must be at least 8 characters long</p>', unsafe_allow_html=True)
            elif len(password) > 8:
                st.markdown('<p class="error-message">Password must not be more than 8 characters long</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="success-message">Logged in successfully</p>', unsafe_allow_html=True)

    elif choice == 'Signup':
        new_user = st.text_input('Email Address', key='new-email-input', help='Enter your new email address')
        new_password = st.text_input('New Password', type='password', key='new-password-input', help='Enter your new password')
        
        if st.button('Signup', key='signup-button'):
            if len(new_password) < 8:
                st.markdown('<p class="error-message">Password must be at least 8 characters long</p>', unsafe_allow_html=True)
            elif len(new_password) > 8:
                st.markdown('<p class="error-message">Password must not be more than 8 characters long</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="success-message">Account created successfully</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
