import datetime

CSV_FILE = "bmi_log.csv"


# ---------------- Validation ----------------
def get_positive_float(prompt):
    value = input(prompt)
    try:
        value = float(value)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        raise ValueError("Value must be a positive number")


# ---------------- Conversions ----------------
def imperial_to_metric(height_in, weight_lb):
    height_m = height_in * 0.0254
    weight_kg = weight_lb * 0.453592
    return height_m, weight_kg


# ---------------- BMI Logic ----------------
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# ---------------- CSV Logging ----------------
def append_to_csv(record):
    try:
        with open(CSV_FILE, "x") as f:
            f.write("timestamp,height_m,weight_kg,bmi,category\n")
    except FileExistsError:
        pass

    with open(CSV_FILE, "a") as f:
        f.write(
            f"{record['timestamp']},"
            f"{record['height_m']:.2f},"
            f"{record['weight_kg']:.2f},"
            f"{record['bmi']:.2f},"
            f"{record['category']}\n"
        )


# ---------------- Logger ----------------
def log_bmi():
    unit = input("Choose unit (M = Metric, I = Imperial): ").strip().upper()

    try:
        if unit == "M":
            height_m = get_positive_float("Height (meters): ")
            weight_kg = get_positive_float("Weight (kg): ")

        elif unit == "I":
            height_in = get_positive_float("Height (inches): ")
            weight_lb = get_positive_float("Weight (pounds): ")
            height_m, weight_kg = imperial_to_metric(height_in, weight_lb)

        else:
            print("Invalid unit choice.")
            return

        bmi = calculate_bmi(weight_kg, height_m)
        category = bmi_category(bmi)

        record = {
            "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
            "height_m": height_m,
            "weight_kg": weight_kg,
            "bmi": bmi,
            "category": category
        }

        append_to_csv(record)

        print(f"BMI: {bmi:.2f} ({category})")
        print("Entry saved.")

    except ValueError as e:
        print("Error:", e)


# ---------------- Display Last 10 ----------------
def display_last_10():
    try:
        with open(CSV_FILE, "r") as f:
            lines = f.readlines()[1:]  # skip header
    except FileNotFoundError:
        print("No BMI records found.")
        return

    last_entries = lines[-10:]

    print("\nLAST 10 BMI ENTRIES")
    print("-" * 40)

    for line in last_entries:
        timestamp, _, _, bmi, category = line.strip().split(",")

        bmi_value = float(bmi)
        bars = "#" * int(bmi_value)

        print(f"{timestamp} | BMI {bmi} | {category}")
        print(bars)


# ---------------- Menu ----------------
def menu():
    while True:
        print("\nBMI LOGGER")
        print("1. Log new BMI")
        print("2. View last 10 entries")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            log_bmi()
        elif choice == "2":
            display_last_10()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


# Run program
menu()
