import os

def setup_user_directory():
    # Check the current working directory
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")

    # Ask for the user's name
    username = input("Please enter your username: ").strip()

   
    user_dir = os.path.join(current_dir, username)

    # Check if the user has a directory named after them
    if not os.path.exists(user_dir):
        print(f"Directory for {username} does not exist. Creating it now...")
        os.makedirs(user_dir)
    else:
        print(f"Directory for {username} exists. Moving into that directory...")

    # Move into the user directory
    os.chdir(user_dir)
    
    # Check if the profile.txt file exists in the user's directory
    profile_path = os.path.join(user_dir, "profile.txt")

    if os.path.exists(profile_path):
        # Read the contents of the profile.txt file
        with open(profile_path, "r") as file:
            profile_data = file.readlines()
        
        # Display the profile info to the user
        print("\nCurrent profile information:")
        profile_info = {}
        for line in profile_data:
            key, value = line.strip().split(": ")
            profile_info[key] = value
            print(f"{key}: {value}")

        # Ask if the info is up to date
        is_up_to_date = input("\nIs this information up to date? (yes/no): ").strip().lower()
        
        if is_up_to_date != "yes":
            # Collecting user info
            profile_info = {
                "Name": input("Enter your name: ").strip(),
                "Email": input("Enter your email: ").strip(),
                "Phone": input("Enter your phone number: ").strip()
            }
            # Write the updated profile info to the profile.txt file
            with open(profile_path, "w") as file:
                for key, value in profile_info.items():
                    file.write(f"{key}: {value}\n")
            print("Profile information updated successfully.")
    else:
        # If profile.txt does not exist, collect info and create it
        print("No profile found. Creating a new profile...")

        profile_info = {
            "Name": input("Enter your name: ").strip(),
            "Email": input("Enter your email: ").strip(),
            "Phone": input("Enter your phone number: ").strip()
        }

        # Write the profile info to the profile.txt file
        with open(profile_path, "w") as file:
            for key, value in profile_info.items():
                file.write(f"{key}: {value}\n")
        print("Profile created successfully.")

    # Give user access to terminal
    print("\nYou now have access to the terminal. You are in your own directory.")

# calling the function
setup_user_directory()
