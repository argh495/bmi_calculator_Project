def calculate_bmi(weight, height_m):
    """
    Calculates BMI using the formula:
    BMI = weight (kg) / height² (m²)
    """
    return weight / (height_m ** 2)


def get_bmi_category(bmi):
    """
    Returns BMI category based on standard ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal Weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"
