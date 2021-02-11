# uzduygu21
* For my final project, I decided to create a financial advisory website.  I wanted to create a website that had functionality for both a financial advisor and separately for his clients to login. This website is designed to allow clients to login and see their accounts and also allow for an advisor to interact with his clients.  I created the advisor as a super user.

* I have used multiple web technologies that I learned throughout the course and projects and have implemented some of those technologies within the website.  I used HTML5, CSS3, Bootstrap 4, Google Material Design, Django, Python, and JavaScript. 

* This project is unique from my other class projects.  The first thing I wanted to do was create a more visual and appealing user interface.  I was able to incorporate images that gave the website a more complete feel.  I have also expanded upon what I learned in my past projects.  I created a top bar and footer for the website as well. I also used google icons as buttons to give  a better user interface.

* This project has been more complex that the other projects for a number of reasons.  Account, questions to advisor and quiz pages have different layouts and functionalities depending on if the advisor or the client is viewing the page.  They are all mobile responsive pages using the bootstrap grid system.

* I incorporated JavaScript by creating a 10 question quiz for the client which shows their investment knowledge.  The scores are kept in the database.  Another complex part of the project including creating a modal window.  When the client asks a question or gets their scores for the quiz, they will see this window.  I did this using Bootstrap 4.

## Run the application:
	1. Download the code from https://github.com/me50/uzduygu21/tree/web50/projects/2020/x/capstone.
	2. Run python3 manage.py makemigrations
	3. Run python3 manage.py migrate
	4. Run python3 manage.py runserver
	5. Create a super user account for advisor: python3 manage.py createsuperuser
	6. Then you can login website as an advisor
	7. You can just register to see website as a client.

##### Below is an outline of the different functionalities of the project, what's contained in each file:
* Linking CSS, Bootstrap, Google icons, scripts, top bar, navigation bar and footer is in layout page for reusability. Take a look at /finance/templates/finance/layout.html.
* Home, about, services, history pages are single-page-app. Take a look at finance/templates/finance/index.html. The route of this page is default. Even if you are not a client or you didn’t log in you can still see these pages and get information about the company. They are all mobile-responsive pages. I have created different layouts for client and advisor.  I did this using HTML5, CSS3, Bootstrap 4 and JavaScript.
* Check finance/urls.py where url configurations of this app defined. The route for login is /login and check /finance/templates/finance/login.html. The route for logout is /logout and it navigates to default route HTML is /finance/templates/finance/index.html. The route for register is /register and template is /finance/templates/finance/register.html.

#### As a client;

* Client can log in/register. For registration client needs to provide username, first name, last name, email address and password. Take a look at finance/models.py. There’s the models of my application. I have created User model that represents each user of my application. It inherits from AbstractUser.
* After logging in client can send question/concerns to advisor(super_user) through Home, About or Services pages. Check it from finance/templates/finance/index.html. They all include a question section. After sending a question, modal pop-up appears and lets the client know question has been sent to advisor. I have used Bootstrap 4 for creating modal pop up. Take a look at finance/models.py. I created Contact model that represents each questions that send from clients to advisor.
* Client also has an Accounts tab after logging in. The route for Accounts page is /account. Take a look at /finance/templates/finance/client.html.  Accounts tab includes profile information of user. And it includes Foreign exchange rates today button. It shows table of some exchange rates daily. I performed GET request to Foreign Exchange Rates API for getting daily rates and show the rates in dark table which I implemented using Bootstrap 4. 
* In accounts page client can also add an account by providing bank name, account number and amount. Take a look at finance/models.py. I created Account model that represents each accounts that client add. When client click plus sign button which I used Google icons, there’s section appears to add account.  If the client decides not to add an account after hitting the plus button, they can hit the minus button to close the section.
* In accounts page client can also edit or delete the account that they already added. Check finance/urls.py. I have created the path using /del_edit/<int:account_id>. I did DELETE request from JavaScript for deleting from database and POST request to edit account details. I have used Google icons for delete and edit buttons.
* Client has resource center tab which includes quiz that client can take to see their financial knowledge. Take a look at finance/urls.py to see the path /quiz. Template of this page is /finance/templates/finance/quiz.html. That’s a 10 questions and multiple choices quiz. I calculated their score in frontend (finance/static/finance/index.js)and send to database to keep. I created Quiz model that represents each quizzes that has been taken from client.  After taking the quiz they see pop-up modal that says advisor will see their results. I have used modal pop up from Bootstrap 4. I wanted to include this section because it is important to understand the clients knowledge.

#### As an advisor:
* Home, About and Services pages (/finance/templates/finance/index.html) has button as questions from clients. When advisor clicks on it, he is navigated to questions page. Take a look at finance/urls.py. You can see /questions path. Check finance/templates/finance/questions.html to see template of questions. There are only 5 questions per page before the next button appears to go to the next page.  If the advisor is not on the first page, the previous button appears. I used pagination from Bootstrap 4. 
* Accounts tab includes all clients detailed information to advisor on the left side of page. On the right of page shows all clients accounts. Take a look at finance/templates/finance/client.html. Advisor is super user and this page showing different layout for advisor by checking if request.user.is_superuser.
* Quiz tab shows all clients scores including their full name and the date they took the quiz. Take a look at finance/templates/finance/quiz.html. Advisor is super user and this page showing different layout for advisor by checking if request.user.is_superuser.