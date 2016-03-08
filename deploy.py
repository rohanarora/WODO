from fabric.api import cd, env, task
from fabric.contrib.files import upload_template
from fabric.operations import reboot, run, sudo


MYSQL_CREATE_DB = """
CREATE DATABASE %(db_name)s DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
"""


MYSQL_CREATE_USER = """
CREATE USER '%(wordpress_user)s'@'localhost' IDENTIFIED BY '%(wordpress_password)s';
"""


MYSQL_GRANT_PRIVILEGES = """
    GRANT ALL PRIVILEGES ON *.* TO '%(wordpress_user)s'@'localhost' IDENTIFIED BY '%(wordpress_password)s';
    FLUSH PRIVILEGES;
"""


@task
def update_upgrade():
    sudo('apt-get update')
    sudo('apt-get upgrade')


@task
def install_os_dependencies():
    packages = [
        'build-essential',
        'mysql-server',
        'libmysqlclient-dev',
        'apache2',
        'php5-mysql',
        'libapache2-mod-php5',
        'php5-mcrypt',
        'php5-gd',
        'php5-curl'
    ]
    sudo('apt-get update')
    sudo('apt-get -y upgrade')
    reboot(120)
    sudo('apt-get -y install %s' % ' '.join(packages))


@task
def setup_swapfile():
    sudo('fallocate -l 1G /swapfile')
    sudo('chmod 600 /swapfile')
    sudo('mkswap /swapfile')
    enable_swap()


@task
def enable_swap():
    sudo('swapon /swapfile')


@task
def setup_mysql():
    sudo('mysql_install_db')
    sudo('/usr/bin/mysql_secure_installation')
    mysql_restart()


@task
def mysql_restart():
    sudo('service mysql restart')


@task
def mysql_grant_privileges():
    sql = MYSQL_GRANT_PRIVILEGES % dict(wordpress_user=env.wordpress_user, wordpress_password=env.wordpress_password)
    mysql_execute(sql)
    mysql_restart()


@task
def create_mysql_user():
    sql = MYSQL_CREATE_USER % dict(wordpress_user=env.wordpress_user, wordpress_password=env.wordpress_password)
    mysql_execute(sql)
    mysql_restart()


@task
def create_mysql_database():
    run('mysqladmin -u %s -p%s create %s' % (env.mysql_root_user, env.mysql_root_password, env.mysql_db_name))


@task
def mysql_execute(sql):
    sql = sql.replace('"', r'\"')
    return run('echo "%s" | mysql --user="%s" --password="%s"' % (sql, env.mysql_root_user, env.mysql_root_password))


@task
def wordpress_setup():
    run('wget https://wordpress.org/latest.tar.gz')
    run('tar xvf latest.tar.gz')
    # Ideally edit the file remotely
    # with cd('wordpress'):
    #     run('cp wp-config-sample.php wp-config.php')
    #     run('nano wp_config.php')
    upload_template('wp-config.php', '~/wordpress/', backup=False, use_sudo=True)
    sudo('rsync -avP ~/wordpress/ /var/www/html')
    sudo('rm /var/www/html/index.html')
    sudo('mkdir /var/www/html/wp-content/uploads')
    sudo('chown -R www-data:www-data /var/www/html/')
    sudo('chmod -R 744 /var/www/html')

@task
def first_time_setup():
    update_upgrade()
    install_os_dependencies()
    setup_swapfile()
    setup_mysql()
    create_mysql_user()
    create_mysql_database()
    mysql_grant_privileges()
    wordpress_setup()
