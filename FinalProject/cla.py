
import hashlib
import timeit
import signal
import random
import string

from ctf import *
from voting import *

"""Represents the CLA"""
class CLA:
    #list of authorized voters
    authList = []
    
    """Authorization Number Stub
    Creates random authorization number for a voter
    and adds the voter to the list of authorized voters.
    Nothing is encrypted yet"""
    def authNumStub(self, voter):
        randAuthNum = random.randint(1000,2000)
        voter.setAuthNum(randAuthNum)
        self.authList.append(voter)
        CTF.notVotedList.append(voter)
        
def canVote(voter):
    #Check if voter is in CLA list and is authorized to vote
    for i in range(len(CLA.authList)):
        if CLA.authList[i].authNum == voter.authNum:
            print ("You are authorized to vote!")
            return True
        #Reject user because they are not authorized
        if i == len(CLA.authList)-1:
            print("You are not authorized to vote!")
            return False
    return False
            
def hasVoted(voter):
    for i in range(len(CTF.notVotedList)):
        #check if voter's authNum matches current authNum
        if CTF.notVotedList[i].authNum == voter.authNum:
            print("You have not voted yet!")
            return False
        #Reject user because they have already voted
        if i == len(CTF.notVotedList)-1:
            print("You have already voted!")
            return True
    return True
    
