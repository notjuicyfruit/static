# build_static_files.py
from app import main

if __name__ == '__main__':
    app = main()
    app.build(app_module_name='app', output_dir='public')
