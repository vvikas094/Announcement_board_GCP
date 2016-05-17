# Announcement_board

1. The website is an announcement board where you can show your announcements among teammembers. 
2. The website first redirects you to google's account login page. After you login and give permission to access your name, you are redirected to a "Announcement Board" page where you can share announcements with others.
3. The website first acquires the user nickname and displays the name on the page at various locations. It also shows a logout url on the top. When a text is entered and submitted, the text is stored in a database and last 25 announcements are retrieved at the same time.If the text is empty, it does not store in the database. The retrieved texts are shown below in the order of which they are entered(latest first).  
4. The website automatically refreshes every 25 seconds, so that the new announcements are visible. 

The app engine services that i used are : App Engine Datastore, Google User Management.
