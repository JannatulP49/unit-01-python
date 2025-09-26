campaign_name = input("Enter campaign name: ")
email_list = input("Enter email addresses: ")
engagement= input('Enter engagement status: ')
company_type = input("What company type is it: ")


domains = {}
engagement_summary = {"opened": 0, "clicked": 0, "bounced": 0, "unsubscribed": 0}

for x in range(len(email_list)):
    domain = email_list(x).split (",") 


