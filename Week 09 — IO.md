# IO: Input/Output

Until now, we have been using the standard input and output for reading and writing data, e.g. `input` and `print` functions. \
What if we want to input data from some other source, like a file? \
Or maybe use the advanced features of the `print` function for generating strings?

### Files
To open a file, we use the `open` function. To close it, we use the `close` function.

```py
file = open('file.txt', 'r/w/a{+}')
file.close()
```

<h5 align="center">Available opening modes</h5>
<table align="center">
    <tr>
        <th align="center">Mode</th>
        <th align="center">Description</th>
        <th align="center">Creates new file</th>
        <th align="center">Truncates file (starts at the beginning)</th>
    </tr>
    <tr>
        <td align="center">r</td>
        <td>Only read from file</td>
        <td align="center"></td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">r+</td>
        <td>Read and write to file</td>
        <td align="center"></td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">w</td>
        <td>Only write to file</td>
        <td align="center">✓</td>
        <td align="center">✓</td>
    </tr>
    <tr>
        <td align="center">w+</td>
        <td>Read and write to file</td>
        <td align="center">✓</td>
        <td align="center">✓</td>
    </tr>
    <tr>
        <td align="center">a</td>
        <td>Append to file</td>
        <td align="center">✓</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">a+</td>
        <td>Read and append to file</td>
        <td align="center">✓</td>
        <td align="center"></td>
    </tr>
</table>

We can utilize multiple methods to read and write data from/to a file:

Reading:
```py
read() -> str             # Reads the entire file
readline() -> str         # Reads one line
readlines() -> list[str]  # Reads all lines
for line in file: ...     # Iterates over the file line by line
```

Writing:
```py
write(str)               # Writes a string
writelines(list[str])    # Writes a list of strings
print(..., file={file})  # Redirects the output of the `print` function to the file
```

All these functions read/write the data starting from the current file pointer position (remember the file opening modes). \
This allows us, for example, to call `realine()` multiple times and get the next line each time.

#### Exercise:
Write a program that creates a file with integers from 1 to 20. After that, read the file and print the numbers in reverse order.

Try using different reading/writing methods, for example:
- numbers `1-5` using `write()`
- numbers `6-10` using `writelines()`
- numbers `11-20` using `print(..., file={file})`  (you can use the `sep` argument to separate the number by a newline character)

Which function is better for reading and reversing the numbers: `read()` or `readlines()`? Try both
```py
file = open('numbers.txt', 'w')
# Using write()
file.write('1\n2\n3\n4\n5\n')
# Using writelines()
file.writelines(['6\n', '7\n', '8\n', '9\n', '10\n'])
# Using print(..., file=file)
print(*list(range(11, 21)), sep='\n', file=file)
file.close()

file = open('numbers.txt', 'r')
# print(file.read()[::-1])  # Reverses symbol-by-symbol, not what we want
for line in file.readlines()[::-1]:  # Reverses line-by-line
    print(line.strip())  # .strip() to remove trailing newline
file.close()
```


### Context Managers

We always need to close the file after we are done working with it. \
For example, if we are writing to a file and the program crashes before we close it, the data might not be saved (flushed from the buffer).

So a safer way to work with files is to enclose them in a `try-except-finally` block:

```py
file = open('file.txt', 'w')
try:
    # Work with the file
except:
    # Optionally handle the exception
finally:
    file.close()
```

But this uses 7 lines! We can do better using the `with` statement (a.k.a context manager):

```py
with open('file.txt', 'w') as file:
    # Work with the file
# File is automatically closed when we exit the block or if an exception is raised
```

### JSON format

