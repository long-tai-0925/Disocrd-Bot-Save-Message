# Disocrd-Bot-Save-Message
#### Notice! Using this code maybe violate Discord ToS

## The following are the steps to use
1. Download [
Disocrd-Bot-Save-Message](https://github.com/Coca-Sprite/Disocrd-Bot-Save-Message/blob/main/main.py) in ur server or computer  
2. 
```
pip install datetime
```
3. 
```
pip install discord.py
```
4. Replace "Your_Token" with your Token    
5. Use **admin** run the code(Prevent messages from being saved due to insufficient permissions)

## If there is insufficient permission, it may result in the following error:  
1.
```py
Ignoring exception in on_message
Traceback (most recent call last):
  File "Ur Discord.py install file", line 343, in _run_event
    await coro(*args, **kwargs)
  File "file.py", line 42, in on_message
    with open(f"./All_Message.txt", "a", encoding='utf8') as log:
FileNotFoundError: [Errno 2] No such file or directory: './All_Message.txt'
```   
2.[*Closing without reason*]

