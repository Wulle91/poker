# Poker

Poker is a family of gambling games in which players bet into a pool, called the pot, the value of which changes as the game progresses that the value of the hand they carry will beat all others according to the ranking system. Variants largely differ on how cards are dealt and the methods by which players can improve a hand. For many reasons, including its age and its popularity among Western militaries, it is one of the most universally known card games in existence.



![Responsice Mockup](https://github.com/Wulle91/poker/blob/main/assets/images/am_i_responsive.PNG)

### Ho to play

In poker, players form sets of five playing cards, called hands, according to the rules of the game. Each hand has a rank, which is compared against the ranks of other hands participating in the showdown to decide who wins the pot. In high games, like Texas hold 'em and seven-card stud, the highest-ranking hands win. In low games, like razz, the lowest-ranking hands win. In high-low split games, both the highest-ranking and lowest-ranking hands win, though different rules are used to rank the high and low hands.

Each hand belongs to a category determined by the patterns formed by its cards. A hand in a higher-ranking category always ranks higher than a hand in a lower-ranking category. A hand is ranked within its category using the ranks of its cards. Individual cards are ranked, from highest to lowest: A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3 and 2. However, aces have the lowest rank under ace-to-five low or ace-to-six low rules, or under high rules as part of a five-high straight or straight flush. Suits are not ranked, so hands that differ by suit alone are of equal rank.

There are nine categories of hand when using a standard 52-card deck, except under ace-to-five low rules where straights, flushes and straight flushes are not recognized. An additional category, five of a kind, exists when using one or more wild cards. The fewer hands a category contains, the higher its rank. There are 311 875 200 distinct hands, because the order in which cards are dealt or arranged in a hand does not matter. Moreover, since hands differing only by suit are of equal rank, there are only 7,462 distinct hand ranks.


![Poker](https://github.com/Wulle91/poker/blob/main/assets/images/poker.PNG)


### Featurs

Random card generation

- Card are shuffled and dealt to the computer and player

- Players cards are shown and computers hidden

- Player has to chose which chard he wants to discard by typing card position

- These cards will be discarded and ne dealt to player and computer

- Computer has its on logic witch card to discard and which to hold


![Game](https://github.com/Wulle91/poker/blob/main/assets/images/initial.PNG)




- After we click enter our cards and computer cards ill be shown 

- Score will be updated and deck shuffled

- Card will be dealt and a new game begins

- After every game score updates as long as we play



![Game](https://github.com/Wulle91/poker/blob/main/assets/images/game1.PNG)

- If we type some other data then number we will get an error message telling us to input proper data.


- Card will be dealt and a new game begins



![Game](https://github.com/Wulle91/poker/blob/main/assets/images/error.PNG)

## Data Model 

I decided to make card game for two players, every player gets 5 cards and can decide which and how munch he'd like to change

Winning system has approximate 120 winning combinations where the computer decides who wins.

Every game deck is shuffled new and dealts as it would be in real life, player and computer decide how to play in their best interest.



- __Bugs__

  - As i was doing my project I encoutered many bugs, i didn't know how complex would this be to make and as i work on logic it became more and more complex so i often made errors in logic or improperly used functions or methods, often string with numbers misplaced and forever shearched where and what went wrong 
           
  - Whenn i was first done with the app i hade two functions with approx. 150 lines of code, it took a big chunk of my time tring to make my code "atomic"


- __Deployment__

  Steps for deployment:
             
  - Fork or clone this repository
  - Create new Heroku app
  - Set the buildbacks to Python and Hode.JS in that order
  - Link the Heroku app to repository
  - Click on Deploy

- __Testing__

  I have manually tested this project by doing following:

  - Passed code throught PEP8 liner and confirmed there are no problems.
            
  - Given invalid inputs: strings when numbers are expected or out of bounds inputs

  - Tested in my local terminal and the code intitute Heroku terminal

![Landing Page](https://github.com/Wulle91/poker/blob/main/assets/images/validator.PNG)


`Poker`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Cards shuffle | Shuffels card for every neww game | Played over and over again | Every time new cards | Pass |
| Cards dealt | Discarding card, getting new and keeping good cards | Discarded cards | Old ones stay, new come, always have 5 cards| Pass |
| Validate input | Should joust number from 1-5 take | Gave correct number, wrong number and words | On correct number game goes on else comes error message| Pass |
| Loop into new game | After the game finishes, new game should start | Game finished | New started | Pass |
| Calculate winner | Validate cards trough 7 functions for both players | Printed all possible cases | Shows points depending on winning cards | Pass |
| Keep score | After every game update overall score to keep track who won more times | Game played | Score updates execpt wenn is tie | Pass |
| Keep cards properly till end of game | Card are dealt as they come out of deck and kept for person as for PC | Printed cards of PC | Keeping cards as expected | Pass |
| Computer logic | Computer deciding ich card to hold and ich to deicard  | printed all the steps trough functions | Cards hold and dicards as expected | Pass |

I confirmed that the form works: requires entries in every field, will only accept number in the inpput field, and the errors work properly.



## Credits 

### Content 

- Code institute for deployment terminal     
- Stack overflow on numerous occasions. I looked all the time how have others solved problems as mine, which methods did they use and did we have the same or different logic for the same problems.  
- Wikipedia for the details of the Poker game




