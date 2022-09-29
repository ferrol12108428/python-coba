from turtle import left
import streamlit as  st

#find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ----- header section -----
st.subheader("Hi, I am Ferol :wave: ")
st.title("A data Analyst From Germany")
st.write("I am passionate abaout finding ways to use to use Python and VBA to be more efficient and effective in business setting.")
st.write("[Learn More >](https://pythonandvba.com)")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("What I do")
        st.write("##")
        st.write(
            """
            On my YouTubr channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Pyhton in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way  to use Pyhton and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "thre has to be a better way."
            
            If this sounds interesting to you, consider subscribing and turning on the notification, so you don't miss any content.
            """
        )
        st.write("[Youtube Channel >](https://youtube.com/c/CodingIsFun)")