from cla import *
from voting import *
"""Represents CTF"""
class CTF:
    #list of authorized voters who have not voted yet
    notVotedList = []
    options = []
    
    """Count Vote Stub
    Checks to see if the user is in the list of authorized
    users who haven't yet voted, then either rejects user or
    allows user to vote
    voter - a voter object
    randomVote - if a random vote needs to be calculated or the user will enter a vote"""
    def countVoteStub(self,voter, randomVote):        
        #Check if voter is in CLA list and is authorized to vote
        if canVote(voter):
            #check if voter is in CTF list and has voted
            if (hasVoted(voter) == False):
                #calculate random vote
                if(randomVote):
                    #random vote
                    self.randomVote(voter)
                    #remove voter from list of people who haven't voted
                    self.notVotedList.remove(voter)
                else:
                    #allow user to enter a vote manually
                    voter.setVote(input("Please enter your vote: "))
                    #remove voter from list of people who haven't voted
                    self.notVotedList.remove(voter)
                    
                #get the vote
                theVote = voter.vote
                
                #first candidate in list
                if len(self.options) == 0:
                    #create new candidate
                    newCandidate = Candidate()
                    #add to their vote count
                    newCandidate.setNumber(theVote)
                    #add to candidates list
                    self.options.append(newCandidate)
                
                #if vote has been counted yet
                counted = False
                #count the vote
                for j in range(len(self.options)):
                    #if candidate that is being voted for is in candidates list
                    if self.options[j].candidateNum == theVote:
                        #increase vote count
                        self.options[j].addVote()
                        counted = True
