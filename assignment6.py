humidity = float(input("Enter Relative Humidity (%): "))
temperature = float(input("Enter Temperature (°C): "))
ph = float(input("Enter pH: "))
salt = input("Salt Present? (Yes/No): ").lower()

if humidity > 80 and salt == "yes":
    risk = "High"
elif humidity > 60 or ph < 5 or temperature > 35:
    risk = "Moderate"
else:
    risk = "Low"

print("\nCorrosion Risk:", risk)
