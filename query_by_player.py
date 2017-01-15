""" this is a command line tool to get specific stats by player
check associated excel file query_by_player_terms.xlsx to get possible --l2 and --l4 terms to use
output written to outfile.txt in same directory"""

import argparse
from stattlepy import Stattleship

def get_level2_data(Output, l2value):
    level3 = (Output[0])[l2value]
    return level3

def get_level4_data(level3, l4value):
    outfile = open('outfile.txt', 'w')

    for item in level3:
        outfile.write(str(item[l4value]))
        outfile.write("\n")

    outfile.close()
    return


parser = argparse.ArgumentParser()

parser.add_argument('--p', '-player_id', type=str, dest='p_id', help='Player ID', metavar='pid')
parser.add_argument('--l2', '-level2_key', type=str, dest='l2key', help='Player ID', metavar='l2')
parser.add_argument('--l4', '-level4_key', type=str, dest='l4key', help='Player ID', metavar='l4')

args = parser.parse_args()

New_query = Stattleship()

Token = New_query.set_token("dacf8c48e6a2261ee169e2d09a379840")

Output = New_query.ss_get_results(sport = "basketball", league="nba", ep="game_logs", player_id = args.p_id)


#Output is a list of 1 dictionary

#To get attributes
#for item in Output:

    #for item2 in item.keys():
        #print "##########", item2

        #for item3 in item[item2][0]:

            #print item3

level3_data = get_level2_data(Output, args.l2key)
get_level4_data(level3_data, args.l4key)
