# day01.py — First structured Python script
# Ajik Naro | AI Engineer Journey

import os
from dotenv import load_dotenv

load_dotenv()

def get_app_info():
    """Return informasi aplikasi dari environment variable."""
    app_name = os.getenv("APP_NAME", "Unknown App")
    return app_name

def calculate_average(numbers: list) -> float:
    """
    Hitung rata-rata dari list angka.
    Args:
        numbers: list berisi angka
    Returns:
        float: nilai rata-rata
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def analyze_business_data(data: dict) -> dict:
    """
    Simulasi analisis data bisnis sederhana.
    Args:
        data: dictionary berisi data bisnis
    Returns:
        dict: hasil analisis
    """
    result = {
        "total_customers": len(data.get("customers", [])),
        "average_score": calculate_average(data.get("scores", [])),
        "status": "analyzed"
    }
    return result


# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    print(f"App: {get_app_info()}")
    print("-" * 30)

    scores = [85, 90, 78, 92, 88]
    avg = calculate_average(scores)
    print(f"Scores: {scores}")
    print(f"Average: {avg}")
    print("-" * 30)

    business_data = {
        "customers": ["Budi", "Sari", "Tono", "Dewi"],
        "scores": [88, 76, 95, 82]
    }
    result = analyze_business_data(business_data)
    print(f"Analysis Result: {result}")