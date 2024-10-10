---
title: Ansible
layout: default
---
### Simple playbook

```yaml
---
- hosts: all
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
```

### Inventory example

hosts.ini

```ini
[webservers]
server1 ansible_host=192.168.1.10 ansible_user=root
server2 ansible_host=192.168.1.11 ansible_user=root
```


### Several OS example
```yaml

---
# tasks file for mysql

- name: Ubuntu MYSQL install
  include_tasks: "debian_mysql.yml"
  when: ansible_os_family == "Debian"

- name: Centos MYSQL install
  include_tasks: "redhat_mysql.yml"
  when: ansible_os_family == "RedHat"

```


### Tree of simple playbook structure

```shell

.
├── ansible.cfg
├── files
│   └── playbook.yml
├── hosts.ini
├── playbook.yml
├── roles
    ├── ansible
    │   ├── README.md
    │   ├── defaults
    │   │   └── main.yml
    │   ├── files
    │   ├── handlers
    │   │   └── main.yml
    │   ├── meta
    │   │   └── main.yml
    │   ├── tasks
    │   │   └── main.yml
    │   ├── templates
    │   ├── tests
    │   │   ├── inventory
    │   │   └── test.yml
    │   └── vars
    │       └── main.yml
    └── python
        ├── README.md
        ├── defaults
        │   └── main.yml
        ├── files
        ├── handlers
        │   └── main.yml
        ├── meta
        │   └── main.yml
        ├── tasks
        │   └── main.yml
        ├── templates
        ├── tests
        │   ├── inventory
        │   └── test.yml
        └── vars
            └── main.yml

```

<div class="button-container">
    <a href="/" class="button">Back to Main</a>
</div>


