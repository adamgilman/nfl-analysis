from fabric.api import env, local, run, cd, sudo

def aptget(package):
	if type(package) is list:
		for p in package:
			aptget(p)
	else:
		sudo("apt-get -y install %s" % package)

def gem(package):
	if type(package) is list:
		for p in package:
			gem(p)
	else:
		sudo("gem -y install %s" % package)

def upgrade_pip():
	#aptget('python-pip')
	pip("pip", upgrade=True)


def pip(package, upgrade=False):
	aptget("python-setuptools")
	sudo("easy_install pip")
	if type(package) is list:
		for p in package:
			pip(p)
	else:
		if upgrade:
			sudo("pip install %s --upgrade" % package)
		else:
			sudo("pip install %s" % package)

def ipython_install():
	pip(['ipython[all]'])
	aptget('python-matplotlib')
