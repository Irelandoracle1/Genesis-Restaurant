# Genesis Restaurant
## Introduction
Genesis Restaurant is a Nigerian Food Restaurant(Fictional) Located in Dublin,
Ireland. It offers seamless online booking functionality, allowing customers 
to reserve a table with just a few clicks. With an intuitive user 
interface and responsive design, customers can easily navigate the menu 
and select their preferred dining experience. Genesis Restaurant's website
Targets Nigerians that lives in Ireland, in order to give them an home away
from home.
<img src="https://github.com/Irelandoracle1/Genesis-Restaurant/blob/main/assets/images/responsiveimage2.jpg">

 [View Live Project Here](https://genesisrestaurant234.herokuapp.com/)

  
## Table of Contents

[Introduction](#introduction)

[UX-DESIGN](#ux-design) 
    - User Stories
        -  Guest User's Stories
        -  Registered User's Stories
        -  Site Admin's Stories
    - [Kanban Board](#kanban-board)
     -[Typography](#typography)
    - [Color Scheme](#color-scheme)
    * [Wireframes](#wireframes)
  
[Features](#features)

[Database Schema](#database-schema)

[Technology Stack Used](#tech-stack-used)
[Testing](#testing)

* [Validator Testing](#validator-testing)

* [Manual Testing](#manual-testing)

[Clone](#clone)

[Deployment](#deployment)

[Credits](#credits)

[Acknowledgements](#acknowledgements)

 ### User stories 

    -   #### Guest User's Stories

       1. View Website Contents: As a Guest User, I can easily understand the purpose of the website and learn through the contents and site presentation
       2. View Menu: As a Guest User, I can view the restaurant's menu online, so that I can make informed choices while booking a table. 
       3. Site Navigation: As a Guest User, I can easily navigate through the website to easily find desired contents
      4. Account Registration: As a Guest User, I can register for an account on the website, so that I can book a table for dining
      5. View Social Media Pages: As a Guest User, I can navigate to restaurant's Social Media Pages, to get more information about them
        

    -   #### Registered User's Stories

       1. Account Login: As Registered User, I can login to my account so I can make bookings 
        
       2. View Bookings: As a Registered User, I can view and manage my upcoming and past bookings in my account, so that I can keep track of my dining history 
       
       3.Modify or Cancel Existing Bookings: As a Registered User, I can modify or cancel my existing bookings, so that I can make changes to my dining plans if needed 

    -   #### Site Admin's Stories
        As a Site Admin, I can create, read, update and delete Users' bookings from an admin area
        
        
# Layout
-   ### Design
    -   #### Colour Scheme
        -   The colours used throughout the website include include: Black, Lavender and blue  
    
    -   #### Imagery
        -   Imagery was chosen to go with the website's colour and content theme. I'm using dining and restaurant interior images with deep-toned, soothing colours and attractive graphics. For the edit, delete and logout page I'm using images with graphics that signal what will happen if user edits, deletes or signs out.

*   ### Wireframes
    -   #### Changes original ideas 
           
        - I had to make some deviations from the original Wireframe at the point of development stage
    -   #### Links to Wireframes

        -   Home Page Wireframe - [View](https://github.com/Irelandoracle1/Genesis-Restaurant/blob/main/assets/images/layout1.jpg)

        -   Booking Page Wireframe - [View](https://github.com/Irelandoracle1/Genesis-Restaurant/blob/main/assets/images/layout2.jpg)

        -   Registration Page Wireframe -[View](https://github.com/Irelandoracle1/Genesis-Restaurant/blob/main/assets/images/layout6.jpg)

        -   Login Page Wireframe - [View](https://github.com/Irelandoracle1/Genesis-Restaurant/blob/main/assets/images/layout7.jpg)


# Deployment

### Heroku

The project was created in Github first and then transferred to the Gitpod development environment by the use of the green Gitpod button.

## Initial Deployment  
- ### When creating a Django project, it is highly advisable to deploy early, due to the compexities of the development process and the actual application.

1. In the Gitpod environment a skeleton django project was created (project, app and relating files).
2. A Heroku app was created in Heroku.
3. In Heroku, under the Resources tab, in Add-ons, I searched for Postgres. When found I submitted a request to use it. 
This attached Heroku Postgres to my project in Heroku.
4. In the Heroku Settings tab I clicked on "Reveal Config Vars" and copied the automatically added postgres link from beside the DATABASE_URL variable. 
5. In Gitpod dev environment, I looked for the env.py file that was automatially generated from the CI template at the beginning. This file stores environment variables.
6. After importing the os into the env.py file, I added the database URL from Heroku into env.py.
7. I added a secret key in the env.py file after having it generated on the [Django Secret Key Generator - MiniWebtool](https://miniwebtool.com/django-secret-key-generator/) website.
8. I added the secret key into the Heroku Settings > config vars as well.
9. In the settings.py file in Gitpod I imported os and added an if statement saying that outside the development environment the environment variables must be used from env.py, including the secret key.
10. Still in the settings.py file, I commented out the present code for databases and added code to use the currently set up django database URL as set in the env.py file and also in the Heroku config vars.
11. I migrated these changes in Gitpod using python3 manage.py migrate
12. To get static and media sites stored on Cloudinary, I went to the dashboard of my previously created Cloudinary account and copied the API Environment Variable.
13. I added this to the Gitpod env.py file and into the Heroku Settings > config vars. 
14. I also added DISABLE_COLLECTATIC = 1 to the Heroku config vars. 
15. I added cloudinary and cloudinary_storage to the installed apps in settings.py. 
16. I set up the static file storage, static file directory, the static root, the media url, the default file storage and the templates directory in settings.py.
17. I added the Heroku name followed by herokuapp.com to the ALLOWED_HOSTS variable name in settings.py, followed by a comma and 'localhost' (to allow running in the development environment).
18. I created 3 directories at the top level: media, static, templates.
19. I created a Procfile at the top level directory. 
20. I did a git add, git commit and git push.
21. In the Deployment tab in Heroku, in Deployment method, I added Github, set up Enable Automated Deployment, looked for my Github repository, connected my Heroku app to it and clicked on Deploy Branch at the bottom of the page.
22. When I opened the app after the app was built and deployed, I saw the success message page with a rocket.
23. After  my application was built, as the first step of the final deployment I turned Debug to False in the settings.py file in Gitpod.
24. In Heroku I removed the DISABLE_COLLECTSTATIC variable.
25. I saved my changes on all my files and performed a git add, git commit and git push.
26. As automatic depoyment had been enabled in Heroku, I waited until my app was built, then I opened it and made sure that all functionalities work.

# Credits 

### Code

-   The structure and the code of the project was mainly based on two project walkthroughs by Code Institute:
    * Hello Django - I created CRUD functionalities based on this walkthrough.
    * I think therefore I blog - I created authentication and messages functionalities based on this walkthrough and followed the deployment steps described here. 

-   [Will Fly For Food](https://www.willflyforfood.net/food-in-nigeria/) Food Images 

-   [Official Django Documentation](https://docs.djangoproject.com/en/3.2/) was researched for syntax, code expressions, code functionalities.

-   Stack Overflow was was researched for syntax, code expressions, code functionalities, problem solving. Validation function for reservation date and time is from there.

-  













