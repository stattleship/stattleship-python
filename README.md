# stattlepy

Stattleship PYTHON Wrapper brought to you by [@stattleship](https://twitter.com/stattleship).

Check out the [Stattleship API](https://www.stattleship.com) - The Sports Data API you've always wanted

Affordable. Meaningful. Developer-Friendly.

:football: :basketball: and :black_circle: with :baseball: coming soon. 

We're gonna need a bigger :boat:!

## Differences From R API wrapper

Due to '''type''' function in python, to indicate the type of stat you would like to query, use the '''stat_type''' variable in the API call 

## Install
```
git clone https://github.com/stattleship/stattleship-python.git
cd /PATH/TO/DIRECTORY/
sudo python setup.py install
```


## Getting Started
Obtain an access TOKEN from [stattleship.com](www.stattleship.com). Load Python and initialize your TOKEN for your session and load the library:

```
from stattlepy import Stattleship
New_query = Stattleship()
Token = New_query.set_token('YOUR_TOKEN')
Output = New_query.ss_get_results(sport='basketball',league='nba',ep='game_logs',player_id='nba-stephen-curry')
```


