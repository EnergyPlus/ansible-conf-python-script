from __future__ import print_function
#!/usr/bin/env python

# OS related imports
import os
import shutil

# Script related templates
from jinja2 import Environment

TEMPLATE_FILES = ['inventory', 'servers.yml']
ANSIBLE_FILES = ['ansible.cfg', 'ssh.config']
VAGRANT_FILES = ['Vagrantfile']
FILES = ANSIBLE_FILES + VAGRANT_FILES + TEMPLATE_FILES

FOLDERS = ['.vagrant']

# Delete files if they are already deployed
def delete_conf(pwd):
    """
    Clean the work environment by making sure that:
        - No `Vagrant` file is present
        - If a `Vagrant` file is present, remove the VM's before deletion
        - No `.vagrant` folder is present
        - No `inventory` file is present.
    """
    files = FILES
    folders = FOLDERS

    def delete(f, func=os.remove):
        """
        Funcion to delete files or folders in `pwd`
        """
        try:
            func(f)
        except OSError as e:
            print("DELETE: " + f + ", " + e.strerror)

    for f in files:
        delete(os.path.join(pwd, f), func=os.remove)

    for f in folders:
        delete(os.path.join(pwd, f), func=shutil.rmtree)

def copy_conf(pwd):
    """
    Place configuration files to manage Ansible ssh conections.
    """
    orig = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static_files')
    files = ANSIBLE_FILES + VAGRANT_FILES

    def copy(f, orig, dest):
        try:
            shutil.copy(os.path.join(orig, f), \
                        os.path.join(dest, f))
        except FileNotFoundError as e:
            print("COPY: " + f + ", " + e.strerror)

    for f in files:
        copy(f, orig, pwd)

# Copy:
#   - Vagrant
#   - ansible.cfg
#   - ssh.config

# Read dictionary with servers

# Create Jinja2 tempates

# Copy Jinja2 templates



def main():
    pwd = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
    delete_conf(pwd)
    copy_conf(pwd)


PWD=os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    main()
