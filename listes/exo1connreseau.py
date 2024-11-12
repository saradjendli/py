packets={500:'TCP', 1000: 'UDP',2000:'TCP',50:'ICMP',1600: 'TCP',800: 'UDP'}

for element in packets:
    if element>1500:
        print(element.items())