from setuptools import setup, find_packages

setup(
    name='dsplayer-youtube',  
    version='1.2.0',
    packages=find_packages(),
    install_requires=[
        'dsplayer',
        'yt-dlp'
    ],
    entry_points={
        'dsplayer.plugins': [
            'youtube = dsplayer_youtube.youtube:YoutubePlugin',
        ],
    },
)