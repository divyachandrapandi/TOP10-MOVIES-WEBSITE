# TOP10-MOVIES-WEBSITE
using sqlite3, sqlalchemy, bootstrap, jinja, flask -- a website created
1. SETUP FLASK SERVER

2. SETUP BOOTSTRAP CLASS OBJECT

3. JINJA USED "EXTEND" TO EXTEND BASE.HTML FROM BOOTSTRAP
            ~ {%block title%}
            ~ {%block styles%}
            ~ {%block content%}

4. INCLUDE WTFORMS IN "edit.html"

5. BLOCK STYLES ARE USED
           ~ super() ---> INHERIT MAIN BOOTSTRAP STYLES ADDITIONALLY,
           ~ GOOGLE FONT
           ~ STATIC FILES URL FOR CSS STYLE

6. CREATE SQLALCHEMY DATABASE ---> TABLE ---> MOVIE ---> ENTRY WITH ATTRIBUTE (ID, TITLE, REVIEW, DESCRIPTION, RATING,
                                                                    YEAR, RANKING, IMG)
7. IN home(),
            USING QUERY BY ALL,
            SEND THE MOVIE TO RENDER TEMPLATE 'index.html'

8. IN "index.html",
            ~ ADD FOR LOOP AND
            ~ ADD ALL ATTRIBUTE IN RESPECTIVE PLACES FOR THE FRONTEND TO WORK {{movie.title}}

9. TO UPDATE THE RATING AND REVIEWS, GOTO update()
            ~ in update(id), id is passed as argument which is movie.id
            ~ calling form
            ~ for rating, review update, render 'edit.html'
            ~ submit through post method
            ~ if success, then update using SQLALchemy
            ~ redirect to home

10. TO ADD NEW MOVIE ,
            ~ IN add(), call form for title
            ~ submit through post
            ~ to get movie database, apikey needed, and endPoint
            ~ use requests.get to connect with url and query
            ~ with the data, render 'select.html' data

11. IN 'select.html', THE MOVIE TITLE , MOVIE YEAR FROM MOVIE DATABASE GENERATED FROM API IS LISTED WITH LIST OF RANGE
    MOVIES WE CAN CHOOSE FROM THAT

12. ADD A <A> TAG FOR MOVIES LIST --> DIRECT TO api_to_db() with movie.id[TMDB id] pass it on /select/<int:id>

13. AGAIN SEARCH SPECIFICALLY WITH MOVIE ID IN API DATABASE AND PASSING MOVIE ID TO ENDPOINT AS WELL

14. EXTRACT TITLE, YEAR, DESCRIPTION ,IMAGE AND CREATE A NEW MOVIE OBJECT INSIDE OUR TABLE

15. REDIRECT TO update() WITH ID AS NOW TABLE.DATA.ID

16. WITH HOLD OF THAT ID, WE CAN CHANGE RATINF, REVIEW AND WHEN SUBMIT---> REDIRECT TO HOME PAGE

17. tO SORT OUT THE RANKING, ORDER BY IS USED , ALONG WITH RANKING IS ADDED BY LENGTH IN FOR LOOP

18. NOW EVERYTHING DONE!!!!!!!!!!!!!!!!!!!
