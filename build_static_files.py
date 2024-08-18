# build_static_files.py
from toga_web import App
import os
import shutil

# Create a new Toga Web app instance
app = App()

# Path to the directory where static files will be stored
output_dir = 'public'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Build the static files
app.build_static(output_dir)

# Optionally, remove previous builds (if needed)
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)

# Now build the static files
app.build_static(output_dir)
