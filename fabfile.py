#!/usr/bin/python

# -*- coding: utf-8 -*-
# os.environ["PYTHONIOENCODING"] = "utf-8"

from fabric.api import *
import time
from cryptography.hazmat.backends import default_backend

from fabric.api import local

# env.hosts = ['root@gisconsulting4.com']
import pyblog


# env.hosts = ['www.kalalso.com']
env.hosts = ['root@143.198.60.181']
env.password = 'fulani'
env.user = 'fulani'
venv = 'source /home/fulani/kala/venv/bin/activate'

# GIT_REPO = "https://github.com/foussenitoure/cadastre.git:gisconsulting"

repo='https://github.com/foussenitoure/cadastre.git:main_kalaliso'
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
# ssh key path
# env.ssh_keys_dir = os.path.join(abs_dir_path, 'ssh-keys')

from fabric.api import env
from fabric.api import run
from fabric.operations import sudo

GIT_REPO = "https://github.com/........"

env.user = 'root'
env.password = '...'

env.hosts = ['demo....com']
env.port = '22'


def deploy():
    source_folder = '/home/.../sites/..../...'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-demo.charon.me')
    sudo('service nginx reload')



# def _install_doc():
#     sudo("%s && pip install -r requirements.txt" % venv)
#
#
# def _get_code():
#     cd("%s git fetch origin main_kalaliso")
#
#
# def _makemigrations():
#
#     sudo("%s && python manage.py makemigrations" % venv)
#
# def _migrate():
#     sudo("%s && python manage.py migrate" % venv)
#
# def _reload():
#     cd("touch rebuild")
#     sudo('service nginx reload')
#
# @task(alias="d")
# def basic_deploy():
#      with cd('/home/fulani/kala'):
#         _install_doc()
#         _get_code()
#         _reload()
#
# @task(alias="dwn")
# def deploy():
#      with cd('/home/fulani/kala'):
#         _install_doc()
#         _get_code()
#         _makemigrations()
#         _migrate()
#         _reload()



