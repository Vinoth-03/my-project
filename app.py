import streamlit as st

# App title
st.title("📐 Square Area & Perimeter Calculator")

# User input
side = st.number_input("Enter the length of one side of the square (in units):", min_value=0.0, format="%.2f")

# Calculate when button is clicked
if st.button("Calculate"):
    if side > 0:
        area = side ** 2
        perimeter = 4 * side

        st.success(f"✅ Area: {area:.2f} square units")
        st.success(f"✅ Perimeter: {perimeter:.2f} units")
    else:
        st.warning("Please enter a positive number for the side length.")

