## Metagaming

------

Metagaming is a blog centered around videogames.It contains a vast array of content such as reviews, previews, opinion articles and even streaming. Users can sign up/login and interact with posts by commenting and upvoting/downvoting them.   


The link to the deployed website can be found [here.](https://metagaming.herokuapp.com/)

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
   - [Carousel](#carousel) 
   - [Blog Posts](#blog-posts)
   - [Footer](#footer)
   - [Post Detail](#post-detail)  
   - [Authentication](#authentication)
   - [Future Features](#future-features)    


[Models](#models)   

   - [Post Model](#post-model)
   - [Comment model](#comment-model)
   - [Diagram](#diagram)


[Testing](#testing)   

   - [General Testing](#general-testing)
   - [Validator Testing](#validator-testing)
   - [Responsiveness Testing](#responsiveness-testing)

[Bugs and Issues](#bugs-and-issues) 

[Site Deployment](#site-deployment) 

[Credits](#credits)   

   - [Media](#media)
   - [Content](#content)
   - [Acknowledgements](#acknowledgements)  
  


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

- dbdiagram for the models diagram

- W3C CSS Validator to validate CSS

- W3C Markup Validator to validate HTML

- Codebeautify to make HTML and CSS easier to read


## features  
<a name="features"></a>
------

### Top Page
<a name="top-page"></a>
  
At the top of the page lies there is a navbar with a short welcome message and the Home/Signup/Login options. If the user is already logged in, the options change to Home/Sign out. Below, there is an background image with the Metagaming name and logo. 

![logo/navbar image](/static/media/images/nav.png "logo and navbar")



### Carousel
<a name="carousel"></a>

Below the Metagaming image, there is a carousel that contains 3 posts. The first is fixed, displaying a message to sign up. The remaining two are the last posts created in the blog. On the right, there is a search bar so users can search for the content they desire. There are 3 additional side widgets, Upcoming Events, Recommended Games and Recommended Streamers below the search bar.   

![carousel image](/static/media/images/carousel.png "carousel")

### Blog Posts
<a name="blog-posts"></a>

The blog posts are displayed below the carousel. Each page contains up to 6 posts, that include image, author, category, date, title and excerpt. The users can open the posts either by clicking on the image or on the read more button.

![blog image](/static/media/images/posts.png "blog")


### Footer
<a name="footer"></a>

This is where users can find all the social media links. The background color is the same as the navbar to maintain visual consistency. There are aria labels in all of the links for screen readers. 

![footer image](/static/media/images/footer.png "footer")



### Post Detail
<a name="post-detail"></a>

Whenever a uder clicks on a post, they will open the post detail page. Inside it, there is all the relevant information such as author, image, category and date, followed by the text content. At the bottom of the page, there is are upvote/downvote buttons and a comment section so users can show the way they feel about that content. Those are features that can only be accessed by registered users. 

![post detail ](/static/media/images/postdetail.png "post-detail")
![post detail2 ](/static/media/images/postdetail2.png "post-detail2")


### Authentication
<a name="authentication"></a>

This blog contains 3 authentication related pages: login, sign up and sign out. The login page includes a link to the sign up page and vice versa. That way, users can complete their desired action in an intuitive manner. 

![login image](/static/media/images/login.png "login")
![sign up image](/static/media/images/sign-up.png "sign up")
![sign out image](/static/media/images/sign-out.png "sign out")


### Future Features
<a name="future-features"></a>

- List of upvoted posts
- Search by categories
- Save posts 


## Models
<a name="models"></a>

------

### Post Model
<a name="post-model"></a>

![Post Model image](/static/media/images/post-model.png "post-model")
![Post Model image2](/static/media/images/post-model2.png "post-model2")

### Comment Model
<a name="comment-model"></a>

![Comment Model image](/static/media/images/comment-model.png "Comment-model")

### Diagram
<a name="diagram"></a>

![Diagram image](/static/media/images/dbdiagram.png "Diagram")


## Testing
<a name="testing"></a>

------

### General Testing
<a name="general-testing"></a>

- Nav Bar: When a user is logged in, Home and Sign Out appears on the nav bar as opposed to Home, Sign In and Sign Up.

![non-authenticated image](/static/media/images/nav.png "non-authenticated")
![authenticated image](/static/media/images/nav2.png "authenticated")

- Comment Section and Upvotes/Downvotes: When a user is authenticated, they can comment and upvote/downvote the post. For those who are not, the comments and upvotes/downvotes still appear, but in an non-interactive way(see image below).  

![non-authenticated comment/upvote/downvote image](/static/media/images/comment-signout.png "non-authenticated comment/upvote/downvote")

- In this scenario, the user is logged in and has both upvoted and downvoted the post(for testing purposes), which is why both buttons have a red background.

![authenticated comment/upvote/downvote image](/static/media/images/comment.png "authenticated comment/upvote/downvote")

- Edit/Delete Comment: If authenticated, the user can delete or edit a comment they made. Pressing delete will permanently erase the comment, while pressing edit will take the user to the screen shown below. 

![edit/delete image](/static/media/images/edit.png "edit/delete")

- Sign in message: After logging in, a successful sign in message appears for two seconds.

![sucessful sign in image](/static/media/images/sign-in-message.png "successful sign in")

- Sign out message: After signint out, a successful sign out message appears for two seconds.

![sucessful sign out image](/static/media/images/sign-out-message.png "successful sign out")

- Search bar: When a search is performed, a list of posts that match said search appear.

![search image](/static/media/images/search.png "search")



### Validator Testing
<a name="validator-testing"></a>

HTML- No errors were shown when put through the [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffranciscobarreira.github.io%2Fjavascript-project%2F)

CSS- No errors were shown when put through the [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffranciscobarreira.github.io%2Fjavascript-project%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=pt-BR)


### Responsiveness Testing
<a name="responsiveness-testing"></a>

This blog was designed with the help of bootstrap, which is a mobile first design tool. The website is responsible to all sorts of different devices. 


## Bugs and Issues
<a name="bugs-and-issues"></a>

------

- No username in comments: The username was not showing in the posted comments. This was because I wrongly set comment_form.instance.username = request.user.username. The problem was fixed when i changed it to comment_form.instance.name = request.user.username.

- Categories bug: I could not get the full name to display in the post category, as it was not getting the human readable value. To fix this, I used the get_FOO_display.

- Carousel bug: The carousel featured in the home page was presenting 4 posts when it should be limited to 3. This was fixed by using slice:2. 




## Site Deployment
<a name="site-deployment"></a>

------

The Metagaming repository was created on GitHub by following these steps:

- Select the Code Institute template

- Click create new repository after naming it 

- Click on the green Gitpod button to create the workspace


This site was deployed to Heroku. To do so, I followed the steps in the [Django Blog cheatsheet.](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)




## Credits
<a name="credits"></a>

------

### Media
<a name="media"></a>

All the images used in the blog were taken from other websites, including:

- Google images for all the images in the posts, the Metagaming page header and placeholder image.
- Twitch.tv for the images in the recommended streamer widget.

I do understand that it is better to use sites such as unsplash for images, but given the highly specific nature of the images required I decided to use google images.

All the icons were taken from "Font Awesome".

### Content
 <a name="content"></a>

For this project, the following sources of information were used:

- Stackoverflow for various code related doubts

- Django documentation for ideas on how to make ideas come true

- All the post content was taken from IGN.com, Gamespot.com and Destructoid.com

- The I think, therefore I do project for helping with login and pagination.


### Acknowledgements
 <a name="acknowledgements"></a>

 I want to thank the following people for helping me with this project:

 - My mentor, Akshat Garg, for helping me go in the right direction

 - The tutors at CodeInstitute for helping me sort small issues with the blog.