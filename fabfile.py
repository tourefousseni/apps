#!/usr/bin/python

# -*- coding: utf-8 -*-
# os.environ["PYTHONIOENCODING"] = "utf-8"

from fabric.operations import sudo
from fabric.api import *
import time
from cryptography.hazmat.backends import default_backend
from fabric.api import local
# env.hosts = ['root@gisconsulting4.com']
import pyblog

# env.hosts = ['www.kalalso.com']
env.hosts = ['fulani@170.187.211.246']
env.password = 'fulani'
env.user = 'touretoure'
# env.port = '22'
# ssh key path
# env.ssh_keys_dir = os.path.join(abs_dir_path, 'ssh-keys')
venv = 'source /var/www/kalaliso/venv/bin/activate'


# GIT_REPO = "https://github.com/foussenitoure/cadastre.git:gisconsulting"

repo='https://github.com/foussenitoure/apps.git:main'
# repo='https://github.com/foussenitoure/cadastre:gisconsulting.git'
# repo='git@github.com:cadastre/gisconsulting.git'
timestamp="release_%s" % int(time.time() * 1000)
# https://github.com/foussenitoure/cadastre
# env.hosts = ['localhost']
# env.user = 'root'
# env.password = '<remote-server-password>'
# env.full_name_user = '<your-name>'
# env.user_group = 'deployers'
# env.user_name = 'deployer'

def deploy():
    source_folder = '/var/www/kalaliso'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip3 install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    # sudo('restart gunicorn-demo.charon.me')
    sudo('service nginx reload')

def _install_doc():
    sudo("%s && pip3 install -r requirements.txt" % venv)

def _get_code():
    cd("%s git fetch origin main")

# def _dumpdata():
    # sudo("%s && python3 manage.py dumpdata --format=json contacts > /var/tmp/$(date +"%Y%m%d_%H:%M:%S")_data.json;" % venv)

# def _loaddata():
    # sudo("%s && python3 manage.py loaddata  /var/tmp/$(current +"%Y%m%d_%H:%M:%S")_data.json;" % venv)
def _makemigrations():

    sudo("%s && python3 manage.py makemigrations" % venv)

def _migrate():
    sudo("%s && python3 manage.py migrate" % venv)

def _reload():
    cd("touch rebuild")
    sudo('service nginx reload')

@task(alias="d")
def basic_deploy():
     with cd('/var/www/kalaliso'):
        _install_doc()
        _get_code()
        _reload()

@task(alias="dwn")
def deploy():
     with cd('/var/www/kalaliso'):
        _install_doc()
        _get_code()
        # _dumpdata()
        # _loaddata()
        _makemigrations()
        _migrate()
        _reload()



