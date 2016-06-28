from __future__ import print_function
#!/usr/bin/env python

# OS related imports
from os import remove
from shutil import rmtree

# Script related templates
from jinja2 import Environment

# Delete files if they are already deployed
def clean_jhub_environment():
    """
    Clean the work environment by making sure that:
        - No `Vagrant` file is present
        - If a `Vagrant` file is present, remove the VM's before deletion
        - No `.vagrant` folder is present
        - No `inventory` file is present.
    """
    files = ['Vagrant', 'ansible.cfg', 'ssh.config']
    folders = ['.vagrant', 'inventory']

    def delete(f, func=remove):
        """
        Funcion to dlete files or folders
        """
        try:
            func(f)
        except OSError as e:
            print("File " + f + ": " + e.strerror)

    for f in files:
        delete(f, func=remove)

    for f in folders:
        delete(f, func=rmtree)



# Copy:
#   - Vagrant
#   - ansible.cfg
#   - ssh.config

# Read dictionary with servers

# Create Jinja2 tempates

# Copy Jinja2 templates

def main():
    clean_jhub_environment()


if __name__ == '__main__':
    main()
