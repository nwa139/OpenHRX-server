# OpenHRX, Free and Open Source EMS

###### © 2025-2026  OpenHRX

[![OpenHRX Official Website](https://img.shields.io/badge/OpenHRX-Official%20Website-0047ab?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOVSURBVFhHrZc/bFdVFMfPeZYBQqpJm+hIKFSMQ9PFaOIiLJgy6GyauLKYEFkYlERXZGCtbRh0M0xU6IJhYZHB2GL8mWBkavljYhVqUsrn6/A7r73v9L0fv6qf5CXvvfs959x737nn3es2JJJelDRjZu+4+7SkQ2b2UjT/4e6/SfrBzG64+6K7rycX/w5gEpgHNjQkwAawAExmfxnPL2okHZD0mZl95O77Utuamf1iZr/HqzEzm3T3V5LuqZldcvdP3X2jbBsIcBRYSaPqAWclHc76GkmHgY+Bn5PtCnA061sBpoGHhfEqMCupytouJFXALLBa+HkITGdtgxh5Gfy6pPGsGxZJ4+Gj7ET7TEg6UE478JWkkayzfkdHgTPAN3GdAUazzvp+R8JX7XcZ2J91BnxRiK53BZd0DLhXawube5KOZb3tdKKciQsNQSy1zWhc7Zp2SfuAnxqRC6Ktq+PjdU4Am40lCiwUTmYblgXAqUbEFoCZbFcTyVzrFsyiwtVFJpZPZ7YD5xrRWgDOZbuaWB290G0Ao5WkGXevk2LO3Ul2JX/lFy10asL3XNzvN7NTBnxZDKCzyNhOrjwr9A2AZ53LLAAmCv2cSbodD6tZ3AZwsRG1ALiY9RlJDqyFyW0DHoXxzSxuI77jeeBxEfgxcH5Q/pQAN8PukQFb8XAlCwch6aCkt+M6mNsHAVyJmFtD9Tgj6ZCkE5Jei+tE7A/2zrCfIKrZaeBOPfUZ4A5wuqsY1TQ+wTBJCIwBt3LALoBbwFj2Yx1JuL0MgYlsYP0OXNtxPxzAtezH+r6OFJq5ysxuFO3vF/dmsW7d/WR+/zzc/WRHXXmvuP8ul+JeXkrAVGNoewCYKn2lUvxk+xcOzBdGjZ9RJN+vDc9DANyV9ELpK/2M5suGgb9j4C1gvRFhAMA68GbpI37Ha9G+uatkAxcKB0t5KcV2bRGgEa2APovZecziUqHb3pBsb8tjm/S9u78eRl+7+4fuvlVrQjdhZu+a2ZSZvRyv75vZj2b2bVVVd0u9pBFJl939g3heMbM3qqr6u9SZxRIBHhQ9XcqfYy/EtJcjfwAcyboGLdvytf+wLa8LTh188La8JmZiuTYOBz3gbBSSXSeqqHATcTDpJdvlrpHvclQTOfF5x9Hsvpn10tHsVXevc6LWPTWzS2b2Ses3H4bI/nngSTmqQfwvh9NMVK0ZMzv+vOO5mV2tqurP5KKVfwBn87Tq7MzTCgAAAABJRU5ErkJggg==)](https://www.openhrx.be)
[![OpenHRX Documentation](https://img.shields.io/badge/OpenHRX-Documentation-0047ab?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOVSURBVFhHrZc/bFdVFMfPeZYBQqpJm+hIKFSMQ9PFaOIiLJgy6GyauLKYEFkYlERXZGCtbRh0M0xU6IJhYZHB2GL8mWBkavljYhVqUsrn6/A7r73v9L0fv6qf5CXvvfs959x737nn3es2JJJelDRjZu+4+7SkQ2b2UjT/4e6/SfrBzG64+6K7rycX/w5gEpgHNjQkwAawAExmfxnPL2okHZD0mZl95O77Utuamf1iZr/HqzEzm3T3V5LuqZldcvdP3X2jbBsIcBRYSaPqAWclHc76GkmHgY+Bn5PtCnA061sBpoGHhfEqMCupytouJFXALLBa+HkITGdtgxh5Gfy6pPGsGxZJ4+Gj7ET7TEg6UE478JWkkayzfkdHgTPAN3GdAUazzvp+R8JX7XcZ2J91BnxRiK53BZd0DLhXawube5KOZb3tdKKciQsNQSy1zWhc7Zp2SfuAnxqRC6Ktq+PjdU4Am40lCiwUTmYblgXAqUbEFoCZbFcTyVzrFsyiwtVFJpZPZ7YD5xrRWgDOZbuaWB290G0Ao5WkGXevk2LO3Ul2JX/lFy10asL3XNzvN7NTBnxZDKCzyNhOrjwr9A2AZ53LLAAmCv2cSbodD6tZ3AZwsRG1ALiY9RlJDqyFyW0DHoXxzSxuI77jeeBxEfgxcH5Q/pQAN8PukQFb8XAlCwch6aCkt+M6mNsHAVyJmFtD9Tgj6ZCkE5Jei+tE7A/2zrCfIKrZaeBOPfUZ4A5wuqsY1TQ+wTBJCIwBt3LALoBbwFj2Yx1JuL0MgYlsYP0OXNtxPxzAtezH+r6OFJq5ysxuFO3vF/dmsW7d/WR+/zzc/WRHXXmvuP8ul+JeXkrAVGNoewCYKn2lUvxk+xcOzBdGjZ9RJN+vDc9DANyV9ELpK/2M5suGgb9j4C1gvRFhAMA68GbpI37Ha9G+uatkAxcKB0t5KcV2bRGgEa2APovZecziUqHb3pBsb8tjm/S9u78eRl+7+4fuvlVrQjdhZu+a2ZSZvRyv75vZj2b2bVVVd0u9pBFJl939g3heMbM3qqr6u9SZxRIBHhQ9XcqfYy/EtJcjfwAcyboGLdvytf+wLa8LTh188La8JmZiuTYOBz3gbBSSXSeqqHATcTDpJdvlrpHvclQTOfF5x9Hsvpn10tHsVXevc6LWPTWzS2b2Ses3H4bI/nngSTmqQfwvh9NMVK0ZMzv+vOO5mV2tqurP5KKVfwBn87Tq7MzTCgAAAABJRU5ErkJggg==)](https://docs.openhrx.be)
[![OpenHRX Installation Guide](https://img.shields.io/badge/OpenHRX-Installation%20Guide-0047ab?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOVSURBVFhHrZc/bFdVFMfPeZYBQqpJm+hIKFSMQ9PFaOIiLJgy6GyauLKYEFkYlERXZGCtbRh0M0xU6IJhYZHB2GL8mWBkavljYhVqUsrn6/A7r73v9L0fv6qf5CXvvfs959x737nn3es2JJJelDRjZu+4+7SkQ2b2UjT/4e6/SfrBzG64+6K7rycX/w5gEpgHNjQkwAawAExmfxnPL2okHZD0mZl95O77Utuamf1iZr/HqzEzm3T3V5LuqZldcvdP3X2jbBsIcBRYSaPqAWclHc76GkmHgY+Bn5PtCnA061sBpoGHhfEqMCupytouJFXALLBa+HkITGdtgxh5Gfy6pPGsGxZJ4+Gj7ET7TEg6UE478JWkkayzfkdHgTPAN3GdAUazzvp+R8JX7XcZ2J91BnxRiK53BZd0DLhXawube5KOZb3tdKKciQsNQSy1zWhc7Zp2SfuAnxqRC6Ktq+PjdU4Am40lCiwUTmYblgXAqUbEFoCZbFcTyVzrFsyiwtVFJpZPZ7YD5xrRWgDOZbuaWB290G0Ao5WkGXevk2LO3Ul2JX/lFy10asL3XNzvN7NTBnxZDKCzyNhOrjwr9A2AZ53LLAAmCv2cSbodD6tZ3AZwsRG1ALiY9RlJDqyFyW0DHoXxzSxuI77jeeBxEfgxcH5Q/pQAN8PukQFb8XAlCwch6aCkt+M6mNsHAVyJmFtD9Tgj6ZCkE5Jei+tE7A/2zrCfIKrZaeBOPfUZ4A5wuqsY1TQ+wTBJCIwBt3LALoBbwFj2Yx1JuL0MgYlsYP0OXNtxPxzAtezH+r6OFJq5ysxuFO3vF/dmsW7d/WR+/zzc/WRHXXmvuP8ul+JeXkrAVGNoewCYKn2lUvxk+xcOzBdGjZ9RJN+vDc9DANyV9ELpK/2M5suGgb9j4C1gvRFhAMA68GbpI37Ha9G+uatkAxcKB0t5KcV2bRGgEa2APovZecziUqHb3pBsb8tjm/S9u78eRl+7+4fuvlVrQjdhZu+a2ZSZvRyv75vZj2b2bVVVd0u9pBFJl939g3heMbM3qqr6u9SZxRIBHhQ9XcqfYy/EtJcjfwAcyboGLdvytf+wLa8LTh188La8JmZiuTYOBz3gbBSSXSeqqHATcTDpJdvlrpHvclQTOfF5x9Hsvpn10tHsVXevc6LWPTWzS2b2Ses3H4bI/nngSTmqQfwvh9NMVK0ZMzv+vOO5mV2tqurP5KKVfwBn87Tq7MzTCgAAAABJRU5ErkJggg==)](https://docs.openhrx.be/install)
[![OpenHRX is licensed under AGPLv3](https://img.shields.io/badge/OpenHRX-AGPLv3-lightgray?logo=GPLv3)](LICENSE)


## Features



## Installation:

---
### Server:
#####  Available for:
[![Windows](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white)](#)
[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![macOS](https://img.shields.io/badge/macOS%20%28No%20installer%29-000000?logo=apple&logoColor=F0F0F0)](#)

##### Requires:
[![Python](https://img.shields.io/badge/Python3-3776AB?logo=python&logoColor=fff)](#)
[![Postgres](https://img.shields.io/badge/Postgres%2018%20%28Recommanded%29-%23316192.svg?logo=postgresql&logoColor=white)](#)
[![OpenHRX Official Website](https://img.shields.io/badge/OpenHRXv1-0047ab?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOVSURBVFhHrZc/bFdVFMfPeZYBQqpJm+hIKFSMQ9PFaOIiLJgy6GyauLKYEFkYlERXZGCtbRh0M0xU6IJhYZHB2GL8mWBkavljYhVqUsrn6/A7r73v9L0fv6qf5CXvvfs959x737nn3es2JJJelDRjZu+4+7SkQ2b2UjT/4e6/SfrBzG64+6K7rycX/w5gEpgHNjQkwAawAExmfxnPL2okHZD0mZl95O77Utuamf1iZr/HqzEzm3T3V5LuqZldcvdP3X2jbBsIcBRYSaPqAWclHc76GkmHgY+Bn5PtCnA061sBpoGHhfEqMCupytouJFXALLBa+HkITGdtgxh5Gfy6pPGsGxZJ4+Gj7ET7TEg6UE478JWkkayzfkdHgTPAN3GdAUazzvp+R8JX7XcZ2J91BnxRiK53BZd0DLhXawube5KOZb3tdKKciQsNQSy1zWhc7Zp2SfuAnxqRC6Ktq+PjdU4Am40lCiwUTmYblgXAqUbEFoCZbFcTyVzrFsyiwtVFJpZPZ7YD5xrRWgDOZbuaWB290G0Ao5WkGXevk2LO3Ul2JX/lFy10asL3XNzvN7NTBnxZDKCzyNhOrjwr9A2AZ53LLAAmCv2cSbodD6tZ3AZwsRG1ALiY9RlJDqyFyW0DHoXxzSxuI77jeeBxEfgxcH5Q/pQAN8PukQFb8XAlCwch6aCkt+M6mNsHAVyJmFtD9Tgj6ZCkE5Jei+tE7A/2zrCfIKrZaeBOPfUZ4A5wuqsY1TQ+wTBJCIwBt3LALoBbwFj2Yx1JuL0MgYlsYP0OXNtxPxzAtezH+r6OFJq5ysxuFO3vF/dmsW7d/WR+/zzc/WRHXXmvuP8ul+JeXkrAVGNoewCYKn2lUvxk+xcOzBdGjZ9RJN+vDc9DANyV9ELpK/2M5suGgb9j4C1gvRFhAMA68GbpI37Ha9G+uatkAxcKB0t5KcV2bRGgEa2APovZecziUqHb3pBsb8tjm/S9u78eRl+7+4fuvlVrQjdhZu+a2ZSZvRyv75vZj2b2bVVVd0u9pBFJl939g3heMbM3qqr6u9SZxRIBHhQ9XcqfYy/EtJcjfwAcyboGLdvytf+wLa8LTh188La8JmZiuTYOBz3gbBSSXSeqqHATcTDpJdvlrpHvclQTOfF5x9Hsvpn10tHsVXevc6LWPTWzS2b2Ses3H4bI/nngSTmqQfwvh9NMVK0ZMzv+vOO5mV2tqurP5KKVfwBn87Tq7MzTCgAAAABJRU5ErkJggg==)](https://www.openhrx.be)

#### For all systems:

- Download the latest version of OpenHRX from Releases
- Download the dependencies:
    - Python3

      Type in PowerShell/Terminal (Valid for all OSes) : `python3 --version`. If you get something like `Python 3.13.X`or higher you can skip Python installation. If you have got a lower version of Python or if you received an error, proceed to the installation.
    
    
    
        | OS                        | Command                                                   |
        | ------------------------- | --------------------------------------------------------- |
        | Windows (PowerShell)      | `winget install Python.Python.3`                          |
        | Linux (apt/Debian Based)  | ```sudo apt update``` <br/>```sudo apt install python3``` |
        | Linux (dnf/RedHat Based)  | `sudo dnf install python3`                                |
        | Linux (pacman/Arch Based) | ```sudo pacman -S python```<br/>```python --version```    |
        | macOS (Homebrew)          | `brew install python`                                     |

Type in PowerShell/Terminal (Valid for all OSes) : `python3 --version`. If you get something like `Python 3.13.X`or higher, you successfully installed Python3


- PostgreSQL



    Type in PowerShell/Terminal (Valid for all OSes) : `psql --version`. If you get an response or you have already PostgreSQL installed somewhere else you can skip PostgreSQL installation.
    
    
    
    | OS                        | Command                                                                                                                                                                                                  |
    | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Windows (PowerShell)      | `winget install PostgreSQL.PostgreSQL`                                                                                                                                                                   |
    | Linux (apt/Debian Based)  | ```sudo apt update```<br/>```sudo apt install postgresql postgresql-contrib```<br/>```sudo systemctl start postgresql```<br/>```sudo systemctl enable postgresql```                                      |
    | Linux (dnf/RedHat Based)  | ```sudo dnf install postgresql-server postgresql-contrib```<br/>```sudo postgresql-setup --initdb```<br/>```sudo systemctl start postgresql```<br/>```sudo systemctl enable postgresql```                |
    | Linux (pacman/Arch Based) | ```sudo pacman -S postgresql```<br/>```sudo -iu postgres initdb --locale $LANG -E UTF8 -D /var/lib/postgres/data```<br/>```sudo systemctl start postgresql```<br/>```sudo systemctl enable postgresql``` |
    | macOS (Homebrew)          | ```brew update```<br/>```brew install postgresql```<br/>```brew services start postgresql```                                                                                                             |
    
    
    
    Type in PowerShell/Terminal (Valid for all OSes) : `psql --version`. If you get a positive response, you successfully installed PostgreSQL









Find the installation steps on [OpenHRX official website](https://www.openhrx.be).





