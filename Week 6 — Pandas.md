# Amusement Park

The `amusement_park.csv` file contains a dataset with information about visitors to an amusement park.

Each row represents a single visitor, and the columns capture various details about their visit:

| **Column Name**     | **Type**          | **Possible Values**                        | **Description**                                                 |
|---------------------|:-----------------:|--------------------------------------------|-----------------------------------------------------------------|
| **`VisitorID`**     | `int`             |                                            | Unique identifier for each visitor                              |
| **`Name`**          | `str`             |                                            | Visitor's full name in the format Surname, FirstName            |
| **`Age`**           | `Optional[float]` | Any positive number or `None`              | Age of the visitor (may contain missing values)                 |
| **`Sex`**           | `str`             | `male`, `female`                           | Gender of the visitor                                           |
| **`TicketClass`**   | `int`             | `1`, `2`, `3`                              | The class of the ticket purchased                               |
| **`Fare`**          | `float`           | Any positive number                        | The price paid for the ticket                                   |
| **`TicketNumber`**  | `str`             | Alphanumeric                               | The visitor's ticket number (numeric or alphanumeric)           |
| **`RideType`**      | `Optional[str]`   | Various ride names or `None`               | Type of ride chosen by the visitor (may contain missing values) |
| **`EntryTime`**     | `datetime64[ns]`  |                                            | Time of park entry stored as a datetime object                  |
| **`Exited`**        | `bool`            | `True`, `False`                            | Indicates if the visitor exited the park                        |
| **`EnteredVia`**    | `str`             | `Main Entrance`, `North Gate`, `East Gate` | Entrance gate used by the visitor                               |


## 0) Read the dataset and take a look at it 📊

Dataset URL: https://github.com/Python-Homeworks-CUB/Seminars/blob/main/notebooks/amusement_park.csv

> *Hint:* Add `?raw=true` to the URL to get the raw file from GitHub

<details><summary>Useful functions</summary>

```python
pandas.read_csv  # Read a CSV file into a DataFrame
```
</details>


```py
import pandas as pd

pd.set_option('display.width', 10 ** 10)  # Optional, allows for prettier printing

df = ???
```

<details><summary><b>Solution</b></summary>

```py
import pandas as pd

pd.set_option('display.width', 10 ** 10)  # Optional, allows for prettier printing

df = pd.read_csv('https://github.com/Python-Homeworks-CUB/Seminars/blob/main/notebooks/amusement_park.csv?raw=true')
print(df)
```
</details>


## 1) Age Profiling 🎂

Find the average age of visitors who entered through the `North Gate` and `East Gate`, separately for each ticket class


<details><summary>Useful functions</summary>

```python
pandas.Series.isin        # Check whether values are contained in Series
pandas.DataFrame.groupby  # Group DataFrame using a mapper or by a Series of columns
pandas.DataFrame.mean     # Return the mean of the values for the requested axis (technically, it's pandas.core.groupby.SeriesGroupBy.mean)
```
</details>

> *Hint:* To print the `groupby` object, you can use `obj.apply(print)`


```py
avg_age_by_gate = ???

print(avg_age_by_gate)
```

<details><summary><b>Solution</b></summary>

```py
avg_age_by_gate = df[
    df['EnteredVia'].isin(['North Gate', 'East Gate'])
].groupby('TicketClass')['Age'].mean()

print(avg_age_by_gate)
```
</details>


## 2) The Phantom Ages 👻

For the Age column, fill in the missing values with the median of the entire dataset and check how many values were filled

<details><summary>Useful functions</summary>

```python
pandas.Series.median  # Return the median of the values
pandas.Series.isna    # Detect missing values (returns a boolean Series with True for missing values)
pandas.Series.sum     # Return the sum of the values
pandas.Series.fillna  # Fill NA/NaN values using the specified method
```
</details>

```py
median_age = ???
filled_count = ???
???

print(f'Filled {filled_count} missing values in Age with median: {median_age}')
```

<details><summary><b>Solution</b></summary>

```py
median_age = df['Age'].median()
filled_count = df['Age'].isna().sum()
df['Age'] = df['Age'].fillna(median_age)

print(f'Filled {filled_count} missing values in Age with median: {median_age}')
```
</details>


## 4) The Cheapskate Club 💰

Find the number of visitors who paid the minimum ticket fare and the average age among them

<details><summary>Useful functions</summary>

```python
pandas.Series.min         # Return the minimum of the values
pandas.Series == {value}  # Select rows where the Series is equal to a specific value
pandas.DataFrame.shape    # Return a tuple representing the dimensionality of the DataFrame
```
</details>

```py
min_fare = ???
min_fare_visitors = ???
average_age_min_fare = ???

print(f'Visitors with minimum fare: {min_fare_visitors???}')  # First try just printing `min_fare_visitors` and work you way from there
print(f'Their average age: {average_age_min_fare}')
```

<details><summary><b>Solution</b></summary>

```py
min_fare = df['Fare'].min()
min_fare_visitors = df[df['Fare'] == min_fare]
average_age_min_fare = min_fare_visitors['Age'].mean()

print(f'Visitors with minimum fare: {min_fare_visitors.shape[0]}')
print(f'Their average age: {average_age_min_fare}')
```
</details>


