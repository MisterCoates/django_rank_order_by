This repository was created to reproduce an issue I'm seeing when Django is 
generating SQL for sqlite3 with the Window() class.
Any help those viewing this repository could provide is appreciated.

Steps to reproduce (using fixtures to load test data):

    python -m venv venv
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py loaddata rank_test
    python manage.py runserver

The error occurs when the evaluation of the queryset takes place in 
rank/templates/rank/index.html.

If you set a breakpoint in the view and review the SQL for the queryset 
you will see the following:

    SELECT 
        "rank_ranktest"."id", 
        "rank_ranktest"."name", 
        "rank_ranktest"."category", 
        "rank_ranktest"."rating", 
        RANK() OVER (CAST(ORDER BY "rank_ranktest"."rating" AS NUMERIC)) AS "rank" 
    FROM "rank_ranktest"

The syntax for the CAST should not take place prior to the ORDER BY, 
but inside of it. The manually corrected SQL pasted below runs and 
returns the expected result:

    SELECT
        "rank_ranktest"."id",
        "rank_ranktest"."name",
        "rank_ranktest"."category",
        "rank_ranktest"."rating",
        RANK() OVER (ORDER BY CAST("rank_ranktest"."rating" AS NUMERIC)) AS "rank"
    FROM "rank_ranktest"
    