[JSON](https://www.json.org/json-en.html) (JavaScript Object Notation) is a lightweight data interchange format compatible with many programming languages.

```json
{
    "name": "John",
    "age": 30,
    "adult": true,
    "children": [
        {
            "name": "Alice",
            "age": 5,
            "adult": false,
            "children": null
        },
        {
            "name": "Bob",
            "age": 7,
            "adult": false,
            "children": null
        }
    ]
}
```

As you can see, JSON's syntax is very similar to Python dictionaries and lists.

Python has a built-in module `json` that allows us to work with JSON data:

```py
import json

json.load({file}) -> obj  # Reads JSON data from a file
json.loads(str) -> obj    # Reads JSON data from a string
json.dump(obj, {file})    # Writes JSON data to a file
json.dumps(obj)           # Writes JSON data to a string
```

### CSV format

You might already be familiar with CSV files from the Pandas library:

[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) (Comma-Separated Values) is a simple file format used to store tabular data.

```csv
name,age,adult
John,30,true
Alice,5,false
Bob,7,false
```

Python has a built-in module `csv` that allows us to work with CSV data:

```py
import csv

reader = csv.reader({file})    # Object to read the file as a list of lists
for row in reader:
    row: list[str]

reader = csv.DictReader(file)  # Object to read the file as a dictionary with the keys being the first row
for row in reader:
    row: dict[str, str]

writer = csv.writer({file})                   # Object to write the data to the file line by line
writer.writerow(list[str])                    # Writes one row
writer.writerows(list[list[str], list[str]])  # Writes multiple rows

writer = csv.DictWriter(file, fieldnames=list[str])  # Object to write the data to the file as a dictionary
writer.writeheader()                                 # Writes the header (specified by `fieldnames` when creating the object)
writer.writerow(dict[str, str])                      # Writes one row
writer.writerows(list[dict[str, str]])               # Writes multiple rows
```

### CLI (Command Line Interface) arguments

Sometimes we want to pass arguments to our program from the command line.

Python has a built-in module `argparse` that allows us to work with CLI arguments:

```py
import argparse

parser = argparse.ArgumentParser(description='Description of the program')
parser.add_argument(
    '{variable name}', '{-name}', '{-shortcut}',
    type=str,
    required=True/False,
    help='{variable description}'
)
args = parser.parse_args()
args.{variable name}  # Access the variable
```

#### Exercise: CSV to JSON Converter

Write an CLI (Command Line Interface) program that converts a CSV file to a JSON file.

If the `-p` flag is set, the program should pretty-print the JSON output: \
Prettify the JSON output by using the `indent` and `sort_keys` arguments of the `json.dump{s}` function

The application will be called like this:

```bash
python csv_to_json {-p} --csv="amusement_park.csv" --json="amusement_park.json"
```

Use the functions we learned above as well as context managers to minimize the amount code.

You can solve this exercise in a separate file to test it's functionality.

```py
import argparse
import json
import csv


def csv_to_json(csv_filename: str, json_filename: str, pretty: bool = False) -> None:
    """Convert CSV data to JSON format with optional pretty formatting."""
    with open(csv_filename, 'r', newline='') as csv_file:
        data = list(csv.DictReader(csv_file))

    with open(json_filename, 'w') as json_file:
        if pretty:
            json.dump(data, json_file, indent=4, sort_keys=True)
        else:
            json.dump(data, json_file)


def main():
    parser = argparse.ArgumentParser(description="Convert a CSV file to a JSON file.")
    parser.add_argument("--csv", required=True, type=str, help="Path to the input CSV file.")
    parser.add_argument("--json", required=True, type=str, help="Path to the output JSON file.")
    parser.add_argument("-p", "--pretty", action="store_true", help="Enable pretty-printing for the JSON output.")

    args = parser.parse_args()
    csv_to_json(args.csv, args.json, pretty=args.pretty)


if __name__ == "__main__":
    main()
```

### Different I/O Streams

- What if we want to pretty-print some data to the string? `f`-strings are good, but there is another option.
- What if we want to process a large amount of data and don't have enough RAM to store it all?
- What if we want stream data to the customer via the Internet (think of livestreams, e.g. YouTube or Twitch)?

Streaming data is a common practice. We already know how streaming works with the standard input (`stdin`) and output (`stdout`).

But there are other streams:

- Standard streams:

    ```py
    import sys

    sys.stdin   # Standard input stream
    sys.stdout  # Standard output stream
    sys.stderr  # Standard error stream (you might have seen those red messages in the console)
    ```

- String streams:

    ```py
    from io import StringIO
    from io import BytesIO

    stream = StringIO()
    stream.write('Hello, World!')
    stream.seek(0)
    print(stream.read())

    stream = BytesIO()
    stream.write(b'Hello, World!')
    stream.seek(0)
    print(stream.read())
    ```

- System processes (advanced topic):

    ```py
    import subprocess

    process = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(process.stdout.decode())
    ```

- Network streams (advanced topic):

    ```py
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        s.sendall(b'Hello, World!')  # Instead of `write`
        data = s.recv(1024)          # Instead of `read`
        print(data.decode())
    ```
