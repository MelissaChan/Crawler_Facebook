# __author__ = MelissaChan
# -*- coding: utf-8 -*-
# 16-4-11 下午11:03

# -*- coding: utf-8 -*-

import sys
import json
import facebook
import urllib2
from Stange_Login import login

try:
    ACCESS_TOKEN = 'CAACEdEose0cBAA5FCCSLfGZClI0hiw86JMzZBNDq0rLCt6jU05ELgXOLToNHmJQLslYvZCVa2KdqNFQwIjerXkaVvh51i513uZBW2k7b9uz8ZBwcLdcdV0u4QsiiMyfvqpDNUUZB5pFqznKZArOwUvM2azHCH7tD4TJsLbUS0RTJ2X5TLJMl63JOpY3JHM0ecGOZAZBl3s5zDj2QfdeV2QORR'
except IOError, e:
    try:

        # If you pass in the access token from the Facebook app as a command line
        # parameter, be sure to wrap it in single quotes so that the shell
        # doesn't interpret any characters in it

        ACCESS_TOKEN = 'CAACEdEose0cBAA5FCCSLfGZClI0hiw86JMzZBNDq0rLCt6jU05ELgXOLToNHmJQLslYvZCVa2KdqNFQwIjerXkaVvh51i513uZBW2k7b9uz8ZBwcLdcdV0u4QsiiMyfvqpDNUUZB5pFqznKZArOwUvM2azHCH7tD4TJsLbUS0RTJ2X5TLJMl63JOpY3JHM0ecGOZAZBl3s5zDj2QfdeV2QORR'
        Q = sys.argv[2]
    except:
        print >> sys.stderr, \
            "Could not either find access token in 'facebook.access_token' or parse args."
        ACCESS_TOKEN = 'CAACEdEose0cBAA5FCCSLfGZClI0hiw86JMzZBNDq0rLCt6jU05ELgXOLToNHmJQLslYvZCVa2KdqNFQwIjerXkaVvh51i513uZBW2k7b9uz8ZBwcLdcdV0u4QsiiMyfvqpDNUUZB5pFqznKZArOwUvM2azHCH7tD4TJsLbUS0RTJ2X5TLJMl63JOpY3JHM0ecGOZAZBl3s5zDj2QfdeV2QORR'
        Q = sys.argv[1]

LIMIT = 100

gapi = facebook.GraphAPI(ACCESS_TOKEN)

# Find groups with the query term in their name

group_ids = []
i = 0
while True:
    results = gapi.request('search', {
        'q': Q,
        'type': 'group',
        'limit': LIMIT,
        'offset': LIMIT * i,
    })
    if not results['data']:
        break

    ids = [group['id'] for group in results['data'] if group['name'
    ].lower().find('programming') > -1]

    # once groups stop containing the term we are looking for in their name, bail out

    if len(ids) == 0:
        break
    group_ids += ids

    i += 1

if not group_ids:
    print 'No results'
    sys.exit()

# Get details for the groups

groups = gapi.get_objects(group_ids, metadata=1)

# Count the number of members in each group. The FQL API documentation at
# http://developers.facebook.com/docs/reference/fql/group_member hints that for
# groups with more than 500 members, we'll only get back a random subset of up
# to 500 members.

for g in groups:
    group = groups[g]
    conn = urllib2.urlopen(group['metadata']['connections']['members'])
    try:
        members = json.loads(conn.read())['data']
    finally:
        conn.close()
    print group['name'], len(members)