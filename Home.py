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
with st.expander("**Objective Team Research - Hornets Venom GT**"):
    st.write("""
    HORNETS VENOM GT
    Most Common Lineup

    MOOCH
    3PT Shot Hunter
    PG
    
    TREY DOLLAZ 
    Chess
    Recent trade for Chess will require more data before we can make assumptions about him at this position. 
    
    FLUKELOCK
    2 Way Spot Up Threat
    LOCK
    
    BIG SAINT
    2 Way Spot Up Glass Cleaner
    PF
    
    CROWN
    Inside The Arc Maestro
    C


    Current standing
    Currently sitting with 20 points total (tied with both Celtics and Magic Gaming).  Two wins away from the playoff picture. Turn tournament still to kick off next week. 
    
    Offensively
    The Hornets deploy an unconventional offensive scheme, leaning on an outside center build to spark their pick-and-roll game. Their offense thrives on constant motion, off-ball cuts, and team-wide involvement, using the traditional high screen setups for a more dynamic approach tailored to individual strengths.
    
    High efficiency play out of the center and power forward position, Crown and Big Saint. With Saint currently sitting at Top 5 in Helio Grade at the PF spot.  The backcourt has a talented duo but seeing some inconsistency out of their play in the first tournament, particularly with their scoring. Currently bottom half in scoring amongst PGs shooting 44% from the field and 43% from three.
    
    Flukelock currently has the highest field goal percentage amongst all lockdowns with 82.6% in five games played. Also, leads locks in 3PT% with 6 or more threes taken on top of averaging over 10 points a game.   
    
    When looking at the offensive impact at the shooting guard, Trey seems to score near the bottom of the pact.  A few names to where he shares this space with are the likes of HarryVZN, BRich, and Reizey. This means he doesn’t spend a lot of time with the ball and needs to convert at a higher margin like his counterparts we see from some of the better teams.  This will have to start creating better routes to get open on the break and some quick hits to get Mooch building confidence and gaining takeover earlier in games.
    
    With Mooch and (now Chess) able to get something going early in the game, this will give the team the edge on being more consistent. Doing this will continue to open up the opportunities for easier buckets for the rest of the team.  Don’t stop involving Saint in the offense with the ‘top of the key’ stops up the court and letting him work in the pick and roll.  Also the defense will begin to overcompensate on the guards, freeing up looks for Fluke and Crown as well  
    
    Defensively
    Looking at the defensive side of the coin, starting with how most stops occur and that’s with a defensive rebound.  Crown currently is 2nd in the east, as of today, in total rebound. Right behind Colt. All the while, Saint is 4th amongst PFs in defensive rebounds in the east.  
    
    Taking a glance at overall defensive rotations, it seems like the whole team knows where they should be once something is called out, but the major takeaway from some of the closer games is that there may be some slip ups late in shot clocks.  In particular, late looks at the hash for a dex or off-ball screen.  Also there were times, like in the matchup vs the Heat, where they took advantage of the size difference with Mooch.  They did this by using off-ball action as a decoy, thus getting a bigger player with finishing ability all alone in the paint with a point guard.
    
    With being a bit average team at getting stops through steals, it's the lapses in communication late in clocks where there seems to be one, maybe two players talking (going off what’s seen on broadcast), is going to result in frustration and forces the team to work out of half court. 
    
    Conclusion
    As Hornets Gaming navigates the twists and turns of the season, finding consistency on both ends of the floor will be key to their success. With adjustments to offensive execution and a sharper focus on defensive communication, the team can unlock their full potential and make a strong push for playoff contention.""")
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
