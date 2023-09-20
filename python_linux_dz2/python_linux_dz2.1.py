import subprocess
import hashlib

def test_list_files():
    # Run command to list files
    result = subprocess.run(['./project', 'l'], capture_output=True, text=True)
    output = result.stdout.strip()

    # Define expected file list here
    expected_files = ['file1.txt', 'file2.txt', 'file3.txt']

    assert output == '\n'.join(expected_files)

def test_extract_files():
    # Run command to extract files
    result = subprocess.run(['./project', 'x'], capture_output=True, text=True)
    output = result.stdout.strip()

    # Define expected files path here
    expected_files = ['/path/to/file1.txt', '/path/to/file2.txt', '/path/to/file3.txt']

    assert output == '\n'.join(expected_files)

def test_calculate_hash():
    # Run command to calculate hash
    result = subprocess.run(['./project', 'h'], capture_output=True, text=True)
    output = result.stdout.strip()

    # Calculate hash of all files
    md5_hash = hashlib.md5()
    md5_hash.update(open('file1.txt', 'rb').read())
    md5_hash.update(open('file2.txt', 'rb').read())
    md5_hash.update(open('file3.txt', 'rb').read())
    expected_hash = md5_hash.hexdigest()

    assert output == expected_hash

# Run all the tests
test_list_files()
test_extract_files()
test_calculate_hash()