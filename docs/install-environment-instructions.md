# Installation instructions for development environment
## On Windows 10

- Install Vscode + pyhon addon + qt for python addon
- Install miniconda (just for me, do not set path)
- use conda to install flake8, pyqt5, opencv
- activate Flake8 in Vscode (TODO details)
- set designer path in qt for python plugin in vscode (TODO details)
- set pyuic (TODO details)

## On Debian/Ubunu Linux
- Install Vscode + pyhon addon + qt for python addon
- install qt (in /opt) from qt site
- install pyqt5 (pip3 install pyqt5)
- set designer path in qt for python addon(/opt/Qt/*Put Qt Version Here*/gcc_64/bin/designer)
- set pyuic command in qt for python addon (pyuic5 -o ${fileDirname}/${fileBasenameNoExtension}_UI.py)