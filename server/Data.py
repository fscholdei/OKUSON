# -*- coding: ISO-8859-1 -*-
#  OKUSON Package
#  Frank L�beck and Max Neunh�ffer

'''This is the place where all data about participants of the course are
administrated. This includes data about their results and submissions.'''

CVS = '$Id: Data.py,v 1.6 2003/10/06 22:44:18 neunhoef Exp $'

import sys,os,string,threading

import Config

from fmTools import Utils, AsciiData

# The following decides, whether the server is in Administrator mode
# or not.
AdminMode = 0

# Here we begin the definition of the user database:

# We agree on the following locking policy:
# Once threaded service has begun, we allow every thread unlocked read
# access to the data base (which is made up of a tree of memory objects
# stored under the root "people"). However, any write access to any data
# in this tree must be protected by acquiring the following lock:
Lock = threading.Lock()

# This means: Whenever a routine writes anything into the database,
# one has to acquire the Lock even before certain read accesses, on
# which the following write operation might depend! So if one for 
# example checks whether there is already some data for a person
# just before creating it (as for example during registration), one
# has to acquire the Lock before the check, to avoid any write accesses
# from other sources between the lookup and the addition of the data!
# Please keep locks short! And ALWAYS, ALWAYS, ALWAYS make sure to 
# release the lock eventually, under all circumstances!

class Person(Utils.WithNiceRepr):
    '''Objects of in this class store a person.'''
    id = "100000"     # an id which determines the person uniquely
    lname = "?"       # last name
    fname = "?"       # first name
    sem = 1           # semester number
    stud = "?"        # "Studiengang"
    passwd = "x"      # password, encrypted via "crypt"
    email = ""        # email address, optional
    wishes = ""       # a string with wishes for small groups
    persondata1 = ""  # there are up to 9 additional entries to store
                      # personal data, these are not used in the default
                      # setup provided by OKUSON
    persondata2 = ""
    persondata3 = ""
    persondata4 = ""
    persondata5 = ""
    persondata6 = ""
    persondata7 = ""
    persondata8 = ""
    persondata9 = ""

    mcresults = {}    # for each sheet name an object of type "MCResult"
                      # note that keys in this dictionary are strings!
    homework = {}     # for each sheet number an object of type "Homework"
    exams = []        # for each exam (zero based numbers) either unbound
                      # or None or an object of type "Exam"
    group = 0         # number of small group the person is in
    messages = []     # here we collect private messages for participants
                      # these are just strings which are put into a web
                      # page one after another.

    def __init__(self):
        self.mcresults = {}
        self.homework = {}
        self.exams = []
        self.messages = []


people = {}     # all people are stored in here under their id

peopledesc = AsciiData.FileDescription(Config.conf['RegistrationFile'],people,
  ( "ENTER", 0, "KEY",    Person,
    "STORE", 0, "id",     "STRING",
    "STORE", 1, "lname",  "STRING",
    "STORE", 2, "fname",  "STRING",
    "STORE", 3, "sem",    "INT",
    "STORE", 4, "stud",   "STRING",
    "STORE", 5, "passwd", "STRING",
    "STORE", 6, "email",  "STRING",
    "STORE", 7, "wishes", "STRING",
    "STORE", 8, "persondata1", "STRING",
    "STORE", 9, "persondata2", "STRING",
    "STORE", 10, "persondata3", "STRING",
    "STORE", 11, "persondata4", "STRING",
    "STORE", 12, "persondata5", "STRING",
    "STORE", 13, "persondata6", "STRING",
    "STORE", 14, "persondata7", "STRING",
    "STORE", 15, "persondata8", "STRING",
    "STORE", 16, "persondata9", "STRING"  ) )


class MCResult(Utils.WithNiceRepr):
    '''Objects in this class store multiple choice submissions and results.'''
    marks = ""      # string of "+", "-", and "0"s each letter for one question
    score = 0       # sum of points
    submission = "" # the submission as one string for later reference
    date = 0        # submission date in seconds since the epoche
                                       
mcresultsdesc = AsciiData.FileDescription(Config.conf['SubmissionFile'],people,
  ( "ENTER", 0, "KEY",        Person,
    "STORE", 0, "id",         "STRING",
    "ENTER", 0, "mcresults",  "DICT",
    "ENTER", 1, "KEY",        MCResult,
    "STORE", 2, "marks",      "STRING",
    "STORE", 3, "score",      "INT",
    "STORE", 4, "submission", "STRING",
    "STORE", 5, "date",       "INT" ) )


class Homework(Utils.WithNiceRepr):
    '''Objects in this class store homework results.'''
    totalscore = 0  # score for all written exercises
    maxscore = 0    # maximal possible score
    scores = ""     # scores of the separate written exercises

    def __init__(self):
        self.scores = ""

homeworkdesc = AsciiData.FileDescription(Config.conf['HomeworkFile'],people,
  ( "ENTER", 0, "KEY",        Person,
    "STORE", 0, "id",         "STRING",
    "ENTER", 0, "homework",   "DICT",
    "ENTER", 1, "KEY",        Homework,
    "STORE", 2, "totalscore", "INT",
    "STORE", 3, "maxscore",   "INT",
    "FILL",  4, "scores",     "STRING" ) )


