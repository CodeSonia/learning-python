from pathlib import Path

cwd = Path.cwd()

p = Path('.')
current_dir_python_files = list(p.glob('*.py'))

print(cwd)
print(current_dir_python_files)

for file in current_dir_python_files:
  print(file.name)
  print(file.stat().st_size)
