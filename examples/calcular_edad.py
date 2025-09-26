from datetime import datetime

# Get current date
now = datetime.now()

# Get birthdate
birthdate = datetime(2002, 7, 21)

# Calculate age
age = now - birthdate

age_in_years = age.days // 365

print(f"Age in years: {age_in_years} | {age}")