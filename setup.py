from setuptools import setup, find_packages

setup(
    name='dsplayer-youtube',  
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'dsplayer',
        'yt-dlp'
    ],
    entry_points={
        'dsplayer.plugins': [
            'youtube = plugin.plugin:YoutubePlugin',
        ],
    },
)