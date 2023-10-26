from cpanel_api import CPanelApi

hostname = '213.165.242.4'
username = 'ne424b5'

client = CPanelApi(hostname, username, '8NVAUWDSXHA0QPG0FYYDDMPGH3ABOQL0', auth_type = 'utoken')

# create subdomain
# create_subdomain = client.uapi.SubDomain.addsubdomain(domain="test" , rootdomain="0e424bde1c10755380.temporary.link" , dir="/")

# create database
# create_db = client.uapi.Mysql.create_database(name=f"{username}_testuser")

# create database user
# create_db_user = client.uapi.Mysql.create_user(name=f"{username}_testuser" , password="8NVAUWDSXHA0QPG0FYYDDMPGH3ABOQL0")

# add user to database
# add_user_to_db = client.uapi.Mysql.set_privileges_on_database(user=f"{username}_testuser" , database=f"{username}_testuser" , privileges="ALL PRIVILEGES")

print(add_user_to_db)