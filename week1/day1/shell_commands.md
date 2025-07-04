# BASIC SHELL COMMANDS
Shell commands are instructions you type into a command-line interface (CLI) like Bash, Zsh, or Terminal to interact with your operating system. It allows us to navigate through directories,manage files and folders,run programs and scripts,monitor system performance all using plain text commands.

## Common commands
| Command | Description | Example | Output |
|---------|-------------|---------|--------|
| `echo` | Prints text or variables to the terminal | `echo "Hello, World!"` | Hello, World! |
| `whoami` | Displays the current logged-in user | `whoami` | *Displays the user* |
| `man` | Opens the manual/help page for a command | `man ls` | *opens the manual for `ls`* |
| `history` | Shows a list of previously used commands | `history` | 1  cd Documents <br> 2  ls -la |
| `clear` | Clears the terminal screen | `clear` | *Terminal is cleared* |
| `exit` | Exits the current shell session | `exit` | *Closes terminal or shell* |
| `date` | Displays the current date and time | `date` | Mon Jun 16 10:22:30 IST 2025 |
| `cal` | Shows the current month’s calendar | `cal` | *Displays a full month calendar* |
| `uname` | Prints system info (use `-a` for all details) | `uname -a` | *Displays the system info* |
| `uptime` | Shows how long the system has been running | `uptime` | 10:22:30 up 1:15, 2 users, load avg: 0.36 |
| `sleep` | Pauses for a specified number of seconds | `sleep 5` | *Waits for 5 seconds* |
| `read` | Takes user input from the terminal | `read name` | *(Waits for input, stores in `name`)* |
| `alias` | Creates shortcuts for commands | `alias ll='ls -l'` | Defines alias, without defining output |
| `pwd` | Print name of current/working directory | `pwd` | *prints current location* |
| `cd` | For changing the directory | `cd <dir>` | *gets into new folder named fol_name* |
| `ls` | List all files inside the directory or a folder | `ls Documents` | test.txt <br> home.txt |

There are variations for ls command:
* `-a`: it lists all files inside a file or directory along withthe hidden folders in it.
* `-al` : shows all hidden files along with other files in a long format

In case of cd command as well:
* `.` (current directory). This is the directory you are currently in.
* `..` (parent directory). Takes you to the directory above your current directory. Such as /home(directory above this).
* `~` (home directory). This directory defaults to your “home directory”. Such as /home/pete.
* `-` (previous directory). This will take you to the previous directory you were just at,shows the directory before we are in.
---
##  File & Directory Management

| Command | Description | Example | Output |
|---------|-------------|---------|--------|
| `file <file>` |  Determines the actual type of a file based on content, not extension | `file input.txt`| *Displays type of file like ASCII text* |
| `mkdir <dir>` | Create a new directory | `mkdir myFolder` | *Creates a folder named `myFolder`* |
| `rmdir <dir>` | Remove an empty directory | `rmdir myFolder` | *Removes `myFolder` if it's empty* |
| `rm -r <dir>` | Remove directory & contents | `rm -r myFolder` | *Deletes folder and all inside it* |
| `touch <file>` | Create a new empty file | `touch notes.txt` | *Creates file `notes.txt`* |
| `cp <src> <dest>` | Copy file or folder | `cp a.txt b.txt` | *Copies `a.txt` to `b.txt`* |
| `mv <src> <dest>` | Move or rename | `mv file.txt folder/` | *Moves file to folder* |
| `rm <file>` | Delete a file | `rm old.txt` | *Deletes `old.txt`* |

For rm command there are flags like:
* `-f` : removes all files in directory whether they are protected or not, without prompting user.
* `-i` : removes files only after giving a prompt whether we want to delete them for sure or not.
in general `-i` flags always prompts us before overwriting, deleting etc and we can use `-b` for making a backup.
---

##  Viewing & Editing Files

| Command | Description | Example | Output |
|---------|-------------|---------|--------|
| `cat <file>` | Show content | `cat notes.txt` | Displays all text in `notes.txt` |
| `less <file>` | Scrollable view | `less notes.txt` | Opens file with scroll support |
| `head <file>` | First 10 lines | `head notes.txt` | Shows first 10 lines |
| `tail <file>` | Last 10 lines | `tail notes.txt` | Shows last 10 lines |
| `nano <file>` | Edit in Nano | `nano notes.txt` | Opens `notes.txt` in Nano editor |
| `vi <file>` | Open in Vim | `vi notes.txt` | Opens `notes.txt` in Vim editor |

 Using a `cat` command we can also merge 2 files and show their combined contents as well only we need to specify thier names.

---

##  Searching

| Command | Description | Example | Output |
|---------|-------------|---------|--------|
| `find . -name "<name>"` | Find file by name | `find . -name "main.py"` | `./project/main.py` |
| `grep "<text>" <file>` | Search text in file | `grep "error" log.txt` | Shows lines with "error" |
| `grep -r "<text>" <dir>` | Recursive search | `grep -r "TODO" src/` | Lists all TODOs in `src/` |

For `grep` command , we can use flags like:
* `-i`: for making words searching to be case-insensitive.
---

## Input and Output
There are mainly 3 data streams : stdin,stdout and stderr.
| Stream | Name | Description | 
|--------|------|-------------|
| `stdin` | Standard Input | Takes input from keyboard or another command | 
| `stdout` | Standard Output | Displays output (usually to terminal) | 
| `stderr` | Standard Error | Displays error messages |



###  Redirection Operators

| Symbol | Purpose | Example | Meaning |
|--------|---------|---------|---------|
| `>` | Redirect stdout to a file | `echo Hello,World > files.txt` | Saves Hello,World  to `files.txt` |
| `>>` | Append stdout to file | `echo "log" >> log.txt` | Appends log to file instead of overwriting |
| `<` | Redirect file to stdin | `wc -l < file.txt` | Sends word count,content of `file.txt` as input |
| `2>` | Redirect stderr | `cat nofile 2> error.txt` | Saves error message to `error.txt` |
| `2>&1` | Merge stderr into stdout | `command > out.txt 2>&1` | Combines both outputs in one file |
---
## Permissins Control
| Command | Description | Example | Output |
|---------|-------------|---------|--------|
| `ls -l` | List files with permissions | `ls -l file.txt` | `-rw-r--r-- 1 user user 1234 date file.txt` |
|`chmod u+x <file>`| Adds executable permission to file | `chmod u+x myfile` | Adds x as well in permissions |
| `chmod u-x <file>`| Removes executable permission from the file | `chmod u-x myfile` | Removes x from permissions |
| `chmod 755 <file>` | Set permissions to `rwxr-xr-x` | `chmod 755 app` | `-rwxr-xr-x` |
| `chown user <file>` | Change file owner | `chown ramya notes.txt` | Ownership changed to `ramya` |
| `chown user:group <file>` | Change file owner and group | `chown ramya:dev script.sh` | Owner and group updated |
| `ls -ld <dir>` | View permissions of a directory | `ls -ld myfolder` | `drwxr-xr-x 2 ramya ramya ... myfolder` |
---
