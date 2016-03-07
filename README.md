## Setting up Digital Ocean
1. Register at https://www.digitalocean.com/  
2. Confirm E-mail address
3. Setup Credit / Debit Card and Paypal

## Creating an SSH-Key [For Mac and Linux]


## Setting up a Droplet  [Simply put a computer at a remote location]
1. Create droplets
2. Select a Ubuntu distribution: 14.04.4 x64  
3. Choose a size: 512 MB RAM / 1 CPU / 20GB SSD / 1TB Transfer [We'll try making up for the low RAM with a swap partition]  
4. Choose a datacenter region - San Francisco  
5. Select Additional Options: Don't select anything  
6. Add the public SSH key (add in a comment for future reference)  
7. How many Droplets: 1 Droplet  
8. Create the droplet


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
1. Setup Python  
2. Install Fabric via pip [pip install fabric / If you are using Anaconda conda install fabric]  


## Time to run the Fabric files  
1. Clone / Download the repository from   
2. Open the file fabfile.py and set the value of env.hosts to the IP address of the instance / droplet as seen at https://cloud.digitalocean.com/droplets [Sign-in if required]. Replace the IP address keyed-in-already with the one you see at the link    
3. Set the value of env.mysql_root_password  
4. Set the value of env.wordpress_password Also head over to wp-config.php in the downloaded directory change 'wordpress1' to thevalue set  
5. 'cd' / head over to the unzipped folder and run the following:  
fabric live first_time_setup  
6. If asked: Yes to upgrade [You'll see something along the lines of: Do you wish to upgrade...additional disk space..]  
7. Enter the value you keyed in Step(3) (skip the single quotes at the beginning and end)   
8. Tab followed by space; enter the password again; tab followed by space  
9. Then you'll be asked enter the password for root. Enter the value you keyed in Step 7  
10. You'll be asked do you want to change the root password. We don't want to. Just type n  
11. Y(es) to remove anonymous users  
12. Y(es) to disallow root login remotely  
13. Y(es) to remove test database and access to it  
14. Y(es) to reload privileges table now  


