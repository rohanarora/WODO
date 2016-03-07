from os import getenv
from fabric.api import env, task

from deploy import *


# functions wrapped in a decorator "@task" loaded as task
@task
def live():
    # Hosts
    env.hosts = ['107.170.223.166']
    # Ubuntu_user
    env.user = 'root'
    # Ubuntu_user_group
    env.group = env.user

    # Database settings
    env.mysql_root_user = 'root'
    env.mysql_root_password = 'rithmio1'

    env.mysql_db_name = 'wordpress'

    env.wordpress_user = 'wordpress'
    env.wordpress_password = 'wordpress1'
