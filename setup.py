from setuptools import setup, find_packages

setup(
    name='doggame',
    packages=find_packages(),
    options={
        'build_apps': {
            # Build exe as a GUI application
            'gui_apps': {
                'doggame': 'game.py',
            },
            'icons': {
                'doggame': ['animal-dog.bmp']
            },
            
    
            # Set up output logging, important for GUI apps!
            'log_filename': 'output.log',
            'log_append': False,

            # Specify which files are included with the distribution
            'include_patterns': [
                'settings.prc',
                'src/assets/**'
                
                
                
            ],

            # Include the OpenGL renderer and OpenAL audio plug-in
            'plugins': [
                'pandagl',
                'p3openal_audio',
                'p3ffmpeg'
            ],
        }
    }
)