## 5) Lady's Choice 👩‍🎤

Identify the ride that has more female visitors than male visitors. Provide the name of the ride and the counts of female and male visitors for that ride.

<details><summary>Useful functions</summary>

```python
pandas.DataFrame.size                 # Return the size of each group
pandas.DataFrame.unstack              # Pivot a level of the index labels
pandas.DataFrame[boolean expression]  # Select rows based on a boolean condition
```
</details>

> *Hint:* You can use `obj.groups` on a `groupby` object to see the groups

> *Hint:* You can use `obj.index` on a `DataFrame` to see the labels


```py
???
```

<details><summary><b>Solution</b></summary>

```py
ride_gender_count = df.groupby(['RideType', 'Sex']).size().unstack()

ride_gender_count[ride_gender_count['female'] > ride_gender_count['male']]
# As we can see, in Jupyter Notebook we can pretty-print the DataFrame
```
</details>


## 6) Lucky Tickets 🍀

Determine the percentage of lucky tickets among visitors

```py
def is_lucky(ticket):
    digits = ''.join(char for char in ticket if char.isdigit())

    if len(digits) % 2 != 0:
        return False

    middle = len(digits) // 2
    sum_first_half = sum(int(digit) for digit in digits[:middle])
    sum_second_half = sum(int(digit) for digit in digits[middle:])

    return sum_first_half == sum_second_half


df['IsLucky'] = ???
lucky = df[???]
proportion_lucky = ???
print(f'Percentage of lucky tickets: {proportion_lucky * 100}%')
```

<details><summary><b>Solution</b></summary>

```py
def is_lucky(ticket):
    digits = ''.join(char for char in ticket if char.isdigit())

    if len(digits) % 2 != 0:
        return False

    middle = len(digits) // 2
    sum_first_half = sum(int(digit) for digit in digits[:middle])
    sum_second_half = sum(int(digit) for digit in digits[middle:])

    return sum_first_half == sum_second_half


df['IsLucky'] = df['TicketNumber'].apply(is_lucky)
lucky = df[df['IsLucky']]
proportion_lucky = lucky.shape[0] / df.shape[0]
print(f'Percentage of lucky tickets: {proportion_lucky * 100}%')
```
</details>


## 7) How Should I Call You? 🗣️

Split the full name into `Surname` and `FirstName`, then create a new dataframe with these two columns.

Show a preview of the freshly created DataFrame

<details><summary>Useful functions</summary>

```python
pandas.Series.str        # Accessor object for string methods
pandas.Series.str.split  # Split strings around given separator (expand: True to return a DataFrame)
```
</details>

> *Hint:* You can use the `DataFrame.head()` method to display the first few rows of the new DataFrame

```py
???
```

<details><summary><b>Solution</b></summary>

```py
df[['Surname', 'FirstName']] = df['Name'].str.split(',', expand=True)
df[["Surname", "FirstName"]].head()
```
</details>


## 8) Can't Live Without Math (NumPy) 🤓

Calculate basic statistical metrics for the `Fare` column: `median`, `min`, `max`, `std` (Standard Deviation)

> *Requirement*: Use `NumPy` here

<details><summary>Useful functions</summary>

```python
pandas.DataFrame.to_numpy  # Convert the DataFrame to a NumPy array
```
</details>

<!-- <details><summary>Useful functions</summary>

```python
pandas.DataFrame.agg  # Aggregate using one or more operations
```
</details>

> *Hint*: We can select one column in the DataFrame and then use `DataFrame.agg` to calculate multiple metrics at once. -->

```py
import numpy as np

fare_values = ???

median_fare = ???
min_fare = ???
max_fare = ???
std_fare = ???

print(f'Median Fare: {median_fare}')
print(f'Min Fare: {min_fare}')
print(f'Max Fare: {max_fare}')
print(f'Standard Deviation of Fare: {std_fare}')
```

<details><summary><b>Solution</b></summary>

```py
import numpy as np

fare_values = df['Fare'].to_numpy()

median_fare = np.median(fare_values)
min_fare = np.min(fare_values)
max_fare = np.max(fare_values)
std_fare = np.std(fare_values)

print(f'Median Fare: {median_fare}')
print(f'Min Fare: {min_fare}')
print(f'Max Fare: {max_fare}')
print(f'Standard Deviation of Fare: {std_fare}')
```
</details>


## 9) Popular Rides 🎢

Find rides with more than 100 visitors and get their names and visitor counts.

<details><summary>Useful functions</summary>

```python
pandas.DataFrame.value_counts  # Return a Series containing counts of unique rows in the DataFrame
```
</details>

```py
all_attractions = ???
popular_attractions = ???

print(f'Rides with more than 100 visitors: {", ".join(popular_attractions)}')
```

<details><summary><b>Solution</b></summary>

```py
all_attractions = df['RideType'].value_counts()
popular_attractions = all_attractions[all_attractions > 100].index

print(f'Rides with more than 100 visitors: {", ".join(popular_attractions)}')
```
</details>
