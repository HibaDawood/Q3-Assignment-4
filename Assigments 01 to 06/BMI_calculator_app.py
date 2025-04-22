import streamlit as st
import pandas as pd

# Set page title and configuration
st.set_page_config(page_title="BMI Calculator", layout="centered")

# Add a title and description
st.title("BMI Calculator")
st.markdown("Calculate your Body Mass Index (BMI) and check your weight status.")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    # Weight input
    weight = st.number_input("Enter your weight", min_value=1.0, max_value=500.0, value=70.0, step=0.1)
    weight_unit = st.selectbox("Weight unit", ["kg", "lbs"])

with col2:
    # Height input
    height = st.number_input("Enter your height", min_value=1.0, max_value=300.0, value=170.0, step=0.1)
    height_unit = st.selectbox("Height unit", ["cm", "m", "ft"])

# Convert weight to kg if in lbs
if weight_unit == "lbs":
    weight = weight * 0.453592

# Convert height to meters
if height_unit == "cm":
    height = height / 100
elif height_unit == "ft":
    height = height * 0.3048

# Calculate BMI when button is pressed
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "green"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"
    
    # Display results
    st.header(f"Your BMI: {bmi:.2f}")
    st.markdown(f"<h3 style='color:{color};'>Category: {category}</h3>", unsafe_allow_html=True)
    
    # Create a visual representation using progress bars instead of matplotlib
    st.subheader("BMI Scale:")
    
    # Create a container for the BMI scale
    scale_col1, scale_col2, scale_col3, scale_col4 = st.columns(4)
    
    with scale_col1:
        st.markdown("<div style='background-color:blue; padding:10px; border-radius:5px; text-align:center; color:white;'>Underweight<br>&lt;18.5</div>", unsafe_allow_html=True)
        if bmi < 18.5:
            st.markdown("**← Your BMI**")
    
    with scale_col2:
        st.markdown("<div style='background-color:green; padding:10px; border-radius:5px; text-align:center; color:white;'>Normal<br>18.5-24.9</div>", unsafe_allow_html=True)
        if 18.5 <= bmi < 25:
            st.markdown("**← Your BMI**")
    
    with scale_col3:
        st.markdown("<div style='background-color:orange; padding:10px; border-radius:5px; text-align:center; color:white;'>Overweight<br>25-29.9</div>", unsafe_allow_html=True)
        if 25 <= bmi < 30:
            st.markdown("**← Your BMI**")
    
    with scale_col4:
        st.markdown("<div style='background-color:red; padding:10px; border-radius:5px; text-align:center; color:white;'>Obese<br>≥30</div>", unsafe_allow_html=True)
        if bmi >= 30:
            st.markdown("**← Your BMI**")
    
    # Use Streamlit's built-in progress bar to show where on the scale the BMI falls
    st.subheader("Your BMI on the scale:")
    
    # Normalize BMI to a 0-100 scale for the progress bar (capped between 10 and 40)
    normalized_bmi = min(max((bmi - 10) * 100 / 30, 0), 100)
    st.progress(normalized_bmi / 100)
    
    # BMI information
    st.subheader("BMI Categories:")
    bmi_data = {
        "Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
        "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "≥ 30"]
    }
    st.table(pd.DataFrame(bmi_data))
    
    # Health tips based on category
    st.subheader("Health Tips:")
    if category == "Underweight":
        st.info("Consider consulting with a healthcare provider about healthy ways to gain weight. Focus on nutrient-dense foods and strength training exercises.")
    elif category == "Normal weight":
        st.success("Maintain your healthy weight with regular physical activity and a balanced diet.")
    elif category == "Overweight":
        st.warning("Consider making lifestyle changes such as increasing physical activity and improving dietary habits. Small changes can make a big difference.")
    else:
        st.error("It's recommended to consult with healthcare providers about weight management strategies. Focus on gradual, sustainable changes to diet and activity levels.")

# Add disclaimer
st.markdown("---")
st.caption("Disclaimer: BMI is a screening tool and not a diagnostic of body fatness or health. Consult with healthcare professionals for proper health assessment.")

# For demonstration purposes, let's simulate a BMI calculation
print("Simulating BMI calculation with sample values:")
sample_weight_kg = 70
sample_height_m = 1.75
sample_bmi = sample_weight_kg / (sample_height_m ** 2)
print(f"Sample weight: {sample_weight_kg} kg")
print(f"Sample height: {sample_height_m} m")
print(f"Calculated BMI: {sample_bmi:.2f}")

# Determine BMI category for the sample
if sample_bmi < 18.5:
    sample_category = "Underweight"
elif 18.5 <= sample_bmi < 25:
    sample_category = "Normal weight"
elif 25 <= sample_bmi < 30:
    sample_category = "Overweight"
else:
    sample_category = "Obese"

print(f"BMI Category: {sample_category}")