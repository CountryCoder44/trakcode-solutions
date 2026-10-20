# Daily Temperature Log Analyzer

from math import isfinite


def classify_temperature(temperature):
    if temperature < 10:
        return "Cold"
    elif temperature <= 25:
        return "Mild"
    else:
        return "Hot"


def print_summary(readings, invalid_count, cold_count, mild_count, hot_count):
    if not readings:
        print("No valid temperature readings were recorded.")
        return

    average = sum(readings) / len(readings)

    print(f"Valid readings: {len(readings)}")
    print(f"Invalid entries skipped: {invalid_count}")
    print(f"Average temperature: {average:.1f}C")
    print(f"Minimum temperature: {min(readings):.1f}C")
    print(f"Maximum temperature: {max(readings):.1f}C")
    print(f"Cold (<10C): {cold_count}")
    print(f"Mild (10-25C): {mild_count}")
    print(f"Hot (>25C): {hot_count}")


def main():
    readings = []
    invalid_count = 0
    cold_count = 0
    mild_count = 0
    hot_count = 0

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line.lower() == "done":
            break

        try:
            temperature = float(line)
        except ValueError:
            invalid_count += 1
            continue

        # NaN and infinity do not represent finite temperature readings.
        if not isfinite(temperature):
            invalid_count += 1
            continue

        readings.append(temperature)
        category = classify_temperature(temperature)

        if category == "Cold":
            cold_count += 1
        elif category == "Mild":
            mild_count += 1
        else:
            hot_count += 1

    print_summary(readings, invalid_count, cold_count, mild_count, hot_count)


if __name__ == "__main__":
    main()
