ospf_route = ['10.0.24.0/24', '110/41', '10.0.13.3', '3d18h', 'FastEthernet0/0']

print("Prefix                " + ospf_route[0])
print("AD/Metric             " + ospf_route[1])
print("Next-Hop              " + ospf_route[2])
print("Last update           " + ospf_route[3])
print("Outbound Interface    " + ospf_route[4])