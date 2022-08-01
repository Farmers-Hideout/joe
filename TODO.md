# Farmer Joe's Todo List
This is farmer Joe's todo list, this is where you can find what has to be done

## cogs/functions
This is the folder functions holding economy and fun
### economy.py
- [ ] Add businesses and corporations (ref: https://top.gg/bot/512079641981353995?campaign=13-2) IT SHOULD BE FARMS / BOT FARMS NOT BUSINESSES
    - [ ] Add potential to own businesses 
        A business will be able to be purchased as many times as you please.
        A business will have these parameters:
            - Income/min
            - Price that increases by some number on whatever you buy like cookie clickers work for idle money
            - Quantity of stuff owned of that business

    - [ ] Add potential to own corporations
        A corporation is a team of people that can work together on a business and compete on corporation leaderboards.
        The more you upgrade a corporation the more people you can have in it.
        A corporation will have these parameters:
            - Cash
            - Level
            - Employees
            - Chief Executive Farmer
            - Multiplier
            - Daily Boost
            - Corporation Age
            - Placement on corporation leaderboard
    - [ ] Add "lootboxes" basically crates 
    - [ ] Add "gems/coins" that you keep after prestiging 
    - [ ] Add prestiging (needing prestige gems/coins) Prestiging will also add a new business you can buy
    - [ ] Add daily money bonus that gets bigger for everyday like a streak
    - [ ] Add researching to make income bigger or cost better for businesses
    - [ ] Ability to buy prestige points
    - [ ] Account creation
        - Will create account if any commands needed with an account is done
        - Will delete an account after 30 days of no interactions. (Decaying accounts)
    - [ ] Buy multipliers from 5% to 100% making 100% cheaper than buying 20 5%
    - [ ] Add leaderboards
    - [ ] Income
        Income will work like this;
        The bot will not update your balance before you do any commands, that way it does not have to put a lot of CPU pressure and will only update what you have earned by taking the difference in minutes when you save a datetime object in the database and calculate based on total income.


### fun.py
 - [ ] Brainstorm