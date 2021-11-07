#Tests of project 2 twitter 

import twitterceshi as tc
import time
import helper as hp


#Functionality under normal use case 
def test_input_sentence():
    tc.API_credentials()
    result = tc.twitter_search()
    if len(result):
       hp.console_print('Keyword accepted')
    else:
        hp.console_print('No keyword detected')
    
#Error handeling: 

def test_API_credentials():
    hp.console_print('testing the credential status')
    api = tc.API_credentials()
    try:
        if api:
            hp.console_print('credential passed')
    except:
        hp.console_print('missing credential information')



#Performance: how long it took the program to run
def test_runtime():
    hp.console_print('testing how long it took the program to run')
    start = time.clock()
    tc()
    end = time.clock()
    print('running time: %s seconds' %(end - start))