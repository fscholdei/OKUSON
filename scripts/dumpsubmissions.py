#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# 
#   Copyright (C) 2007 by  Frank L�beck
#  
#   $Id:$
#
import sys,os,time

# get paths right
homedir = os.path.abspath(sys.path[0])
okudir = os.path.join(homedir, '..') 
os.environ["OKUSONHOME"] = okudir
sys.path = [os.path.join(okudir, 'server')] + sys.path

# read config
import Config
Config.ReadConfig()
Config.PostProcessing()

# read exercises and sheets
from fmTools import Utils, AsciiData
Utils.Error('Reading exercises and sheets...',prefix='Info: ')
import Exercises
for d in Config.conf['ExerciseDirectories']:
    Exercises.ReadExercisesDirectory(d)
for d in Config.conf['SheetDirectories']:
    Exercises.ReadSheetsDirectory(d)

# list of triples (number, name, sheet)
sheets = Exercises.SheetList()

# read data
import Data
Utils.Error('Reading personal data...',prefix='Info: ')
Data.peopledesc.LoadFile()
Utils.Error('Reading multiple choice data...',prefix='Info: ')
Data.mcresultsdesc.LoadFile()

Utils.Error('Dumping (to stdout) all submissions in lines of format:',
             prefix='Info: ')
Utils.Error('id:sheetname:exercisenr:questionnr:variantnr:answer:mark',
             prefix='Info: ')

# now dump the data sheet-wise
for s in sheets:
  for k in Data.people:
    # the data of person with id k
    p = Data.people[k]
    try:
      mc = p.mcresults[s[1]]
      # the submitted answers
      answers = AsciiData.TupleLine(mc.submission,'|')
      # the marks in the same order
      marks = mc.marks
      # corresponding exercises as tuples (sheetname,number,question,variant)
      tmp = s[2].ChooserFunction(hash(p.id))
      choice = []
      for i in range(0, len(tmp)):
        if tmp[i] != None:
          for a in tmp[i]:
            choice.append((s[1],str(i),str(a[0]),str(a[1])))
      #print k,choice,marks,answers
      for j in range(0, len(choice)):
        l = (k,)+choice[j]+(answers[j], marks[j])
        print AsciiData.LineTuple(l)
    except:
      # do nothing if nothing submitted for sheet s
      pass



sys.exit(0)

