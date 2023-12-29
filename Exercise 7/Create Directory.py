###########
Create Directory

####################

def create_directory(new_directory_name: str) ->bool:
    # Use try/except to catch errors
    try:
        # Create the diretory
        os.mkdir(new_directory_name)
        # If this worked, return True
        return True
    except:
        # Give an explicit error message
        print(f"Error creating directory {new_directory_name}")
        # If this did not work, return False
        return False    