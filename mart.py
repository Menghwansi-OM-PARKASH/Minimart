import streamlit as st
# Welcome My MiniMart
st.title("Welcome to My MiniMart")
st.write('''01. Pizza       = 350\n
02. Cold Drink  = 150\n
03. Burgar      = 120''')

# --- Initialize session state for amount ---
if 'amount' not in st.session_state:
    st.session_state['amount'] = 0

# --- Take Order ---
order = st.text_input("Sir/Mam, place your 1st order please:").lower()

# --- Process Order ---
if order == 'pizza':
    st.write("Sir, your order is placed.")
    st.session_state['amount'] += 350

elif order == 'cold drink':
    st.write("Sir, your order is placed.")
    st.session_state['amount'] += 150

elif order == 'burger':
    st.write("Sir, your order is placed.")
    st.session_state['amount'] += 120

elif order != "":
    st.write("Sorry, we don't have that item.")

# --- Ask for More Orders ---

n_order =st.text_input("Do you want to add something else, Sir/Mam. YES/NO:\t").lower()
if n_order == 'no':
    st.write(f"💰 Total Amount: Rs. {st.session_state['amount']}")
    st.write("Thanks for choosing MiniMart. Enjoy your meal!")

# --- 2nd Order --- if (yes)
if n_order == 'yes':
    order = st.text_input("Sir/Mam, place your 2nd order please:\t").lower()
    if order == 'pizza':
        st.write("Sir, your order is placed.")
        st.session_state['amount'] += 350
       
    elif order == 'cold drink':
        st.write("Sir, your order is placed.")
        st.session_state['amount'] += 150
        
    elif order == 'burgar':
        st.write("Sir, your order is placed.")
        st.session_state['amount'] += 120
        
    else:
        st.write("Sorry, we don't have that item.") 
        
    n_order =input("Do you want to add something else, Sir/Mam. YES/NO:\t").lower()
    if n_order == 'no':
        # --- Show Total Amount ---
      st.write(f"💰 Total Amount: Rs. {st.session_state['amount']}")
      st.write("Thanks for choosing MiniMart. Enjoy your meal!")
        
        
# 3rd order
if n_order == 'yes':
    order = st.text_input("Sir/Mam, place your 3rd order please:\t").lower()
    if order == 'pizza':
        st.write("Sir, your order is placed.")
        st.session_state['amount'] += 350
    elif order == 'cold drink':
        st.write("Sir, your order is placed.")
        st.session_state['amount'] += 150
    elif order == 'burgar':
        st.write("Sir, your order is placed.")
        st.session_state['amount'] += 120
    else:
        st.write("Sorry, we don't have that item.")

# No more chances after 3rd order
# --- Show Total Amount ---
st.write(f"💰 Total Amount: Rs. {st.session_state['amount']}")
st.write("Your Total Bill is:['amount']")
st.write("Thanks for choosing MiniMart. Enjoy your meal!")
st.write("You have reached the maximum number of orders.")
st.write("Your Total Bill is:['amount']")