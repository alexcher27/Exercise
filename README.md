## Ex1: 

Bash Ex:
This Script will need 3 parameters, 2 string and 1 Directory.
Sustitues the 1 string with the 2 string in all files (where present) of the Directory you give. 

## Ex3:

Crontab Ex: 
This Crontab String will make a backup of /home/user to a remote server every Sunday at Midnight wich is reachable by ssh.


## Ex4:

Ansible Ex: 
Multi-Machine Vagrant Environments:
This Vagrantfile will create 2 Centos VM's to simulate Ansible control machine and 1 target host with Wordpress installed.
* Host2 - Centos2
* ansible-host - No GUI, ansible core installed and Ansible-tower

## Requirements:

* Internet connection is a must!
* Make sure the VT support is enabled on your BIOS
* Vagrant - 1.9.x or higher
* Vagrant plugins - vagrant-proxyconf - needed if you are running behind proxy
* Ansible: latest
* Virtualbox: latest


# Note: if the build fail because of the hypervisor errors. You need to follow this steps.

First find out the name of the hypervisor:
```
$ lsmod | grep kvm
kvm_intel             204800  6
kvm                   593920  1 kvm_intel
irqbypass              16384  1 kvm
```
The one we're interested in is kvm_intel. You might have another.

Blacklist the hypervisor (run the following as root):
```
$ echo 'blacklist kvm-intel' >> /etc/modprobe.d/blacklist.conf
```
Restart your machine and try running vagrant again.



## Connecting the dots:
Before you run vagrant up, make sure that you updated the Vagrantfile to your desired configuration. 

## How tu use:
- _vagrant up_
  Wait for about 6 minutes to finish the build. Once done. You can try to ssh to your ansible-host vm. You can verify this by using "_vagrant status_"

- _vagrant ssh ansible-host_ 
  once you are login to your ansible-host vm, you can now verify if the other vm are reachable. The command to use is: "_ansible-playbook -i inventory playbook/ping.yml_"



