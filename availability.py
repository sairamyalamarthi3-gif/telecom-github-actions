def calculate_availability(total_minutes, downtime_minutes):
    if total_minutes <= 0:
        raise ValueError("Total minutes must be greater than zero")

    if downtime_minutes < 0:
        raise ValueError("Downtime cannot be negative")

    if downtime_minutes > total_minutes:
        raise ValueError("Downtime cannot exceed total minutes")

    available_minutes = total_minutes - downtime_minutes
    availability = (available_minutes / total_minutes) * 100

    return round(availability, 3)


if __name__ == "__main__":
    monthly_availability = calculate_availability(43200, 20)
    print(f"Circuit availability: {monthly_availability}%")
