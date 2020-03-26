from pathlib import Path

# Absolute path -- start from root of hard disk
#   /usr/local/bin
# Relative path
#

path = Path("emails")  # like Java File class
print(path.exists())
# print(path.mkdir())
# print(path.rmdir())

path = Path()
# print(path.glob('*.py'))  # all py files in current directory

for file in path.glob('*'):
    print(file)
