
import os
import pprint

# Get the list of user's
env_var = os.environ

# Print the list of user's
print("User's Environment variable:")
pprint.pprint(dict(env_var), width = 1)



if "s3password" in os.environ:
    password = os.environ["s3password"]
    print(f"Password: {password}")
