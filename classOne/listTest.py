invitationList = ["aimingChen", "Json", "Master", "Justin"]
print(invitationList)

canNotComeMan = "Master"
print(canNotComeMan + " can not come to the party!")

invitationList[2] = "Pink"
print(invitationList)

print("I find a bigger room to the party.")

invitationList.insert(0, "Jack")
invitationList.insert(2, "Jim")
invitationList.append("Orange")
print(invitationList)

print("Food is't enough, Only for two people!")

while len(invitationList) > 2:
    notInvitationPeople = invitationList.pop()
    print("I'm sorry " + notInvitationPeople + ",the party is cancel.")

print(invitationList)

del invitationList[0:2]
print(invitationList)
