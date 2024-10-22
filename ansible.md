# Ansible Cheat Sheet

![Ansible Version](https://img.shields.io/badge/Ansible-2.10+-blue.svg)

## Table of Contents
- [requirements.yml](#requirements.yml)
- [hosts.ini](#hosts.ini)
- [ansible.cfg](#ansible.cfg)
- [loops](#loops)
- [ways to speed up ansible](#ways_to_speed_up_ansible)
- [vault.yml](#vault.yml)
- [adhoc](#adhoc)
- [ansible-bender (buildah)](#ansible-bender)
- [ansible-lint](#ansible-lint)

---

<a name="requirements.yml"></a> 
### Examplefile of requirements.yml

```yml
---

roles:
 - src: geerlingguy.postgresql


 - name: green.mongodb
   src: https://github.com/UnderGreen/ansible-role-mongodb
   version: 1.0.0

collections:
 - name: community.postgresql
```

### install roles from requirements.yml

```bash
ansible-galaxy install -r requirements.yml
```

### install collections from requirements. yml

```bash
ansible-galaxy collection install -r requirements.yml

```

<a name="hosts.ini"></a> 
### Examplefile of hosts.ini

```ini
[centos]
centos_server ansible_host=192.168.51.3

[ubuntu]
ubuntu_server ansible_host=192.168.51.4

[no_python]
ubuntu_no_python_server ansible_host=192.168.51.2

[centos_python]
centos_python_server ansible_host=192.168.51.5
```

<a name="ansible.cfg"></a> 
### Examplefile of ansible.cfg

```ini
[default]
inventory=./hosts.ini
private_key_file=/home/vagrant/.ssh/vagrant_test
host_key_checking=false
```

<a name="loops"></a>
## loops
### Examplefile: start python script several times
```yml
---
- name: Exclude hosts from prod
  hosts: localhost
  gather_facts: true
  pre_tasks:
    - name: Exclude server from production
      delegate_to: 127.0.0.1
      command: "python3 files/setup.py {{ item }}"
      loop: "{{ range(10) | list }}"
      register: command_result
      failed_when: "'failure' in command_result.stdout"
      changed_when: "'success' in command_result.stdout"

  tasks:
    - name: "Print os family"
      ansible.builtin.debug:
        msg: "OS family is {{ ansible_os_family }} and python is {{ ansible_python_version }}"
```

<a name="ways_to_speed_up_ansible"></a> 
## Ways to speed up Ansible

### Pipelining
```cfg
[default]
pipelining = true
```

```yml
---

- name: "install gitlab from role"
  hosts: "gitlab_main"
  become: true
  vars:
   gitlab_domain: "test-gitlab.test"
   ansible_ssh_pipelining: true
  roles:
   - geerlingguy.gitlab
```

### Forks
### In ansible.cfg
```cfg
[default]
forks = 100 # maximum number of threads
```

### Highlight the number of simultaneous streams for playbook
### In playbook.yml
```yml
---

- name: "install gitlab from role"
  hosts: "gitlab_main"
  become: true
  serial: "3" # number of threads for current playbook 
  vars:
   gitlab_domain: "test-gitlab.test"
   ansible_ssh_pipelining: true
  roles:
   - geerlingguy.gitlab
```

### Highlight the number of simultaneous streams for current task
```yml
---

- name: "install gitlab from role"
  hosts: "gitlab_main"
  become: true
  serial: "3" # number of threads for current playbook 
  vars:
   gitlab_domain: "test-gitlab.test"
   ansible_ssh_pipelining: true
  roles:
   - geerlingguy.gitlab
  tasks:
  - name: "throttle"
    ansible.builtin.debug:
      msg: "test"
    throttle: 5 # number of threads for current task
```

## Parallel execution strategies

Linear

Debug

Free - the fastest (the hosts are not waiting for each other)

Host pinned

P.S. These are plugins, you can write your own strategies.

## Two ways to configure strategies (and import plugins)
### In ansible.cfg
```cfg
[default]
stratedy_plugins = /usr/share/ansible/plugins/strategy
action_plugins = /usr/share/ansible/plugins/action
inventory_plugins = /usr/share/ansible/plugins/inventory
# etc...

strategy = linear
```

### In playbook.yml
```yml
---

- name: "strategies"
  strategy: free
  serial: "30%"
  tasks:
  - name: "Msg"
    ansible.builtin.debug:
      msg: "Hi!"

```

## Multiplexing
```cfg
[default]
stratedy_plugins = /usr/share/ansible/plugins/strategy
action_plugins = /usr/share/ansible/plugins/action
inventory_plugins = /usr/share/ansible/plugins/inventory
# etc...

strategy = linear
forks = 30

[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
```

## Async tasks
```yml
---

- name: Run an async task
  ansible.builtin.yum:
    name: docker-io
    state: present
  async: 1000
  poll: 0 # (if > 0 - not async)
  register: yum_sleeper

- name: Check on an async task
  async_status:
    jid: "{{ yum_sleeper.ansible_job_id }}"
  register: job_result
  until: job_result.finished
  retries: 100
  delay: 10
```

## Defining an assembly of facts

/etc/ansible/facts.d or local facts

All - all facts about a machine

Min - minimal facts about a machine

Hardware - info about hardware (very slow)

Network - about network interfaces

Virtual - about network adapters

All facts can be combined 
```yml
---

- name: "strategies"
  strategy: free
  serial: "30%"
  max_fail_percentage: "80%" # if 80% failed, then strategy off and go without strategy
  tasks:
  - name: Collect only facts returned by Network
    ansible.builtin.setup:
      gather_subset:
        - '!all'
        -  network

  - name: Collect only selected facts
    ansible.builtin.setup:
      filter:
       - 'ansible_distribution' 
       - 'ansible_machine_id'
       - 'ansible_*_mb'
```

## Special plugins

### Mitogen - all task in one thread in one python, the growth rate is from 1.25 to 7 times
Installing mitogen: mitogen.networkgenomics.com/ansible_detailed.html

## Callbacks (measuring the execution time)
```cfg
[default]
strategy = linear

forks = 30

stdout_callback = default
callback_enabled = timer, mail, profile_roles, collection_namespace.collection_name.custom_callback


[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
```

<a name="vault.yml"></a> 
## vault.yml
```yml
db_user: "mydbuser"
db_password: "secretpassword"
api_key: "yourapikey"
```
Encrypt vault.yml:

ansible-vault encrypt vault.yml

Use vault.yml in playbook:

```yml
---
- name: Example playbook using Vault
  hosts: all
  vars_files:
    - vault.yml  # подключаем зашифрованные переменные

  tasks:
    - name: Print database user
      debug:
        var: db_user

    - name: Print API key
      debug:
        var: api_key
```
Run playbook with vault.yml:

```bash
ansible-playbook playbook.yml --ask-vault-pass
```

Edit vault.yml:

```bash
ansible-vault edit vault.yml
```
Use file with password:

```bash
ansible-playbook playbook.yml --vault-password-file vault_pass.txt
```

<a name="adhoc"></a>
## adhoc
### adhoc shell

```bash
ansible all -m shell -a "uptime > ~/test/test.txt" -u your_user

ansible test -m shell -a "uptime"

ansible -m shell -a "uptime" -i hosts.ini

ansible web_servers -m shell -a "touch /tmp/testfile" -u your_user

ansible all -m shell -a "free -m"
```

### adhoc command

```bash
ansible all -m command -a "uptime" -u your_user
```

### adhoc ping

```bash
ansible all -m ping
```

### adhoc apt

```bash
ansible all -m apt -a "update_cache=yes upgrade=yes"
ansible all -m apt -a "name=htop state=present"

ansible all -m yum -a "name=* state=latest"
ansible all -m yum -a "name=htop state=present"

ansible all -m apt -a "update_cache=yes cache_valid_time=3600"
ansible all -m yum -a "name=* state=present"
```

### adhoc file

```bash
ansible all -m file -a "path=/tmp/testfile state=touch"

ansible all -m file -a "path=/tmp/testfile state=absent"

ansible all -m file -a "path=/tmp/testfile owner=root group=root mode=0644"
```

### adhoc systemd

```bash
ansible all -m systemd -a "name=nginx state=restarted" --become

ansible all -m systemd -a "name=nginx state=stopped" --become
```

### adhoc user

```bash
ansible all -m user -a "name=newuser state=present"
```

### adhoc copy

```bash
ansible all -m copy -a "src=/local/path/to/file dest=/remote/path/to/file"
```

### adhoc setup

```bash
ansible all -m setup -a "filter=ansible_default_ipv4.address"
```

### adhoc script

```bash
ansible all -m script -a "/path/to/local/script.sh"
```

<a name="ansible-bender"></a>
## ansible-bender
### Setup for buildah and controlnode

think about how to install the six moves module

```ruby
ENV['VAGRANT_SERVER_URL'] = 'https://vagrant.elab.pro'
Vagrant.configure("2") do |config|

  config.vm.provision "file", source: "files/vagrant_test.pub", destination: "/home/vagrant/.ssh/"

  config.vm.define "controlnode" do |controlnode|
    controlnode.vm.box = "ubuntu/focal64"
    controlnode.vm.hostname = "controlnode"
    controlnode.vm.network "private_network", ip: "192.168.50.4"
    controlnode.vm.synced_folder "./files","/home/vagrant/files"
    controlnode.vm.provision "file", source: "files/vagrant_test", destination: "/home/vagrant/.ssh/"
    controlnode.vm.provision "shell", inline: <<-SHELL
      sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/#g' /etc/ssh/sshd_config
      service ssh restart
      sudo apt update && sudo apt -y install ansible python3-pip
      sudo pip3 install ansible-bender
      chmod 600 /home/vagrant/.ssh/vagrant_test
      chmod 644 /home/vagrant/.ssh/vagrant_test.pub
      sudo bash /home/vagrant/files/podman_buildah.sh
    SHELL
  end
end
```

podman_buildah.sh (ubuntu install)

```bash
#!bin/bash

# prereq packages
sudo apt-get update
sudo apt-get install -y wget ca-certificates gnupg2

# add repo and signing key
VERSION_ID=$(lsb_release -r | cut -f2)
echo "deb http://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/ /" | sudo tee /etc/apt/sources.list.d/devel-kubic-libcontainers-stable.list
curl -Ls https://download.opensuse.org/repositories/devel:kubic:libcontainers:stable/xUbuntu_$VERSION_ID/Release.key | sudo apt-key add -
sudo apt-get update

# install buildah and podman
sudo apt install buildah podman -y

# fix known issue 11745 with [machine] entry
sudo sed -i 's/^\[machine\]$/#\[machine\]/' /usr/share/containers/containers.conf

```

### Example playbook.yml

```yml
- name: Demonstration of ansible-bender functionality
  hosts: localhost
  vars:
    ansible_bender:                # Все переменные для контейнеров мы помещаем в переменную
      base_image: python:3-alpine   # Укажем базовый Docker образ
      working_container:
        volumes:
          - '{{ playbook_dir }}:/src'  # На рабочий контейнер смонтируем директорию playbook_dir
      target_image:
        name: a-very-nice-image        # Определим имя итогового контейнера
        working_dir: /src              # Рабочая директория для запуска скриптов
        labels:
          built-by: 'root'             # Метаданные
      environment:
        FILE_TO_PROCESS: README.md     # Переменные окружения, например, файл для обработки
  tasks:                               # Эти таски выполнятся ВНУТРИ контейнера, который будет запечен как Docker image
    - name: Run a sample command
      ansible.builtin.command: 'ls -lha /src'

    - name: Stat a file
      ansible.builtin.stat:
        path: "{{ ansible_bender.environment.FILE_TO_PROCESS }}" # Проверка файла, на который указывает переменная окружения
```

### Start ansible-bender playbook

```bash
ansible-bender build playbook.yml
```
### List of containers via bender

```bash
ansible-bender list-builds
```
### Logs of build bender

```bash
ansible-bender get-logs
```

<a name="ansible-lint"></a>
## Ansible-lint

https://ansible.readthedocs.io/projects/lint/usage/

```bash
sudo apt-get -y install ansible-lint 

ansible-lint --version

ansible-lint playbook.yml
```

