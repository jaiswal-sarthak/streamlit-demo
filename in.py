import streamlit as st

# Animations (no arguments allowed)
st.snow()       # ❄ Snow effect
st.balloons()   # 🎈 Balloons effect
st.spinner("Loading...")  # ⏳ Spinner effect
st.progress(50)  # 📊 Progress bar at 50

# Headings in Markdown
st.markdown("# heading 1")
st.markdown("## heading 2")
st.markdown("### heading 3")
st.markdown("#### heading 4")
st.markdown("##### heading 5")
st.markdown("###### heading 6")

# Title & text outputs
st.title("streamlit demo")
st.write("Hello from st.write()", 123, {"key": "value"})
st.markdown("*Italic* **Bold** ***bold+italic***")

# Other text elements
st.title("title example")
st.header("header example")
st.subheader("subheader example")
st.text("plain text here")

# Code block
st.code("print('Hello, Streamlit!')", language='python')
