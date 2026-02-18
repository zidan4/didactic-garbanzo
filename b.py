#if it's ICMP, we want it
if ip_header.protocol == "ICMP":
  # calculate where our ICMP packet starts
  offset = ip_header.ihl * 4
  buf = raw_buffer[offset:offset + sizeof(ICMP)]
  
  # create our ICMP structure
  icmp_header = ICMP(buf)
  print "ICMP -> Type: %d Code: %d" % (icmp_header.type, icmp_header.¬
  code
