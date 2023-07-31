
# Git Alias Manager

This Python script allows you to manage Git aliases easily by adding or removing them globally. It utilizes the `subprocess` module to execute Git commands for setting and removing aliases.


## Requirements

Before running the script, make sure you have the following:
- Python 3.x
- Subprocess module (pre-installed with python)




## How to use
- Open a terminal or command prompt.
- Navigate to the directory containing the git_alias_manager.py script.
- Execute the script using the following command:
```bash
python git_alias_manager.py
```
- The script will automatically set the aliases defined in the alias_dict dictionary. Uncomment the line remove_git_alias(key) if you wish to remove the aliases after they have been set.

## Alias Definitions

In the script, the alias_dict dictionary is used to define the aliases you want to set globally. Each key-value pair represents an alias, where the key is the alias name, and the value is the corresponding Git command or sequence of commands. You can modify this dictionary to add or remove aliases as needed.

```python
alias_dict = {
    "a" : r"add -A",
    "acm" : r"!git add -A && git commit -m",
    "ll" : r"log --oneline",  
    "mc" : r"commit -m",
    "rh" : r"reset --hard",
    "s" : r"status",
    "se" : r"log --grep"
}
```
- `"a": "git add -A"`: The alias a allows you to stage all changes in the working directory using `git add -A`.
- `"acm": "git add -A && git commit -m"`: The alias acm combines staging all changes and making a commit with a default commit message using `git add -A && git commit -m <message>`.
- `"ll": "git log --oneline"`: The alias ll allows you to view the commit history with concise, one-line log entries using `git log --oneline`.
- `"mc": "git commit -m"`: The alias mc allows you to make a commit with a custom commit message using `git commit -m <message>`.
- `"rh": "git reset --hard"`: The alias rh allows you to perform a hard reset, which discards all changes and resets the branch to the commit specified, using `git reset --hard <hex-code>`.
- `"s": "git status"`: The alias s allows you to check the status of the repository, displaying information about tracked and untracked files, as well as the current branch status using git status.
- `"se": "git log --grep"`: The alias se allows you to filter the commit history based on a specific search pattern using `git log --grep <commit-name>`.

## Disclaimer

Be aware of the potential risks associated with executing scripts that interact with your version control system. Use this script at your own risk, and always review the code to ensure it meets your specific requirements.

## Acknowledgement

Happy downloading! If you encounter any issues or have suggestions for improvements, feel free to [open an issue](https://github.com/phanitallapudi/Git-Alias-Manager/issues) or contribute to the project by creating a pull request.