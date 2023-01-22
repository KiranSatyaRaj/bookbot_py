# bookbot_py

BookBot is my first git project!

- It takes a text file as input and gives back the number of words and times each character found ordered from highest to lowest.


## Running it

- [Install the neccessary dependencies to run the program](https://gist.github.com/KiranSatyaRaj/1b99f51c3c5833132a14a923c945d3a5)
- fork and clone the repo
```bash
cd && git clone https://github.com/<Your-UserName>/bookbot_py.git
```
- change into project's directory and make a new books directory 
```bash
cd bookbot_py && mkdir && cd books
```
- You can add your own <file-name>.txt or download this [sample text](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt) in books directory and use it
- `cd ..` and change the [path](https://github.com/KiranSatyaRaj/bookbot_py/blob/main/main.py#L4) 
with the `books/<file-name>.txt` in [main.py](https://github.com/KiranSatyaRaj/bookbot_py/blob/main/main.py), and save it
- execute
```bash 
python main.py
```
