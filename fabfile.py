from fabric.api import env, task

from deploy import *


# functions wrapped in a decorator "@task" loaded as task
@task
def live():
    # Hosts
    env.hosts = ['198.199.114.148']
    # Ubuntu user
    env.user = 'root'
    # Ubuntu password
    env.password = '733743fd450ed290'

    # Database settings
    env.mysql_root_user = 'root'
    env.mysql_root_password = 'rithmio1'

    env.mysql_db_name = 'wordpress'

    env.wordpress_user = 'wordpress'
    env.wordpress_password = 'wordpress1'
