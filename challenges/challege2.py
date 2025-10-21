# Seconds conversor

seconds = int(input("Enter a number of seconds: "))

hours = seconds // 3600
seconds_remaining = seconds % 3600

minutes = seconds_remaining // 60
final_seconds = seconds_remaining % 60

print(f"{seconds} seconds equals to:")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Final seconds: {final_seconds}")