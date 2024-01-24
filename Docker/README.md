Task name => Docker

Task preparation => what preparation is necessary to perform the task?
  First we make a folder named Docker where we will put all the needed files inside.
  Then we make a HTML folder where we will put the index.html file inside. 

Task implementation => what is the way you have implemented this? 
  We make a Dockerfile where we will put parameters inside so that Docker when building will use these parameters.
 # FROM httpd:2.4
 # COPY html/index.html /usr/local/apache2/htdocs/
 # COPY html/datescript.js /usr/local/apache2/htdocs/

 # EXPOSE 80

  Then we will put inside the index.html file the text and code that we want to be seen on the browser

 # <!DOCTYPE html>
# <html lang="en">
# <head>
 #   <meta charset="UTF-8">
  #  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  #  <title>DevNet Associate Skills Test: Danny Rodriguez Rincon</title>
   # <style>
    #    body {
    #        font-family: Arial, sans-serif;
    #        margin: 40px;
    #    }

  #      h1 {
    #        color: #333;
  #      }

  #      p {
   #         color: #666;
    # }
#    </style>
# </head>
# <body>
#    <h1>DevNet Associate Skills Test</h1>
 #   <p>Created by: Danny Rodriguez Rincon</p>
 #   <p id="datetime"></p>

  #  <script src="datescript.js"></script>
    
# </body>
# </html>

After this we will create a function who will work on the object with id "datetime" to show the current time

# document.addEventListener("DOMContentLoaded", function() {
    
 #   function updateDateTime() {
      
  #      var currentDate = new Date();
   #     var formattedDateTime = currentDate.toLocaleString();
    #    document.getElementById("datetime").innerText = formattedDateTime;
   # }

   # // Initial call to update date and time
   # updateDateTime();

   
   # setInterval(updateDateTime, 1000);
# });

Terminal: 

--> docker stop my-apache-container
--> docker rm my-apache-container
--> docker run -d -p 8080:80 --name my-apache-container my-apache-image

https://github.com/DannyRodriguezRincon/Devasc-Skills_DannyRodriguez/blob/2d809be02bb0d8eaaf364b9c85abbd9bb1c4ebe9/Docker/Docker-commands-terminal.png


Task troubleshooting => what were the problems encountered? Did not have any problem with it.

Task verification => proof of the quality of the result

Screenshot at 2024-01-24 10-20-06
https://github.com/DannyRodriguezRincon/Devasc-Skills_DannyRodriguez/blob/19dbf088cc8c505a5d24c0252dfb1624df42bf9b/Docker/Docker-localhost.png
