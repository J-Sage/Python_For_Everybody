def calculate_grade(score):
    """
    Calculates the letter grade based on the input score.

    Args:
        score (float): The numeric score (between 0 and 1).

    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if 0.9 <= score <= 1.0:
        return "A"
    elif 0.8 <= score < 0.9:
        return "B"
    elif 0.7 <= score < 0.8:
        return "C"
    elif 0.6 <= score < 0.7:
        return "D"
    elif score < 0.6:
        return "F"
    else:
        return "Invalid Input"  # Handles scores outside the valid range

try:
    user_score = float(input("Please insert your score to receive your grade: "))
    user_grade = calculate_grade(user_score)
    print(f"Your grade is: {user_grade}")
except ValueError:
    print("Please check the value you have inserted and try again.")