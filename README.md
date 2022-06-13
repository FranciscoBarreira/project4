## Metagaming

------

Mtagaming is a blog centered around videogames.It contains a vast array of content such as reviews, previews, opinion articles and even streaming. Users can sign up/login and interact with posts by commenting and upvoting/downvoting them.   


The link to the deployed website can be found [here.](https://franciscobarreira.github.io/javascript-project/)

The link to the Github repository can be found [here.](https://github.com/FranciscoBarreira/project4/)


![mockup site generator image](/static/media/images/mockup-metagaming.png "mockup preview")

## Table of Contents 

[User Experience](#user-experience)

   - [User Requirements](#user-requirements)
   - [User Stories](#user-stories)

[Design](#design)   

   - [Images](#images)
   - [Colour Scheme](#colour-scheme)
   - [Fonts](#fonts)

[Technologies Used](#technologies-used) 

[Features](#features)   

   - [Top Page](#top-page)
   - [Page Image](#page-image) 
   - [Quiz Section](#quiz-section)
   - [End Results Section](#ending-results-section)
   - [Footer](#footer)  


[Testing](#testing)   

   - [General Testing](#general-testing)
   - [Validator Testing](#validator-testing)
   - [Responsiveness Testing](#responsiveness-testing)

[Site Deployment](#site-deployment) 

[Credits](#credits)   

   - [Media](#media)
   - [Content](#content) 
  


## User Experience 
<a name="user-experience"></a>

------


### User Requirements 
<a name="user-requirements"></a>

- The website should be easy to navigate
- The posts should include the category to understand the topic in discussion
- Commenting and upvoting/downvoting should be featured
- The website's visuals should be maintained across all pages
- Login/signup process should be quick and intuitive
- The website should adapt to different screen sizes on different devices


### User Stories
 <a name="user-stories"></a>

In order to better organize the workflow using agile tools, a series of user stories were created in the project repository. Those can be seen below:
 
![user stories image 1](/static/media/images/user_stories1.png "user stories")
![user stories image 2](/static/media/images/user_stories2.png "user stories2")
![user stories image 3](/static/media/images/user_stories3.png "user stories3")
![user stories image 4](/static/media/images/user_stories4.png "user stories4")

The users stories read as follows:

- Search Bar : As a user I can search for different topics so that I get the exact content I want.
- Create Post : As an admin I can create a new post so that I can add content to the website. 
- Login: As a user I can register or login so that I have access to all the site's benefits.
- Upvotes/Downvotes: As a user I can upvote and downvote comments so that I can express my opinion towards the content of the post.
- Number of Upvotes/Downvotes: As a user I can see the number of upvotes or downvotes so that better content becomes more easily distinguishable.
- Approve Comments: As a site admin I can approve or reject comments so that I can assure no distasteful comments are public.
- Draft Posts: As an admin I can draft posts so that I can write them ahead of time.
- Post List: As a user I can view a list of posts so that choose the content I want to interact with.
- Delete Post: As a site admin I can delete posts so that I can assure certain types of content are not present in the site.
- Comment Section: As an authenticated user I can comment on a post so that I can give my opinion on the topic.
- Search Filter: As a user I can filter the posts so that I can look for specific content.
- Edit Post: As an admin I can edit a post I created so that I can correct possible mistakes.


## Design
 <a name="design"></a>

 ------

### Images 
<a name="images"></a>


All the images used in the blog were taken from other websites, including:

- Google images for all the images in the posts, the Metagaming page header and placeholder image
- Twitch.tv for the images in the recommended streamer widget

### Colour Scheme 
<a name="colour-scheme"></a>

The colour scheme chosen for the blog were:

- #fff white for text, as it it is a very standard, easy to read colour
- #212429 grey in the nav-bar, read me more buttons
- #990099 purple in the widgets, username of the user who posted the article and username in comments when the user is logged in. 
- #212529 grey for text (slightly different than nav grey as it reads better).

### Fonts 
<a name="fonts"></a>

Tittillium Web is used for the headings and widgets due to its visual appeal. The rest of the text is in Roboto, a font that improves readability.

## Technologies Used
<a name="technologies-used"></a>

------



- HTML

- CSS

- Python

- Django

- GitHub for software hosting

- GitPod for development hosting

- Heroku for project deployment

- Summernote for adding fields to the posts

- Google fonts to add custom fonts to the website

- Font Awesome for icons

- Bootstrap for quick HTML mobile first design

- Cloudinary for online image storage

- W3C CSS Validator to validate CSS

- W3C Markup Validator to validate HTML

- Codebeautify to make HTML and CSS easier to read


## features  
<a name="features"></a>
------

### Top Page
<a name="top-page"></a>
  
At the top of the page lies there is a short 

![logo image](/assets/images/home-quiz.png "logo")



### Page Image
<a name="page-image"></a>

As shown in the image above, the home page contains two small containers, "Your Goals" and "Start Quiz". The first contains the information on how many right answers it would take to reach a certain tier. Users can choose to skip that information and just start the quiz right away, instead. 



### Quiz Section
<a name="quiz-section"></a>

This is the main page of the website. It is where users will take part in the quiz. It consists of a quiz container, that holds both the questions and the answers, and a home button underneath so that the home page is always within reach. On the bottom of the quiz container, there is a counter so users can know how many right answers they have so far. When a user clicks the right answer, it turns green, otherwise, it turns red. At that point, a next button (which is hidden by default), shows up. By clicking it, the next question will appear, the right answers counter will update, and the colors(red or green) will disappear.   

![quiz](/assets/images/quiz.png "quiz")


### End Results Section
<a name="end-results-section"></a>

After clicking the next button on the final question, the whole quiz container will be hidden, and the final results container will be displayed. It contains the final number of right answers out of 15, and it reminds the user of how many it was required to be in each tier. Finally, there is a home and a start the quiz button. 

![final results](/assets/images/end.png "final results")


### Footer
<a name="footer"></a>

This is where users can find all the social media links. The background color is goldenrod to maintain visual consistency. There are aria labels in all of the links for screen readers. 

All the icons were taken from "Font Awesome".

![footer section](/assets/images/footer-quiz.png "footer")


## Testing
<a name="testing"></a>

------

### General Testing
<a name="general-testing"></a>


### Validator Testing
<a name="validator-testing"></a>

HTML- No errors were shown when put through the [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffranciscobarreira.github.io%2Fjavascript-project%2F)

CSS- No errors were shown when put through the [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffranciscobarreira.github.io%2Fjavascript-project%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=pt-BR)

JavaScript - No errors were shown when put through JShint validator, as shown in the image below.

![jshint test](/assets/images/jshint.png "jshint test")

### Responsiveness Testing
<a name="responsiveness-testing"></a>

The website responsiveness was tested using Chrome Dev Tools and was physically tested on a Samsung S20. It generally responded well to the different devices, however, there was a need to implement some changes, such as:

-Reducing the Logo font size to keep it from overflowing into the body of the page

-restructuring the quiz answers to keep them from overflowing the container

-repositioning the home and next button as they were negatively affecting each other's position in smaller screens  

-making width and margin related adjustments to the scorecard page to prevent it from deforming

-making width and margin related adjustments to the hidden div in the quiz page to prevent it from deforming


## Site Deployment
<a name="site-deployment"></a>

------

This site was deployed to GitHub pages. The steps to deploy it were:

-In the GitHub repository, click on on settings 

-Scroll down to Github pages

-From the source section drop-down menu, select Main 

-After all these steps are followed successfully the page will refresh and provide a link to the deployed website.



## Credits
<a name="credits"></a>

------

### Media
<a name="media"></a>

The background image used in the website was taken directly from Unsplash.com.

All the icons were taken from "Font Awesome".

### Content
 <a name="content"></a>

For this project, the following sources of information were used:

-Stackoverflow and w3schools for various code related doubts

-The idea for the increment score functions was initially taken from the Love Math walkthrough project.