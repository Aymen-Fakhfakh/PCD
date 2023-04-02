import streamlit as st
import sqlite3

conn = sqlite3.connect("user_data.db")
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY,
              first_name TEXT,
              last_name TEXT,
              email TEXT,
              username TEXT,
              password TEXT)''')

def main():
    st.set_page_config(page_title="User Information Form")
    st.title("User Information Form")
    
    # Get user information
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    verify_password = st.text_input("Verify Password", type="password")

    if password != verify_password:
        
        st.error("Passwords do not match. Please enter the same password again.")
    return
    if first_name == None or last_name == None:
        st.error("This field must'nt bee empty ")

    # Print user information
    if st.button("Submit"):
        c.execute("INSERT INTO users (first_name, last_name, email, username, password) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, email, username, password))
        conn.commit()
        st.success("User information saved to database.")

if __name__ == "__main__":
    main()
   




