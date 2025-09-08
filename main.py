import streamlit as st
import numpy as np
from predict import predict_digit
from ScreenGame import run_drawer
import matplotlib.pyplot as plt

# Simple page setup
st.title("Digit Recognition App")
st.write("Draw a digit and get a prediction!")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Drawing")
    
    if st.button("Open Drawing Canvas", type="primary"):
        st.write("Drawing canvas will open in a new window...")
        st.write("Close the pygame window when you're done drawing!")
        
        # This will open your pygame drawing interface
        try:
            grid = run_drawer()
            st.session_state.grid = grid
            st.success("Drawing captured!")
        except Exception as e:
            st.error(f"Error with drawing interface: {e}")

with col2:
    st.subheader("Prediction")
    
    if 'grid' in st.session_state:
        grid = st.session_state.grid
        # Show the drawing
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.imshow(grid, cmap='gray')
        ax.set_title("Your Drawing")
        ax.axis('off')
        st.pyplot(fig)
        
        # Make prediction
        try:
            prediction = predict_digit(grid)
            st.write(f"## Predicted Digit: **{prediction}**")
        except Exception as e:
            st.error(f"Prediction error: {e}")
            
    else:
        st.write("Draw something first!")

# Instructions
st.write("---")
st.write("**Instructions:**")
st.write("1. Click 'Open Drawing Canvas'")
st.write("2. Draw a digit in the pygame window")
st.write("3. Press ENTER when done")
st.write("4. See your prediction here!")