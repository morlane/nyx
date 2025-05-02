import os

def count_lines_in_file(file_path):
    """Count non-empty lines in a single file."""
    try:
        with open(file_path, 'r', errors='ignore') as f:
            return sum(1 for line in f if line.strip())
    except Exception as e:
        print(f"Could not read {file_path}: {e}")
        return 0

def scan_directory_for_lines(directory, extension):
    total_lines = 0
    file_count = 0

    print(f"Scanning '{directory}' for '*{extension}' files...\n")
    
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(extension):
                full_path = os.path.join(root, filename)
                lines = count_lines_in_file(full_path)
                print(f"{full_path}: {lines} lines")
                total_lines += lines
                file_count += 1

    print(f"\nScanned {file_count} file(s).")
    print(f"Total lines of code: {total_lines}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Count lines of code in project files.")
    parser.add_argument("directory", help="Directory to scan")
    parser.add_argument("extension", help="File extension to look for (e.g., .py, .vhd, .c)")

    args = parser.parse_args()
    scan_directory_for_lines(args.directory, args.extension)
