from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock',
    'pytest-qt',
    'pytest-xvfb',
]

setup(
    name='demo-qt-inspector',
    version='0.0.1',
    description="A PyQt5 GUI application",
    author="demo_qt_inspector",
    author_email='williamjamir@gmail.com',
    url='https://github.com/williamjamir/demo-qt-inspector',
    packages=['demo-qt-inspector', 'demo-qt-inspector.images',
              'demo-qt-inspector.tests'],
    package_data={'demo-qt-inspector.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'Template=demo-qt-inspector.application:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='demo-qt-inspector',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
