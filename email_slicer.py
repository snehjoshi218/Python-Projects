#get users email

email = input ('What is your email?: ').strip()
print(email)

#slice out user name

user = email[:email.index('@')]


#slice domain name

domain = email[email.index('@') + 1:]


#format message

output = "Your username is {} and your domain name is {}"
output = output.format (user, domain) 

#display output message

print(output)
 
