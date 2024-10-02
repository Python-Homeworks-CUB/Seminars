import pandas as pd
import numpy as np
import random
import string


def generate_amusement_park_data(num_entries=200, seed=42):
    np.random.seed(seed)
    random.seed(seed)

    # Define possible values for each column
    first_names = ["John", "Jane", "Sam", "Sally", "Michael", "Michelle", "Chris", "Christina", "Daniel", "Danielle"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    sexes = ["male", "female"]
    ticket_classes = [1, 2, 3]
    ride_types = ["rollercoaster", "carousel", "bumper cars", "haunted house", "water slide"]
    gates = ["Main Entrance", "North Gate", "East Gate"]

    # Generate visitor data
    data = []

    today = pd.to_datetime('today').normalize()

    for i in range(num_entries):
        visitor_id = i + 1

        # Randomly select name (ensuring some family surnames)
        last_name = random.choice(last_names)
        first_name = random.choice(first_names)
        if i % 20 == 0:  # Introduce families every 20 entries
            family_name = random.choice(last_names)
            first_name = random.choice(first_names)
            full_name = f"{family_name}, {first_name}"
        else:
            full_name = f"{last_name}, {first_name}"

        # Random age with some NaNs
        age = np.random.choice([np.random.randint(5, 80), np.nan], p=[0.9, 0.1])

        sex = random.choice(sexes)
        ticket_class = np.random.choice(ticket_classes, p=[0.3, 0.5, 0.2])  # Assign ticket classes with probabilities

        # Random fare: higher for lower class numbers
        fare = round(np.random.uniform(10, 50) * (4 - ticket_class), 2)

        # Random ticket number, some being non-numeric
        ticket_number = ''.join(random.choices(string.digits, k=random.choice([4, 5, 6, 8])))
        if random.random() < 0.2:
            ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Ride type with some NaNs
        ride_type = np.random.choice(ride_types + [np.nan], p=[0.2, 0.2, 0.2, 0.2, 0.1, 0.1])

        # Random entry time and exit status
        # entry_time = f"{random.randint(9, 21):02}:{random.randint(0, 59):02}"
        entry_hour = random.randint(9, 21)
        entry_minute = random.randint(0, 59)
        entry_time = pd.Timestamp(f"{today.date()} {entry_hour:02}:{entry_minute:02}")

        exited = np.random.choice([True, False], p=[0.7, 0.3])  # Most people eventually exit

        # Random gate entry
        entered_via = random.choice(gates)

        # Append to data list
        data.append([
            visitor_id, full_name, age, sex, ticket_class, fare, ticket_number,
            ride_type, entry_time, exited, entered_via
        ])

    # Create the DataFrame
    df = pd.DataFrame(data, columns=[
        "VisitorID", "Name", "Age", "Sex", "TicketClass", "Fare", "TicketNumber",
        "RideType", "EntryTime", "Exited", "EnteredVia"
    ])

    # Introduce some NaN values in the dataset
    nan_indices = np.random.choice(df.index, size=int(0.05 * num_entries), replace=False)
    df.loc[nan_indices, "Age"] = np.nan
    df.loc[np.random.choice(df.index, size=int(0.05 * num_entries), replace=False), "RideType"] = np.nan

    # Save the DataFrame to CSV
    df.to_csv("../notebooks/amusement_park.csv", index=False)
    print("amusement_park.csv generated successfully!")


# Run the generator
generate_amusement_park_data(1000, random.randint(0, 1000))
