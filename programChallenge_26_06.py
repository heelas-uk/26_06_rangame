import requests
import math
import streamlit as st 

st.title("🎮 Alfred's Game")
st.write("Welcome to Alfred's random number game! Enter three numbers and see what fate decides for you.")

# Create input fields for the three numbers
col1, col2, col3 = st.columns(3)

with col1:
    num1 = st.number_input("Number 1", min_value=1, value=1, step=1)

with col2:
    num2 = st.number_input("Number 2", min_value=1, value=1, step=1)

with col3:
    num3 = st.number_input("Number 3", min_value=1, value=1, step=1)

# Add a play button
if st.button("🎲 Play Game!", type="primary"):
    nums = [num1, num2, num3]
    
    # Show the numbers entered
    st.write(f"Your numbers: {num1}, {num2}, {num3}")
    
    # Get a random integer from random.org between 1 and 3 (inclusive)
    with st.spinner("Getting random number from random.org..."):
        try:
            response = requests.get("https://www.random.org/integers/?num=1&min=1&max=3&col=1&base=10&format=plain&rnd=new")
            psudorand = int(response.text.strip())
        except:
            st.error("Could not connect to random.org. Using local random number.")
            import random
            psudorand = random.randint(1, 3)
    
    st.write(f"🎯 Random number drawn: {psudorand}")
    
    avg = (num1 + num2 + num3)/3
    top = max(nums)
    low = min(nums)
    
    # Display results with styling
    if psudorand == 1:
        st.success(f"🎉 Well done you win with {top*2}!")
    elif psudorand == 2:
        st.info(f"🤝 Good result all round {avg:.2f} - You get a draw!")
    else:
        st.warning(f"😅 You are pathetic with {math.floor(low/2)}")
    
    # Show some game statistics
    st.subheader("📊 Game Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Highest Number", top)
    
    with col2:
        st.metric("Average", f"{avg:.2f}")
    
    with col3:
        st.metric("Lowest Number", low)
