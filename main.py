import subprocess

def set_git_alias(alias_name: str, alias_command: str) -> None:
    '''This code defines a function to set a global Git alias using the subprocess module.'''
    try:
        git_config_command = f'git config --global alias.{alias_name} "{alias_command}"'
        subprocess.run(git_config_command, shell=True, check=True)
        print(f"Git alias '{alias_name}' has been set globally.")
    except subprocess.CalledProcessError as e:
        print("Error setting Git alias:")
        print(e.stderr)

def remove_git_alias(alias_name: str) -> None:
    '''The code defines a function to remove a global Git alias, using subprocess to run Git commands.'''
    try:
        git_config_command = f'git config --global --unset alias.{alias_name}'
        subprocess.run(git_config_command, shell=True, check=True)
        print(f"Git alias '{alias_name}' has been removed globally.")
    except subprocess.CalledProcessError as e:
        print("Error removing Git alias:")
        print(e.stderr)

alias_dict = {
    "a" : r"add -A",                            #adds all the files
    "acm" : r"!git add -A && git commit -S -m",    #adds and commit the files with a message
    "ll" : r"log --oneline",                    #displays concise commit history with abbreviated hashes and commit messages.
    "mc" : r"commit -m",                        #commit files with a message
    "rh" : r"reset --hard",                     #discards all changes and resets to the specified commit if not previous commit, removing untracked files.
    "s" : r"status",                            #shows the current status of the repository.
    "se" : r"log --grep"                        #shows commit history filtered by a specific search pattern in commit messages.
}

if __name__ == "__main__":
    for key, value in alias_dict.items():
        set_git_alias(key, value)
        #remove_git_alias(key)