class Exam(Utils.WithNiceRepr):
    '''Objects in this class store exam information.'''
    registration = 1          # if true, person has registered for exam
    totalscore = 0            # totalscore
    maxscore = 0              # maximal score
    scores = ""               # scores for separate parts of exam


examregdesc = AsciiData.FileDescription(Config.conf['ExamRegistrationFile'],
                                        people,
  ( "ENTER", 0, "KEY",          Person,
    "STORE", 0, "id",           "STRING",
    "ENTER", 0, "exams",        "VECT",
    "ENTER", 1, "KEY",          Exam,
    "STORE", 2, "registration", "INT" ) )

examdesc = AsciiData.FileDescription(Config.conf['ExamFile'],people,
  ( "ENTER", 0, "KEY",          Person,
    "STORE", 0, "id",           "STRING",
    "ENTER", 0, "exams",        "VEC",
    "ENTER", 1, "KEY",          Exam,
    "STORE", 2, "totalscore",   "INT",
    "STORE", 3, "maxscore",     "INT",
    "STORE", 4, "scores",       "STRING" ) )

groupdesc = AsciiData.FileDescription(Config.conf['GroupFile'],people,
  ( "ENTER", 0, "KEY",          Person,
    "STORE", 0, "id",           "STRING",
    "STORE", 1, "group",        "INT" ) )

messagedesc = AsciiData.FileDescription(Config.conf['MessageFile'],people,
  ( "ENTER", 0, "KEY",          Person,
    "STORE", 0, "id",           "STRING",
    "ENTER", 0, "messages",     "VECT",
    "STORE", 1, "NEXT",         "STRING" ) )

def cleanRevokedMessages():
    '''This little function cleans revoked messages. If the administrator
       deletes a private message, it is not really deleted but only revoked.
       This means, that a new message is appended, that starts with a dollar
       sign and repeats the text of the message before. Such messages cancel
       the previous ones by way of this function.'''
    for k,p in people.iteritems():
        i = 0
        while i < len(p.messages):
            if len(p.messages[i]) > 0 and p.messages[i][0] == '$':
                j = 0
                while j < i and p.messages[j] != p.messages[i][1:]: 
                    j += 1
                if j < i:   # found a revoked message
                    del p.messages[i]
                    del p.messages[j]
                    i -= 2   # will be inkremented in a second.
            i += 1

# Here comes a little statistic about the exercises classes or "groups":
# Under each key we store

groups = {}

class GroupInfo(Utils.WithNiceRepr):
    '''Object containing general information about a tutoring group.'''
    people = []        # list of participants by their ID
    number = -1        # number of group ( = its key in 'groups')
    passwd = ''        # encrypted password for tutor access
    tutor = ''         # name of tutor
    place = ''         # description where the group meets
    time = ''          # description when the group meets
    emailtutor = ''    # email of tutor
    groupinfo1 = ''    # customization info for use on group specific web pages 
    groupinfo2 = ''    # customization info for use on group specific web pages 
    groupinfo3 = ''    # customization info for use on group specific web pages 
    groupinfo4 = ''    # customization info for use on group specific web pages 
    groupinfo5 = ''    # customization info for use on group specific web pages 
    groupinfo6 = ''    # customization info for use on group specific web pages 
    groupinfo7 = ''    # customization info for use on group specific web pages 
    groupinfo8 = ''    # customization info for use on group specific web pages 
    groupinfo9 = ''    # customization info for use on group specific web pages 

    def __init__(self, number = -1):
        self.people = []
        self.number = number

def AddToGroupStatistic(p):
    '''Adds a person to the groups statistic.'''
    global groups
    g = str(p.group)
    if not(groups.has_key(g)): groups[g] = GroupInfo(g)
    groups[g].people.append(p.id)

def MakeGroupStatistic():
    global groups
    for k in people.keys():
        p = people[k]
        AddToGroupStatistic(p)

# General information about tutoring groups 
groupinfodesc = AsciiData.FileDescription(Config.conf['GroupInfoFile'],groups,
  (  "ENTER", 0, "KEY",        GroupInfo,
     "STORE", 0, "number",     "INT",
     "STORE", 1, "passwd",     "STRING",
     "STORE", 2, "tutor",      "STRING",
     "STORE", 3, "place",      "STRING",
     "STORE", 4, "time",       "STRING",
     "STORE", 5, "emailtutor", "STRING",
     "STORE", 6, "groupinfo1", "STRING",
     "STORE", 7, "groupinfo2", "STRING",
     "STORE", 8, "groupinfo3", "STRING",
     "STORE", 9, "groupinfo4", "STRING",
     "STORE", 10, "groupinfo5", "STRING",
     "STORE", 11, "groupinfo6", "STRING",
     "STORE", 12, "groupinfo7", "STRING",
     "STORE", 13, "groupinfo8", "STRING",
     "STORE", 14, "groupinfo9", "STRING"    )  )

