
## The Vagrantfile:

```
Vagrant.configure("2") do |config|
# Define VMs with static private IP addresses, vcpu, memory and vagrant-box.
  boxes = [
    {
      :name => "client2",
      :box => "centos/8",
      :ram => 4096,
      :vcpu => 2,
      :ip => "192.168.29.2"
    },
    {
      :name => "ansible-host",
      :box => "x.x.x.xxx",
      :ram => 8048,
      :vcpu => 4,
      :ip => "192.168.29.4"
    }
  ]


  # Provision each of the VMs.
  boxes.each do |opts|
    config.vm.define opts[:name] do |config| disabled: true
      config.ssh.insert_key = false
      config.vm.box = opts[:box]
      config.vm.hostname = opts[:name]
      config.vm.provider :virtualbox do |v|
        v.memory = opts[:ram]
        v.cpus = opts[:vcpu]
      end

```


