#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on November 15, 2017, at 21:47
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Experiment'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\Connor\\Google Drive\\Courses\\FALL 2017\\PSYCH397\\Experiment\\Predicting-Help-Seeking-Behaviour\\Experiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "start"
startClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='In the following experiment you will be presented with a series of questions. \n\nYour job will be to indicate your responses using a slider.\n\nIf you have any questions before you begin, feel free to let one of us know.\n\nPlease press the enter key to continue.',
    font='Times New Roman',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "scenarioTrials"
scenarioTrialsClock = core.Clock()
likelihood = visual.RatingScale(win=win, name='likelihood', textSize = .5, marker=u'triangle', 
size=2, pos=[0.0, -0.5], showAccept = False, showValue = False, 
choices=[u'Definitely Not\n     (0%)', u'Probably Not\n     (25%)', u'Possibly\n   (50%)', u'Quite Probably\n     (75%)', u'Definitely\n   (100%)'], 
tickHeight=-1, markerStart=u'50')
Scenario = visual.TextStim(win=win, name='Scenario',
    text='default text',
    font='Times New Roman',
    pos=(0, .6), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
qPrompt = visual.TextStim(win=win, name='qPrompt',
    text='What is the likelihood that you will seek help from the course instructor?',
    font='Times New Roman',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
proceedInstructions = visual.TextStim(win=win, name='proceedInstructions',
    text='Press the enter key to confirm your response',
    font='Times New Roman',
    pos=(0, -.9), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "GPA"
GPAClock = core.Clock()
gpaProbe = visual.TextStim(win=win, name='gpaProbe',
    text=u'Please indicate your overall university average using the slider below.',
    font=u'Times New Roman',
    pos=(0, .4), height=1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
gpaScale = visual.RatingScale(win=win, name='gpaScale', textSize = .4, marker=u'triangle', 
size=2, pos=[0.0, -0.5], showAccept = False, showValue = False,
choices=[u'60-64.9', u'65-69.9', u'70-74.9', u'75-79.9', u'80-84.9', u'85-89.9', u'90-94.9', u'95-100'], 
tickHeight=-1, markerStart=None)
proceedInstructions2 = visual.TextStim(win=win, name='proceedInstructions2',
    text='Press the enter key to confirm your response',
    font='Times New Roman',
    pos=(0, -.9), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
noteText = visual.TextStim(win=win, name='noteText',
    text='Note: We are using intervals of ~5%',
    font='Times New Roman',
    pos=(0, -.2), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='            Thank you for your participation!\n\nPlease press the enter key to exit the experiment.',
    font='Times New Roman',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
startComponents = [text, key_resp_3]
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
scenarios = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('scenario.xlsx'),
    seed=None, name='scenarios')
thisExp.addLoop(scenarios)  # add the loop to the experiment
thisScenario = scenarios.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisScenario.rgb)
if thisScenario != None:
    for paramName in thisScenario.keys():
        exec(paramName + '= thisScenario.' + paramName)

for thisScenario in scenarios:
    currentLoop = scenarios
    # abbreviate parameter names if possible (e.g. rgb = thisScenario.rgb)
    if thisScenario != None:
        for paramName in thisScenario.keys():
            exec(paramName + '= thisScenario.' + paramName)
    
    # ------Prepare to start Routine "scenarioTrials"-------
    t = 0
    scenarioTrialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    likelihood.reset()
    key_resp_2 = event.BuilderKeyResponse()
    Scenario.setText(scenarioDescrip)
    # keep track of which components have finished
    scenarioTrialsComponents = [likelihood, key_resp_2, Scenario, qPrompt, proceedInstructions]
    for thisComponent in scenarioTrialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "scenarioTrials"-------
    while continueRoutine:
        # get current time
        t = scenarioTrialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *likelihood* updates
        if t >= 0.0 and likelihood.status == NOT_STARTED:
            # keep track of start time/frame for later
            likelihood.tStart = t
            likelihood.frameNStart = frameN  # exact frame index
            likelihood.setAutoDraw(True)
        continueRoutine &= likelihood.noResponse  # a response ends the trial
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *Scenario* updates
        if t >= 0.0 and Scenario.status == NOT_STARTED:
            # keep track of start time/frame for later
            Scenario.tStart = t
            Scenario.frameNStart = frameN  # exact frame index
            Scenario.setAutoDraw(True)
        
        # *qPrompt* updates
        if t >= 0.0 and qPrompt.status == NOT_STARTED:
            # keep track of start time/frame for later
            qPrompt.tStart = t
            qPrompt.frameNStart = frameN  # exact frame index
            qPrompt.setAutoDraw(True)
        
        # *proceedInstructions* updates
        if t >= 0.0 and proceedInstructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            proceedInstructions.tStart = t
            proceedInstructions.frameNStart = frameN  # exact frame index
            proceedInstructions.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scenarioTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "scenarioTrials"-------
    for thisComponent in scenarioTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for scenarios (TrialHandler)
    scenarios.addData('likelihood.response', likelihood.getRating())
    scenarios.addData('likelihood.rt', likelihood.getRT())
    # the Routine "scenarioTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'scenarios'


# ------Prepare to start Routine "GPA"-------
t = 0
GPAClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
gpaScale.reset()
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
GPAComponents = [gpaProbe, gpaScale, key_resp_4, proceedInstructions2, noteText]
for thisComponent in GPAComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "GPA"-------
while continueRoutine:
    # get current time
    t = GPAClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gpaProbe* updates
    if t >= 0.0 and gpaProbe.status == NOT_STARTED:
        # keep track of start time/frame for later
        gpaProbe.tStart = t
        gpaProbe.frameNStart = frameN  # exact frame index
        gpaProbe.setAutoDraw(True)
    # *gpaScale* updates
    if t >= 0.0 and gpaScale.status == NOT_STARTED:
        # keep track of start time/frame for later
        gpaScale.tStart = t
        gpaScale.frameNStart = frameN  # exact frame index
        gpaScale.setAutoDraw(True)
    continueRoutine &= gpaScale.noResponse  # a response ends the trial
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *proceedInstructions2* updates
    if t >= 0.0 and proceedInstructions2.status == NOT_STARTED:
        # keep track of start time/frame for later
        proceedInstructions2.tStart = t
        proceedInstructions2.frameNStart = frameN  # exact frame index
        proceedInstructions2.setAutoDraw(True)
    
    # *noteText* updates
    if t >= 0.0 and noteText.status == NOT_STARTED:
        # keep track of start time/frame for later
        noteText.tStart = t
        noteText.frameNStart = frameN  # exact frame index
        noteText.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GPAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GPA"-------
for thisComponent in GPAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('gpaScale.response', gpaScale.getRating())
thisExp.addData('gpaScale.rt', gpaScale.getRT())
thisExp.nextEntry()
# the Routine "GPA" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [text_2, key_resp_5]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
