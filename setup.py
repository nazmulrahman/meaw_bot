from setuptools import setup
import os
from glob import glob

package_name = 'meaw_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),  # <-- supports meaw.launch.py
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arnab',
    maintainer_email='your_email@example.com',
    description='Robot controller and camera integration',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller = meaw_bot.controller:main',
        ],
    },
)
