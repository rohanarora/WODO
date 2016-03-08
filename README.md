## Setting up Digital Ocean
1. Register at https://www.digitalocean.com/  
2. Confirm E-mail address  
3. Setup Credit / Debit Card and Paypal  


## Creating an SSH-Key [Optional]
1. https://help.github.com/categories/ssh/  


## Setting up a Droplet  [Simply put a computer at a remote location]
1. Create droplets
2. Select a Ubuntu distribution: 14.04.4 x64  
3. Choose a size: 512 MB RAM / 1 CPU / 20GB SSD / 1TB Transfer [We'll try making up for the low RAM with a swap partition]  
4. Choose a data-center region - San Francisco (or any)  
5. Select Additional Options: Don't select anything  
6. **Option 1**: Add the public SSH key (add in a comment for future reference)   
7. **Option 2**: Don't add an SSH key and check email for credentials from DigitalOcean   
8. How many Droplets: 1 Droplet  
9. Create the droplet  


## Testing access the Droplet [Optional]
1. Head over to https://cloud.digitalocean.com/droplets [Sign-in if required]  
2. Make note of the IP address of the instance / droplet  
3. Open up a terminal on your computer and key in the following:  
ssh -v root@IP-Address-Of-The-Instance  
An example would be: ssh -v root@107.170.223.166  
5. Are you sure you want to continue connecting: Yes  
6. At the end you should see something along the lines of:  
root@ubuntu-512mb-
Hurray! You have successfully logged into the remote instance. In the terminal type:  
exit


## Setup Python and Fabric 
1. Setup Python [https://developers.google.com/edu/python/set-up#python-on-linux-mac-os-x-etc]  
2. Install [pip][https://pip.pypa.io/en/stable/installing/]   
3. Install Fabric via pip  
[In the Terminal execute:  
 pip install fabric (if you get a permission denied error execute: sudo pip install fabric)
If you are using Anaconda execute:  
conda install fabric]  


## Time to execute the scripts  
1. Clone / Download the repository from https://github.com/rohanarora/WoDO/archive/master.zip. Unzip it. You should see a directory WoDo-master. Navigate into the directory.  
2. Open the file fabfile.py and set the value of env.hosts to the IP address of the instance / droplet as seen at https://cloud.digitalocean.com/droplets. Replace the IP address keyed-in-already with the one you see at the link(retain the single quotes)    
3. In fabfile.py set the value of env.mysql_root_password(retain the single quotes); just like any password
4. In fabfile.py set the value of env.wordpress_password just like any password(retain the single quotes). Head over to wp-config.php in the downloaded directory and change 'wordpress1' to the value set for env.wordpress_password(again retain the single quotes)  
5. If you have resorted to *Option 2* in **Setting up a Droplet** set the value of env.password (retain the single quotes) in fabfile.py with the password you received in an email from Digital Ocean post creation of droplet / instance  
6. In the unzipped directory execute the following:  
fabric live first_time_setup  
If you have resorted to *Option 2* in **Setting up a Droplet** you'll be asked to set a new Unix Password. Enter the password you received in an email from Digital Ocean post creation of droplet / instance and hit Enter. Post which you'll be asked to enter a password of your choice. Update the new password you just entered in fabfile.py's env.password (retain the single quotes)  
6. If you are caught in a loop where-in its asking you to re-enter the password again and again hit Ctrl+C and then re-run fabric live first_time_setup  
7. If asked: Yes to upgrade (You'll see something along the lines of: Do you wish to upgrade...additional disk space..)  
8. After installing LAMP components it'll ask you to set the root password for MySQL. Enter the value you keyed in Step(3) (skip the single quotes at the beginning and end)   
9. To continue press the Tab key followed by space; enter the password again; tab followed by space  
10. Then you'll be asked enter the MySQL's root password. Enter the value / password you keyed in Step 8  
11. You'll be asked do you want to change the root password. We don't want to. Just type n  
12. Y(es) to remove anonymous users  
13. Y(es) to disallow root login remotely  
14. Y(es) to remove test database and access to it  
15. Y(es) to reload privileges table now  
16. Wait until the execution is complete (you'll see 'Done...')
