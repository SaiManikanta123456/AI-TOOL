
import base64
import streamlit as st
import subprocess

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
# add_bg_from_local(r"D:\python\Face1\TECH-CHAT\Untitled design.png")


st.markdown("""
<style>
.chat{
font-size:20px !important;
font-family:sans-serif;
color:orange;
font-weight:bold;
}
.main1{
font-size:40px !important;
font-family:sans-serif;
color:red;
text-align:center;
font-weight:bold;
}
.c1{
font-size:20px !important;
font-family:sans-serif;
font-weight:bold;
}
.c2{
font-size:16px !important;
font-family:sans-serif;
color:grey;
}
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<p class="main1">AI STUDY TOOL</p>',unsafe_allow_html=True)

    options = ["Chat Bot 🤖", "URL Explorer🕸️", "PDF's FRIEND📃"]

    # Add custom CSS to create vertical lines across the entire page
    st.markdown(
        """
        <style>
        .css-1v5m7av {
            border-right: 1px solid #ccc;
            padding-right: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display options and descriptions
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<p class="chat">CHATIFY</p>',unsafe_allow_html=True)
        if st.button(options[0]):
            pass
            subprocess.run(["streamlit", "run", "chat.py"])
        st.markdown('<p class="c1">Chat with our friendly chat bot.</p>',unsafe_allow_html=True)

        st.write('<p class="c2">Select the subjects from dropdown</p>',unsafe_allow_html=True)
        st.write('<p class="c2">Ask questions and Get the answers🥳🎉</p>', unsafe_allow_html=True)


    with col2:
        st.markdown('<p class="chat">WEBIFY</p>', unsafe_allow_html=True)
        if st.button(options[1]):
            pass
            subprocess.run(["streamlit", "run", "URL.py"])
        st.markdown('<p class="c1">Explore URLs</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Paste the URLs that are tedious to read</p>', unsafe_allow_html=True)
        st.write('<p class="c2">click 👆 on Process URLs</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Ask questions and Get the answers🥳🎉</p>', unsafe_allow_html=True)

    with col3:
        st.markdown('<p class="chat">DOCIFY</p>', unsafe_allow_html=True)
        if st.button(options[2]):
            pass
            subprocess.run(["streamlit", "run", "pdf.py"])
        st.markdown('<p class="c1">PDF utility</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Give us the heavy PDFs🤯</p>', unsafe_allow_html=True)
        st.write('<p class="c2"> Give a simple click 👆 to Process them</p>', unsafe_allow_html=True)
        st.write('<p class="c2">Ask questions and Get the answers🥳🎉</p>', unsafe_allow_html=True)



if __name__ == "__main__":
    main()


