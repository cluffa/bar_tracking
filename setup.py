import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name = 'bar-tracking',
        version = 0.2,
        author = 'cluffa',
        author_email = 'alexcluff16@gmail.com',
        url = 'https://github.com/cluffa/bar_tracking',
        packages = ['BarTracking'],
        install_requires = [
            'numpy', 'scipy', 'pandas', 'torch', 'torchvision', 'opencv-python', 'matplotlib'
        ]
    )