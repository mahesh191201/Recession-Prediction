import pickle
import streamlit as st

model = pickle.load(open('rf.pkl', 'rb'))

st.title("AI for Economics: Recession prediction using ML")

bg = """

<style>
[data-testid="stAppViewContainer"] {
 
background-image: url("https://discover.rbcroyalbank.com/wp-content/uploads/Untitled-design-2023-07-31T120240.836.jpg");
background-size: cover;
}

<style/>

"""

st.markdown(bg, unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    year = st.text_input("Enter the year")

with col2:
    quarter = st.text_input("Enter the Quarter")

with col1:
    gdp = st.text_input("Enter the GDP growth")

with col2:
    inf = st.text_input("Enter the Inflation")

with col1:
    ip = st.text_input("Enter the Industrial Production")

with col2:
    jm = st.text_input("Enter the Jobs added")

recession = ""

if st.button("Recession Prediction"):
    try:
        year = int(year)
        quarter = int(quarter)
        gdp = float(gdp)
        inf = float(inf)
        ip = float(ip)
        jm = int(jm)

        prediction = model.predict([[gdp, inf, ip, jm]])

        if prediction[0] == 0:
            recession = "No Recession"
        else:
            recession = "Recession ahead"

    except ValueError as e:
        st.error(f"Invalid input: {e}")


st.success(recession)
