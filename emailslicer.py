def email_slice():
    # Define the email
    email = input("enter your email id:")
    # Split the email into username and domain
    username,domain= email.split("@")
    # Split the domain into domain name and domain extension
    domain_name,domain_extension = domain.split(".")
    # Print the sliced email
    
    print("\n email slicing result:")
    print(f"username:{username}")
    print(f"domain name:{domain_name}")
    print(f"domain extension:{domain_extension}")

email_slice()
