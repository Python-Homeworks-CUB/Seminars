from magic import file_not_found_handler

def get_relative_path():
    return 'data.txt'

def get_absolute_path():
    return r'/Users/Rodion.Khvorostov/Desktop/Prog/Other/python_teaching_2024/practice_materials/seminars/seminar12_imports/path_practice/data.txt'

def get_absolute_path_with_os():
    import os  # bad practice
    relative_path = get_relative_path()
    parent_dir = os.path.dirname(__file__)
    return os.path.join(parent_dir, relative_path)

@file_not_found_handler
def print_content(path: str, method_used: str):
    print(f"Printing content of file using {method_used}")
    with open(path, 'r') as file:
        print(file.read())

    print('---')
    print()


def main():
    # relative
    path = get_relative_path()
    print_content(path, 'relative')

    # absolute
    path = get_absolute_path()
    print_content(path, 'absolute')

    # absolute with os
    path = get_absolute_path_with_os()
    print_content(path, 'absolute with os')

if __name__ == '__main__':
    main()