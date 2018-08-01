# Unstack users by 'weekday': byweekday
byweekday = users.unstack(['weekday'])

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
app = byweekday.stack(level='weekday')
print(app)

#------------------------------
# Unstack users by 'city': bycity
bycity = users.unstack(['city'])

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
app = bycity.stack(level='city')
print(app)

#---------------------------


# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level='city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0,1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))
#--------------OUTPUT-----------#

                visitors  signups
city   weekday                   
Austin Mon           326        3
Dallas Mon           456        5
Austin Sun           139        7
Dallas Sun           237       12
                visitors  signups
city   weekday                   
Austin Mon           326        3
       Sun           139        7
Dallas Mon           456        5
       Sun           237       12
True

<script.py> output:
                    visitors  signups
    city   weekday                   
    Austin Mon           326        3
    Dallas Mon           456        5
    Austin Sun           139        7
    Dallas Sun           237       12
                    visitors  signups
    city   weekday                   
    Austin Mon           326        3
           Sun           139        7
    Dallas Mon           456        5
           Sun           237       12
    True
	
#--------------------------