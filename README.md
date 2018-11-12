Pathogen
=========

This role installs tpopes pathogen to your machine.

Requirements
------------

It is assumed you already have `vim` installed.

Role Variables
--------------

```
---
plugins:
  - repo: "https://github.com/hashivim/vim-terraform.git"
    name: "vim-terraform"
    version: master
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```
---
- name: install pathogen 
  hosts: all
  roles:
    - role: pathogen
```

License
-------

BSD
