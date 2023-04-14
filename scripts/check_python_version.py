import platform
import argparse
from packaging import version

parser = argparse.ArgumentParser()
parser.add_argument('--min-version', help='Minimum Python version')
args = parser.parse_args()

actual_py=version.parse(platform.python_version())
min_py=version.parse(args.min_version)

if (min_py > actual_py):
    print(f"Error: Python version is {actual_py}, but required {min_py} or higher!")
    exit(1)
