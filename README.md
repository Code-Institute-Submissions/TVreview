# What 2 Watch

## Introduction
What 2 Watch is a website that tells you what next series you should watch on Netflix, Amazon
Prime etc. It is unique in having only tv series so attracts the ‘binge watchers’ as oppose to the ‘film
buffs’ to the website.

## UX

### Project Goals
What to watch came about as a result of lockdown. With people stuck in their homes,
conversations turned to what to watch and series such as ‘Tiger King’ were very popular. When
looking for a new series to watch, there are sources such as IMDB and Rotten Tomatoes.
However, these also include films and the information contained in them is very detailed. I wanted
to create a site that would give basic information on only tv series about whether it was worth
watching or not. Rotten Tomatoes have a user rating and their own rating. I wanted just a rating
and review from people who have watched it.

### Developer Goals
As a developer:
- I want to make a website that has useful information about tv shows
- I want to demonstrate my skills in using a database and CRUD functionality

### User Stories
As a user:
- I want to search for a tv show
- I want to see the reviews of the tv show
- I want to write my own review of a tv show
- I want to rate how good a tv show is
- to see the average rating for a tv show
- I want to sign in
- I want to book mark a show by making it a favourite
- I want to see my history of reviews and favourites
- To be given suggested shows based on my likes

### Design
#### Fonts
The text is a little archaic in style to signify going back to basics- a recommendation from
a friend as oppose to modern data laden websites.
#### Colours
A lot of the popular tv series have mystery and twists involved. The design is dark to signify
mystery. The alert font was initially red but changed to green as the alert does not always mean something bad. Some colour added to the buttons, e.g. the login button to make them stand out more.
#### Icons
I used icons from materialize. These icons are recognisable by the user and they can work out what the function is.
#### Styling
I used Materilize to help to organise my layout. What 2 Watch is the title of the website and is shortened to W2W for the logo. 
The buttons have slightly rounded edges to look more appealing. 

### Wireframes
I created the wireframes on [Balsamiq](https://balsamiq.com/). There were changes to the shortened title (from WtW to W2W). Also, I removed the add tv show and 
decided to import from an API: 

- [Home page on computer](/static/wireframes/home-web.jpg)
- [Profile page on computer](/static/wireframes/profile-web.jpg)
- [TV show page on computer](/static/wireframes/tv-show-web.jpg)
- [Home page on mobile](/static/wireframes/home-mobile.jpg)
- [Profile page on mobile](/static/wireframes/profile-mobile.jpg)
- [TV show page on mobile](/static/wireframes/tv-show-mobile.jpg)
## Features

### Existing Features
- Navbar with links to home page, sign up and login. Changes when logged in so that log out and profile are available
- Search bar for searching tv shows titles from IMDB API
- Ability to sign up and login with user authentication and password validation
- Password stored securely using Werkzeug
- Message flashes to ensure the user knows what is happening
- User, when logged in, can rate and review a tv show
- User profile with their favourite tv shows and their reviews
- ability for user to edit and delete their reviews
- protection against a user rating or reviewing multiple times
- User can navigate back to previously viewed tv show
- User can see the reviews and average star rating for each show
- User can see information pulled from IMDB API about the tv show
- Suggested tv shows similar to the one they are looking at 

### Future Features
- Suggested titles come up as user is searching
- User can search genres, actors etc.
- User can see a trailer for the tv show
- User is given options of where to view the show
- User can view the top rated tv shows on the home page
- Monetise website through advertising and/ or linking to Netflix, Amazon Prime

## Technologies Used
- This project uses HTML5, CSS3, Javascript, Python, Flask and Jinja.
- This project uses [Mongo DB](https://www.mongodb.com) as its database 
- This project uses [Materialize](https://materializecss.com) to support with structuring the website responsively
- This project uses [Google Fonts](https://fonts.google.com) for more interesting fonts
- This project uses [Github](https://github.com)
## Testing
### Debugging
The debugger in flask was used throughout the development stage. This gave me information as to where there was a bug. Manuel debugging was done by printing to the
console. This was particularly helpful when pulling information from the database to check that I had the correct information. Chrome Developer Tools allowed me to view any 
layout issues. This was particularly helpful when laying out the tvshow.html. There are a lot of 'div's and it got confusing as to where the closing 'div's should be. 
### Fixed Issues
- Information required for users to view dependent on whether they had written reviews or not etc. was too complex for Jinja. I used a global variable for whether any user was 
logged in and then was able to have conditional statements in app.py.
- The search term used was being lost as the page redirected meaning no results were being shown. I created a new function which could grab the search term and then pass it into
the next function.
- User was able to use same email address to sign up so needed to find if that email was already in the database before allowing progress.
- Tried to use Javascript to display the correct amount of stars as per the rating. Was difficult to link this to Flask, though, so instead used a loop in Jinja.
- It would have been frustrating for the user to login on the tvshow.html and then have to press the back button to get back. In order to get back to the tv show they last looked at,
I created a session variable for the tv show id.
- Having moved elements around on tvshow.html, there appeared a white space between the sections. Using overflow: none fixed it.
### Manuel Testing
#### Flow of website
![Website Flow](/static/media/flow.jpeg)
#### Nav Links
- Home nav links go to the correct places.
- Login and Sign up nav links working and buttons between the two.
#### Login and Sign up
- Password validator works.
- Check if username/ email exists works.
- Sign Up, logout, login works.

#### Profile
- Link to profile from logged in page works.
- 

## Deployment

## Credits
### Content
### Media
### Code
### Acknowledgements