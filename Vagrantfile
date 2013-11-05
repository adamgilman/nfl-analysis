Vagrant::Config.run do |config|
  config.vm.box = "lucid64"
  config.vm.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
  config.vm.forward_port 8888, 7777
end