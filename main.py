import subprocess

def set_git_alias(alias_name, alias_command):
    try:
        git_config_command = f'git config --global alias.{alias_name} "{alias_command}"'
        subprocess.run(git_config_command, shell=True, check=True)
        print(f"Git alias '{alias_name}' has been set globally.")
    except subprocess.CalledProcessError as e:
        print("Error setting Git alias:")
        print(e.stderr)

def remove_git_alias(alias_name):
    try:
        git_config_command = f'git config --global --unset alias.{alias_name}'
        subprocess.run(git_config_command, shell=True, check=True)
        print(f"Git alias '{alias_name}' has been removed globally.")
    except subprocess.CalledProcessError as e:
        print("Error setting Git alias:")
        print(e.stderr)


alias_dict = {
    "a" : r"add -A",
    "acm" : r"!git add -A && git commit -m",
    "ll" : r"log --oneline",  
    "mc" : r"commit -m",
    "rh" : r"reset --hard",
    "s" : r"status",
    "se" : r"log --grep"
}

for key, value in alias_dict.items():
    set_git_alias(key, value)
    #remove_git_alias(key)

