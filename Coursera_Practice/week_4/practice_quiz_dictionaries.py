def email_list(domains):
    emails = []
    for domain,users in domains.items():
      for user in users:
        emails.append(user+'@'+domain)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
                  "yahoo.com": ["barbara.gordon", "jean.grey"],
                  "hotmail.com": ["bruce.wayne"]}))









def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group in group_dictionary.keys():
        # Now go through the users in the group
        for users in group_dictionary[group]:
            list = []
            for group in group_dictionary.keys():
                if users in group_dictionary[group] and users not in list:
                    list.append(group)
                user_groups[users] = list

            # Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"] }))





wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)












