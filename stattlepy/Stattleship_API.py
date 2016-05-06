#!/usr/bin/env python

#Install: 
#git clone https://github.com/stattleship/stattleship-python.git
#cd /PATH/TO/DIRECTORY/
#sudo python setup.py install

#Usage:
#New_query = Stattleship()
#Token = New_query.set_token('YOUR_TOKEN')
#Output = New_query.ss_get_results(sport='basketball',league='nba',ep='game_logs',player_id='nba-stephen-curry')

import requests
import json
import math
import time
import re

### Main class that all Stattleship functions will be a part of
class Stattleship(object):
        
        # function to set the token
        def set_token(self, pro_token):        
                if pro_token is None or not isinstance(pro_token,basestring):
                         warnings.warn('Stattleship API token must be provided in order to access the Stattleship API.')
                else:
                        global token
                        token = pro_token
                
        ### function to get the results for them Stattleship API
        def ss_get_results(self,**kwargs):

                # initial defaults for all variables
                sport = "hockey"
                league = "nhl"
                ep = "teams"
                query = list()
                version = 1
                walk = False
                page = 1
                verbose = True
                place = None
                stat_type = None
                param = {}
                
                # loop through inputs and 
                for key, value in kwargs.iteritems():
                        if str(key) == 'sport':
                                sport = value
                        elif str(key) == 'league':
                                league = value
                        elif str(key) == 'ep':
                                ep = value
                        elif str(key) == 'version':
                                version = value
                        elif str(key) == 'walk':
                                walk = value
                        elif str(key) == 'page':
                                page = value 
                        elif str(key) == 'verbose':
                                verbose = value
                        elif str(key) == 'stat_type':
                             param['type'] = value
                        else:
                                param[key] = value
                
                ### initial verbose to indicate request occurring
                if verbose:
                    print'Making Initial API Request'
                    
                ### initial query       
                tmp, return_header = self.query_api(sport, league, ep, param, version, walk, page, verbose, token)
               
                ### make response list
                response = list()
               
                ### set the original first parsed 
                response.append(tmp)
                
                ### walk function using REGEX to idenify the next link in the header to pull next request 
                if(walk):
                    while 'link' in return_header:
                        
                        ### Next link to request from the API
                        next_link = re.findall( 'rel="last", <(.*?)>; rel="next"', return_header['link'], re.MULTILINE)
                        
                        ### Use try and except to see if the next link was found within the header
                        try:
                            if verbose:
                                print 'Next link sent to API:'
                                print next_link[0]

                            headers = {
                            'Authorization': token,
                            'Accept':'application/vnd.stattleship.com; version=%s' %version,
                            'Content-Type':'application/json'        
                            }

                            res = requests.get(next_link[0], headers = headers)

                            content = json.loads(res.content)

                            response.append(content)

                            return_header = res.headers

                            ### delay in making call
                            time.sleep(0.1)
                            
                        except IndexError:
                            break
                        
                print 'Stattleship API request complete'                
                return(response)
            
        def query_api(self, sport, league, ep, param, version, walk, page, verbose, token):
        
                ### make sure that the sport, league and ep are all lower case
                sport = sport.lower()
                league = league.lower()
                ep = ep.lower()        
                
                ### base url to make the request from
                url = 'https://www.stattleship.com/{}/{}/{}'.format(sport, league, ep)
                
                ### depends on page being requested
                if page >= 1:
                        param['page'] = page
                
                headers = {
                        'Authorization': token,
                        'Accept':'application/vnd.stattleship.com; version=%s' %version,
                        'Content-Type':'application/json'        
                         }
                
                res = requests.get(url,params=param, headers = headers)
                
                if verbose:
                    print res
                    print res.url
                
                content = json.loads(res.content)
               
                return(content, res.headers)