#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Not useful for others - but just a note to myself

import facebook # sudo pip install facebook

# # Steps to connect to a facebook page - create an app (then you get app_id and app_secret)
# app_id = "901095986651940"
# app_secret = "3449b2e9b7d287258cec9ec341f9d7d5"
# # The below token is a sample temporary token given by facebook
# short_token = "CAAMzisIxYyQBANOl9pqbJdb5FTkX3tVU34KFZCsE1prOc7AILAs44xIcgwUoln2SnHg8RAQZANlgiBRb2VvPg7ZBV3nAyZCFsRR7ozrLnCO9FZArcOs9t7eqsgingEGqPY3ZBvLgeIF4sK53VtEly2StKnXV8bdlHaFIG8bPRDtxuvxz2b1w4OEFYjUHP7Ot5rKx4GGBZAGNTI0Ua1Seyt6"
# url = "https://graph.facebook.com/oauth/access_token?client_id="+app_id+"&client_secret="+app_secret+"&grant_type=fb_exchange_token&fb_exchange_token="+short_token
# r = requests.get(url)
# # Generate a life long token (only for pages) using the line below
# long_token = r.text.split('=')[1].split('&')[0]

def get_api(cfg):
  # graph = facebook.GraphAPI(cfg['access_token'])
  # # Get page token to post as the page. You can skip 
  # # the following if you want to post as yourself. 
  # resp = graph.get_object('me/accounts')
  page_access_token = "CAAMzisIxYyQBANynJplY2eDjqXknBlX9A85oZCcKIZBde5GvP1LBCjs9O2ZBZBA5SQ8nQLbPw2xhoyzHemj2n5TTg1gCZAq7kVt3AqcnzlKeU0HpegPyZBZBZAZAtQAvKAZCVyTkQkz3kodbevuBCIX3ZAZCDgSQFdRqRcYhKpmSwhCrFKS2GRnXbyMKGjBOYu4EhcoZD"
  
  # page_access_token = None;
  # for page in resp['data']:
  #   if page['id'] == cfg['page_id']:
  #     page_access_token = page['access_token']
  #     print "PAGE TOKEN "+page_access_token
      
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3
# # # TOKEN - CAAMzisIxYyQBANd5wyyMabIWqPBgS20d7veY4LkG0vhUBIxAha3DUANSnqI9kIGnICihpwTZBxIyBhQZCNG8CAlfeKLTw7NNABi1nz40ZBktYyryskxC0EMl7TxXtWUg9VJVVF3IUe8i4qb0vVUrtmjjtLl1z8AW0Hq2ViBElex2uDsD9vVQyOojyTp6d4ZD

def main(words, meanings):
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"         : "857558994358171",  # Step 1
    # "access_token"  : long_token          # Step 3
    }

  api = get_api(cfg)
  msg = "Your Message Here"
  status = api.put_wall_post(msg)
