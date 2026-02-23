import json
import os


def load_json(file_name):
    """
    Reads a JSON file from the testdata folder and returns a list of dictionaries.
    """
    # 1. Get the directory where data_reader.py is located (utilities/)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 2. Go up one level to the project root, then into 'testdata'
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, 'testdata', file_name)

    # 3. Safety check to provide a clear error message
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JSON file not found at: {file_path}")

    # 4. Open and return the data
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)