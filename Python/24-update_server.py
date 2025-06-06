#update the server config file

def update_server_config(file_path, key, value):

    with open(file_path, "r") as file: # Read the existing content of the server configuration file
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(f"{key}={value}\n")

            else:
                file.write(line) # Keep the existing line as it is

update_server_config("server.conf", "MAX_CONNECTIONS", "2000")

'''
# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '600'  # New maximum connections allowed

# Update the server configuration file
update_server_config(server_config_file, key_to_update, new_value)'
'''