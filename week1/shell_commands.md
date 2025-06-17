# BASIC SHELL COMMANDS
Shell commands are instructions you type into a command-line interface (CLI) like Bash, Zsh, or Terminal to interact with your operating system. It allows us to navigate through directories,manage files and folders,run programs and scripts,monitor system performance all using plain text commands.
| Command | Description | Example | Output |
|---------|-------------|---------|--------|
| `echo` | Prints text or variables to the terminal | `echo "Hello, World!"` | Hello, World! |
| `clear` | Clears the terminal screen | `clear` | *Terminal is cleared* |
| `man` | Opens the manual/help page for a command | `man ls` | *opens the manual for `ls`* |
| `history` | Shows a list of previously used commands | `history` | 1  cd Documents <br> 2  ls -la |
| `exit` | Exits the current shell session | `exit` | *Closes terminal or shell* |
| `date` | Displays the current date and time | `date` | Mon Jun 16 10:22:30 IST 2025 |
| `cal` | Shows the current month’s calendar | `cal` | *Displays a full month calendar* |
| `whoami` | Displays the current logged-in user | `whoami` | *Displays the user* |
| `uname` | Prints system info (use `-a` for all details) | `uname -a` | *Displays the system info* |
| `uptime` | Shows how long the system has been running | `uptime` | 10:22:30 up 1:15, 2 users, load avg: 0.36 |
| `sleep` | Pauses for a specified number of seconds | `sleep 5` | *Waits for 5 seconds* |
| `read` | Takes user input from the terminal | `read name` | *(Waits for input, stores in `name`)* |
| `alias` | Creates shortcuts for commands | `alias ll='ls -l'` | Defines alias, without defining output |
