#I labeled all the variables asking for various inputs.
campaign_name = input("Enter campaign name: ")
email_list = input("Enter email addresses: ")
engagement= input('Enter engagement status: ')
company_type = input("What company type is it: ")
#This turns the emails into a list and the engagements into a list. 
email_L = email_list.split(",")
engagement_L = engagement.split(",")
#This sets up how the different engagements would be organized and counted.
domains = {}
engagement_summary = {"opened": 0, "clicked": 0, "bounced": 0, "unsubscribed": 0}
#This basically creates a loop to look through the list and looks for the different domains.
for x in range(len(email_L)):
    email = email_L[x]
    domain = email.split("@")[-1]
#This basically counts how mamy of each domains there are.
    if domain in domains:
       domains[domain] += 1
    else: 
        domains[domain] = 1
    #This records the engagement/status and show how many times it was clicked, opened, or other and adds one.
    status = engagement_L[x]
    if status in engagement_summary:
        engagement_summary[status] += 1
#This code basically calculated the success rate of the differnet comapanies.
click_rate = engagement_summary['clicked']/len(email_L) * 100
#This does the mathto determine the success.
if click_rate >= 50: percent="Excellenet"
elif click_rate >= 30: percent= "Good"
elif click_rate > 0: percent= "Needs Improvement"
elif click_rate == 0: percent="Poor"

#This prints the information!
print()
print()
print(campaign_name)
print(company_type)
print(domains)
print(engagement_summary)
print(percent)