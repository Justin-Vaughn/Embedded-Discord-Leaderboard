# GuildXP
###Creates a leaderboard of users based on total daily experience

Developed a program that would display users’ accumulated experience gained in games. The program also tracks trends, total experience gained, and the positions of each user in chronological order.

- Parsed API using a combination of Python and JSON
- Created an algorithm to compare and display user’s statistics and trends in Python
- Operated the program using Discord.py library to display the leaderboard whenever a user ran a specific command

![image](https://imgur.com/oIdK2F1.png)

- The total group experience is tracked at the top "Total Guide XP"
  - The percent increase represents how well the group did in caparison to the day before

- This list shows the top 10 users with the most experience in the guild
- Each user also has a ranking among themselves
  - Arrows represent if the user moved up/down/remained the same ranking in the top 10
  - The number assocated at the end of each user is how many positions that user moved up since the previous day
