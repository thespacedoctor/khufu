from __future__ import print_function
from builtins import str
import os
import unittest
import shutil
import yaml
from khufu.utKit import utKit
from fundamentals import tools
from os.path import expanduser
home = expanduser("~")

packageDirectory = utKit("").get_project_root()
settingsFile = packageDirectory + "/test_settings.yaml"

su = tools(
    arguments={"settingsFile": settingsFile},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName=None,
    defaultSettingsFile=False
)
arguments, settings, log, dbConn = su.setup()

# SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
moduleDirectory = os.path.dirname(__file__)
pathToInputDir = moduleDirectory + "/input/"
pathToOutputDir = moduleDirectory + "/output/"

try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
def setUpModule():
    "set up test fixtures"
    moduleDirectory = os.path.dirname(__file__)

    # SETUP PATHS TO COMMONG DIRECTORIES FOR TEST DATA
    global pathToInputDataDir, pathToOutputDir, pathToOutputDataDir
    pathToInputDataDir = moduleDirectory + "/input/data/"
    pathToOutputDir = moduleDirectory + "/output/"
    pathToOutputDataDir = pathToOutputDir + "data/"

    # SETUP THE TEST LOG FILE
    global testlog
    testlog = open(pathToOutputDir + "tests.log", 'w')

    return None

def tearDownModule():
    "tear down test fixtures"
    # CLOSE THE TEST LOG FILE
    testlog.close()
    return None

# SETUP AND TEARDOWN FIXTURE FUNCTIONS
def setUpFunc():
    "set up the test fixtures"

    return None

def tearDownFunc():
    "tear down the test fixtures"

    return None
