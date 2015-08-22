#!/usr/bin/python

val = None
with open('cntr.txt', 'rw+') as f:
  val = int(f.read() or 0)
  f.truncate()
  val += 1
  f.write(str(val))


print "Content-type: text/html"

print "<title>Update Counter</title>"
print "<p>The new value is: %d</p>" % val
