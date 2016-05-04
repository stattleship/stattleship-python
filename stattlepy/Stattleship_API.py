import requests
import json
import math
import time

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
                
                ### walk function IN PROGRESS
                if(walk):
                        
                    ### append the results from pages 2+ to the response list
                    while 'link' in return_header:
                        for p in range(2,pages+1):
                            
                            ### set page number to pass to API call
                            page = p 
                            
                            ###if verbose print out which page it is returning
                            if verbose:
                                print 'Retrieving results from page',p,'from',pages
                                
                            tmp_p, return_header_p = self.query_api(sport, league, ep, param, version, walk, page, verbose, token)
                            
                            response.append(tmp_p)
                            
                            ### delay in making call
                            time.sleep(0.5)
                        
                print 'Stattleship API request complete'                
                return(response)
            
        def query_api(self, sport, league, ep, param, version, walk, page, verbose, token):
        
                ### make sure that the sport, league and ep are all lower case
                sport = sport.lower()
                league = league.lower()
                ep = ep.lower()        
                
                url = 'https://www.stattleship.com/{}/{}/{}'.format(sport, league, ep)
                
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
                    print res.headers
    
                content = json.loads(res.content)
                
                return(content, res.headers)
