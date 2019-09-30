import phonetics as ph

file = open('C:/Users/Kshitij Sinha/Desktop/hacktober/Phonetica/sinarest.txt', 'r')

cl = []
for f in file:
    cl.append(f.replace('\n', ''))
file.close()

for c in cl:
    print(ph.ipa_fd(c))
