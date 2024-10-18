# Vagrant Cheat Sheet

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-blue)

## Table of Contents
- [Vagrant plugins](#Vagrant-plugins)
- [Vagrantfile](#Vagrantfile)

---

<a name="Vagrant-plugins"></a> 
## Vagrant-plugins

### Vagrant plugin install

```bash
vagrant plugin install --plugin-clean-sources --plugin-source https://rubygems.org vagrant-vbguest
```

<a name="Vagrantfile"></a> 
## Vagrantfile

### Examplefile

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

ENV['VAGRANT_SERVER_URL'] = 'https://vagrant.elab.pro'
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  config.vm.provision "file", source: "files/vagrant_test.pub", destination: "/home/vagrant/.ssh/"

  config.vm.define "controlnode" do |controlnode|
    controlnode.vm.box = "ubuntu/focal64"
    controlnode.vm.hostname = "controlnode"
    controlnode.vm.network "private_network", ip: "192.168.50.4"
    controlnode.vm.synced_folder "./ansible","/home/vagrant/ansible"
    controlnode.vm.synced_folder "./files","/home/vagrant/"
    controlnode.vm.provision "file", source: "files/vagrant_test", destination: "/home/vagrant/.ssh/"
    controlnode.vm.provision "file", source: "files/exclude_from_prod.py", destination: "/home/vagrant/"
    controlnode.vm.provision "file", source: "files/include_to_prod.py", destination: "/home/vagrant/"
    controlnode.vm.provision "shell", inline: <<-SHELL
      sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/#g' /etc/ssh/sshd_config
      service ssh restart
      sudo apt update && sudo apt --assume-yes install ansible
      chmod 600 /home/vagrant/.ssh/vagrant_test
      chmod 644 /home/vagrant/.ssh/vagrant_test.pub
    SHELL
  end

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.define "server_postgres_master" do |server_postgres_master|
    server_postgres_master.vm.box = "centos/8"
    server_postgres_master.vm.hostname = "server-postgres-master"
    server_postgres_master.vbguest.auto_update = false
    server_postgres_master.vm.network "private_network", ip: "192.168.51.2"
    server_postgres_master.vm.provision "shell", inline: <<-SHELL
      chmod 644 /home/vagrant/.ssh/vagrant_test.pub
      chmod 755 /home/vagrant/exclude_from_prod.py
      chmod 755 /home/vagrant/include_to_prod.py
      cat /home/vagrant/.ssh/vagrant_test.pub >> /home/vagrant/.ssh/authorized_keys
      sed -i s/mirror.centos.org/vault.centos.org/g /etc/yum.repos.d/CentOS-*.repo
      sed -i s/^#.*baseurl=http/baseurl=http/g /etc/yum.repos.d/CentOS-*.repo
      sed -i s/^mirrorlist=http/#mirrorlist=http/g /etc/yum.repos.d/CentOS-*.repo
    SHELL
  end

  config.vm.define "server_postgres_slave" do |server_postgres_slave|
    server_postgres_slave.vm.box = "centos/8"
    server_postgres_slave.vm.hostname = "server-postgres-slave"
    server_postgres_slave.vbguest.auto_update = false
    server_postgres_slave.vm.network "private_network", ip: "192.168.51.3"
    server_postgres_slave.vm.provision "shell", inline: <<-SHELL
      chmod 644 /home/vagrant/.ssh/vagrant_test.pub
      cat /home/vagrant/.ssh/vagrant_test.pub >> /home/vagrant/.ssh/authorized_keys
    SHELL
  end

  config.vm.define "server_mongo_primary" do |server_mongo_primary|
    server_mongo_primary.vm.box = "centos/8"
    server_mongo_primary.vm.hostname = "server-mongo-primary"
    server_mongo_primary.vbguest.auto_update = false
    server_mongo_primary.vm.network "private_network", ip: "192.168.52.2"
    server_mongo_primary.vm.provision "shell", inline: <<-SHELL
      chmod 644 /home/vagrant/.ssh/vagrant_test.pub
      cat /home/vagrant/.ssh/vagrant_test.pub >> /home/vagrant/.ssh/authorized_keys
      sed -i s/mirror.centos.org/vault.centos.org/g /etc/yum.repos.d/CentOS-*.repo
      sed -i s/^#.*baseurl=http/baseurl=http/g /etc/yum.repos.d/CentOS-*.repo
      sed -i s/^mirrorlist=http/#mirrorlist=http/g /etc/yum.repos.d/CentOS-*.repo
    SHELL
  end

  config.vm.define "server_mongo_secondary" do |server_mongo_secondary|
    server_mongo_secondary.vm.box = "centos/8"
    server_mongo_secondary.vm.hostname = "server-mongo-secondary"
    server_mongo_secondary.vbguest.auto_update = false
    server_mongo_secondary.vm.network "private_network", ip: "192.168.52.3"
    server_mongo_secondary.vm.provision "shell", inline: <<-SHELL
      chmod 644 /home/vagrant/.ssh/vagrant_test.pub
      cat /home/vagrant/.ssh/vagrant_test.pub >> /home/vagrant/.ssh/authorized_keys
    SHELL
  end

  config.vm.define "server_mongo_arbiter" do |server_mongo_arbiter|
    server_mongo_arbiter.vm.box = "centos/8"
    server_mongo_arbiter.vm.hostname = "server-mongo-arbiter"
    server_mongo_arbiter.vbguest.auto_update = false
    server_mongo_arbiter.vm.network "private_network", ip: "192.168.52.4"
    server_mongo_arbiter.vm.provision "shell", inline: <<-SHELL
      chmod 644 /home/vagrant/.ssh/vagrant_test.pub
      cat /home/vagrant/.ssh/vagrant_test.pub >> /home/vagrant/.ssh/authorized_keys
      sed -i s/mirror.centos.org/vault.centos.org/g /etc/yum.repos.d/CentOS-*.repo
      sed -i s/^#.*baseurl=http/baseurl=http/g /etc/yum.repos.d/CentOS-*.repo
      sed -i s/^mirrorlist=http/#mirrorlist=http/g /etc/yum.repos.d/CentOS-*.repo
    SHELL
  end

    config.vm.define "server_docker_builder" do |server_docker_builder|
    server_docker_builder.vm.box = "centos/8"
    server_docker_builder.vm.hostname = "server-docker-builder"
    server_docker_builder.vbguest.auto_update = false
    server_docker_builder.vm.network "private_network", ip: "192.168.53.2"
    server_docker_builder.vm.provision "shell", inline: <<-SHELL
      chmod 644 /home/vagrant/.ssh/vagrant_test.pub
      cat /home/vagrant/.ssh/vagrant_test.pub >> /home/vagrant/.ssh/authorized_keys
    SHELL
  end

  config.vm.define "server_docker_runner" do |server_docker_runner|
    server_docker_runner.vm.box = "centos/8"
    server_docker_runner.vm.hostname = "server-docker-runner"
    server_docker_runner.vbguest.auto_update = false
    server_docker_runner.vm.network "private_network", ip: "192.168.53.3"
    server_docker_runner.vm.provision "shell", inline: <<-SHELL
      chmod 644 /home/vagrant/.ssh/vagrant_test.pub
      cat /home/vagrant/.ssh/vagrant_test.pub >> /home/vagrant/.ssh/authorized_keys
      sed -i s/mirror.centos.org/vault.centos.org/g /etc/yum.repos.d/CentOS-*.repo
      sed -i s/^#.*baseurl=http/baseurl=http/g /etc/yum.repos.d/CentOS-*.repo
      sed -i s/^mirrorlist=http/#mirrorlist=http/g /etc/yum.repos.d/CentOS-*.repo
    SHELL
  end

end
```
