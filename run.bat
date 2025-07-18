@echo off
echo Checking for updates...
git pull https://github.com/onlyzerosonce/Progress main

echo Starting the media consumption application...
python media_consumer.py
pause
