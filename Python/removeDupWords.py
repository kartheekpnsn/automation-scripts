#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Remove duplicate words in a string
def removeDups(s):
	s = s.replace('\n', ' <@> ') # In order not to remove the new line characters
	ulist = []
	[ulist.append(x) for x in s.split(' ') if x == '<@>' or x not in ulist]
	s = ' '.join(ulist)
	s = s.replace(' <@> ', '\n')
	return(s)
	
print removeDups("I am a good boy\nI a good kartheek\nis the best bud")

# # # Start of Output:
# # I am a good boy
# # kartheek
# # is the best bud
# # # End of Output;
