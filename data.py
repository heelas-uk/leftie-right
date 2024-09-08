import streamlit as st
import random as ran

st.set_page_config(
    page_title="Leftie right (YAyy)",
    page_icon="👋",
)

st.write("# Welcome to my leftie rightie game 👋")


st.markdown(
    """
    Credits to streamlit for the package 
    ### Lets get started
    """
)
st.button("Reset", type="primary")
crossroad = ran.randrange(1,4)
if st.button("# Crossroad"):
    if crossroad == 1:
        st.write("# TURN LEFT")
        st.image("left.png", caption="A turn left arrow")
        crossroad = ran.randrange(1,4)
    elif crossroad == 2:
        st.write("# STRAIGHT AHEAD")
        st.image("forward.png", caption="An arrow pointing straight forward")
        crossroad = ran.randrange(1,4)
    elif crossroad == 3:
        st.write("# TURN RIGHT")
        st.image("right.png", caption="A right turn arrow")
        crossroad = ran.randrange(1,4)
    else:
        st.write("You have broke the time space contium sorry...  try reloading")
        crossroad = ran.randrange(1,4)
turn = ran.randrange(1,3)
if st.button("# Left turn"):
    if turn == 1:
        st.write("# TURN LEFT")
        st.image("left.png", caption="A turn left arrow")
        turn = ran.randrange(1,3)
    elif turn == 2:
        st.write("# STRAIGHT AHEAD")
        st.image("forward.png", caption="An arrow pointing straight forward")
        turn = ran.randrange(1,3)
    else:
        st.write("You have broke the time space contium sorry...  try reloading")
        turn = ran.randrange(1,3)

turn = ran.randrange(1,3)
if st.button("# Right turn"):
    if turn == 1:
        st.write("# TURN RIGHT")
        st.image("right.png", caption="A turn right arrow")
        turn = ran.randrange(1,3)
    elif turn == 2:
        st.write("# STRAIGHT AHEAD")
        st.image("forward.png", caption="An arrow pointing straight forward")
        turn = ran.randrange(1,3)
    else:
        st.write("You have broke the time space contium sorry...  try reloading")
        turn = ran.randrange(1,3) 

turn = ran.randrange(1,3)
if st.button("# Two exit roundabout"):
    if turn == 1:
        st.write("# Staight over the roundabout")
        st.image("forward.png", caption="Staight through the roundabout")
        turn = ran.randrange(1,3)
    elif turn == 2:
        st.write("# Go around the roundabout")
        st.image("uturn.png", caption="A symbol shoowing a u-turn")
        turn = ran.randrange(1,3)
    else:
        st.write("You have broke the time space contium sorry...  try reloading")
        turn = ran.randrange(1,3) 

crossroad = ran.randrange(1,4)
if st.button("# Three exit roundabout"):
    if crossroad == 1:
        st.write("# TAKE THE FIRST EXIT")
        st.image("leftround.png", caption="Exit left at the roundabout")
        crossroad = ran.randrange(1,4)
    elif crossroad == 2:
        st.write("# TAKE THE SECOND EXIT")
        st.image("forward.png", caption="An arrow pointing straight forward")
        crossroad = ran.randrange(1,4)
    elif crossroad == 3:
        st.write("# GO AROUND THE ROUNDABOUT")
        st.image("uturn.png", caption="A uturn symbol")
        crossroad = ran.randrange(1,4)
    else:
        st.write("You have broke the time space contium sorry...  try reloading")
        crossroad = ran.randrange(1,4)

roundIV = ran.randrange(1,5)
if st.button("# Four exit roundabout"):
    if roundIV == 1:
        st.write("# TAKE THE FIRST EXIT")
        st.image("leftround.png", caption="Exit left at the roundabout")
        roundIV = ran.randrange(1,5)
    elif roundIV == 2:
        st.write("# TAKE THE SECOND EXIT")
        st.image("forward.png", caption="An arrow pointing straight forward")
        roundIV = ran.randrange(1,5)
    elif roundIV == 3:
        st.write("# GO AROUND THE ROUNDABOUT")
        st.image("uturn.png", caption="A uturn symbol")
        roundIV = ran.randrange(1,5)
    elif roundIV == 4:
        st.write("# TAKE THE THIRD EXIT")
        st.image("rightround.png", caption="Take the third exit")
    else:
        st.write("You have broke the time space contium sorry...  try reloading")
        roundIV = ran.randrange(1,5)

roundV = ran.randrange(1,6)
if st.button("# Five exit roundabout"):
    if roundV == 1:
        st.write("# TAKE THE FIRST EXIT")
        st.image("leftround.png", caption="Exit left at the roundabout")
        roundV = ran.randrange(1,6)
    elif roundV == 2:
        st.write("# TAKE THE SECOND EXIT")
        st.image("forward.png", caption="An arrow pointing straight forward")
        roundV = ran.randrange(1,6)
    elif roundV == 3:
        st.write("# GO AROUND THE ROUNDABOUT")
        st.image("uturn.png", caption="A uturn symbol")
        roundV = ran.randrange(1,6)
    elif roundV == 4:
        st.write("# TAKE THE THIRD EXIT")
        st.image("rightround.png", caption="Take the third exit")
    elif roundV == 5:
        st.write("# TAKE THE FOURTH EXIT")
        st.image("fourth.png", caption="well read the big title duh...")
    else:
        st.write("You have broke the time space contium sorry...  try reloading")
        roundV = ran.randrange(1,6)
background_color = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-color: #000000;
}
</style>
"""

st.markdown(background_color, unsafe_allow_html=True)







st.write("Click or tap above to get started")