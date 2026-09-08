from availability import calculate_availability


total_minutes = 43200
downtime_minutes = 20

availability = calculate_availability(
    total_minutes,
    downtime_minutes
)

print(f"Total circuit minutes: {total_minutes}")
print(f"Downtime minutes: {downtime_minutes}")
print(f"Circuit availability: {availability:.3f}%")
