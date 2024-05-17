import streamlit as st
from streamlit_extras.app_logo import add_logo  # Import the app_logo function

#Use the app_logo function to display the logo
add_logo("images/liquid_logo.png", height=65)
st.sidebar.image("images/small_logo.png",caption="Developed and Maintained by Roy Krishnan")
st.sidebar.image("images/HVG_logo.png",caption= "Made to the specifications of the 2024 Hornets Venom Gaming Team")


# Rest of your Streamlit code
st.title("The One Man Front Office | OMFO")
st.subheader("By: Roy Krishnan")
st.markdown("**Liquid Pro Am** [here](https://twitter.com/LiquidProAm_) | **Roy's personal X Account** [here](https://twitter.com/RoyKrishnan_) | **Roy's 2K Esports X (rarely checked these days)** [here](https://twitter.com/RoyKhris)") 
st.subheader('', divider='grey')

st.write("Where we'll release news, new releases, and updates: ")
st.link_button('OMFO X Account', 'https://twitter.com/1ManFrontOffice')

with st.expander("**What is OMFO?**"):
    st.write("**OMFO is a 2K League basketball player box-score score visualization system that allows teams to see real time rendered visualizations to track player progress and value**.") 
with st.expander("**Accuracy**"):
    st.write('OMFO is run off of source data publicly available from the 2K League. All scrapes and sorts come from what is issued, posted, and circulated by the league.')
with st.expander("App Limitations "):
    st.write("The more data, the less the limitations. The more information we provide this application, the better it will get at forecasting.")
with st.expander("**Premium Model**"):
    st.write("""
            Welcome to the Season 7 Premium Model - Hornets Venom GT! If you have any questions at all, feel free to contact a member of our team.""")
with st. expander("**Acknowledgements:**"):
    st.write("""
            Tanner Mannett - idea for player radar charts, as well as the first rendition of PG radar charts. 
             Yey Not Gaming - Helping out with data collection and marketing 
            """)
