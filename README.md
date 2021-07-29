# CrazyMouse
### Did your co-worker forget to lock the computer again when he left the room?
## Run Crazy_Mouse.exe on his/her computer!


**What does it do?**

This is a very simple piece of Python code that uses a [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/), time and random python library to move the mouse randomly on the screen forever (or until the computer restarts).

**Why did I write this?**

My co-workers took over my computer when I left the room for a few moments, and I was looking for a creative way to avenge them.

**H E L P !!!, someone installed it for me on the computer, how do I disable it?**

It's really simple, you can close the program via Windows Task Manager or by restarting your computer.

###### (If this keeps happening, then your co-worker is very creative and he made sure to run it while the computer boots.)

**Is it a virus?**

No.

**Will it encrypt my hard disk?**

No.

**Does the software collect sensitive information?**

No. it just moves the mouse.

**Is it a virus?**

I already said, no.

**Is the exe file signed?**

No, I wanted to avoid instances of someone accidentally distributing the file via GPO to the entire organization. (But if this happens to you, [please let me know how the Helpdesk staff responded](https://github.com/Burekasim/CrazyMouse/issues/new "please let me know how the Helpdesk staff responded")).

**How do I compile the python file?**

Using [pyinstaller](https://www.pyinstaller.org/ "pyinstaller") library, you can build the exe by running:

`pyinstaller.exe --onefile --windowed crazy_mouse.py`
