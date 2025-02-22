# setup.py

import setuptools

setuptools.setup(
    name="post-crafter",                        # Package name (choose any unique name)
    version="0.1.0",                          # Package version
    packages=setuptools.find_packages(),       # Automatically find packages (i.e. 'my_package')
    install_requires=[                         # Dependencies for runtime
        "requests>=2.32.3",
        "python-dotenv>=1.0.1",
        "openai>=1.63.2",
        "streamlit>=1.42.2"
    ],
    entry_points={
        # This is the magic that creates a console command called 'llm'
        'console_scripts': [
            'post-crafter = post_crafter.cli:main',
        ],
    },
    python_requires=">=3.12"
)
