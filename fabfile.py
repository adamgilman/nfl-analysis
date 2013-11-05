from fabric.api import env, local, run, cd, sudo, prefix
from fab_essentials import aptget, gem, pip, upgrade_pip, ipython_install

def vagrant():
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:2222']
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]
    env.install_dir = "/vagrant/"
    env.activate = "source bin/activate"

def build():
	sudo("apt-get update")
	upgrade_pip()
	aptget( ['build-essential', 'byobu', 'python-dev'] )
	ipython_install()
	pip(["virtualenv", "virtualenvwrapper"])

def nflgame():
	#setup virtualenv
	with cd("/vagrant"), prefix("source /usr/local/bin/virtualenvwrapper.sh"):
		run("mkvirtualenv nflanalysis")

	with cd('/vagrant'), prefix('workon myvenv'):	
		pip(['nflgame'])

	'''
	with cd('/path/to/app'), prefix('workon myvenv'):
	with prefix('workon myvenv'):
        run('git pull')
        run('do other stuff, etc')'''
	#run("ipython notebook --pylab --ip='*'&")