# Queries

sqlite> SELECT * FROM tstest_apirequests;

    1|/posts/1/|GET|12|200|2017-11-16 07:35:35.775873
    2|/posts/2/|GET|11|200|2017-11-16 07:35:46.117000
    3|/posts/|GET|7|200|2017-11-16 07:35:57.622038
    4|/uses/|GET|2|404|2017-11-16 07:36:18.357550
    5|/users/1/|DELETE|3|500|2017-11-16 07:36:38.894064
    6|/users/2/|PUT|3|500|2017-11-16 07:36:47.654048
    7|/users/2/|PUT|5|400|2017-11-16 07:44:49.681600
    8|/posts/2/|GET|4|200|2017-11-16 07:55:19.412934
    9|/users/2/|GET|2|400|2017-11-16 08:07:46.940976


### Write a query that returns the total number of api_requests where the status code was 200?

    sqlite> SELECT COUNT(*) FROM tstest_apirequests WHERE status_code = 200;
    4


### Write a query that gives the count, and average response_ms for every api_endpoint. Sorted by the average

    sqlite> SELECT COUNT(api_endpoint), api_endpoint, AVG(response_ms) AS avg_response FROM tstest_apirequests GROUP BY api_endpoint ORDER BY avg_response;
    1|/uses/|2.0
    1|/users/1/|3.0
    3|/users/2/|3.33333333333333
    1|/posts/|7.0
    2|/posts/2/|7.5
    1|/posts/1/|12.0


### Write a query that gives the total count of api_requests per hour ordered by the hour

    sqlite> SELECT COUNT(*), strftime('%Y-%m-%d:%H', received) AS hour FROM tstest_apirequests GROUP BY hour ORDER BY hour;
    8|2017-11-16:07
    1|2017-11-16:08


### Write a query that gives the total number api requests for each status code, includes the actual code and the description from the second table

    sqlite> SELECT COUNT(*), ar.status_code, sc.description FROM tstest_apirequests ar LEFT JOIN tstest_statuscodes sc ON ar.status_code = sc.status_code GROUP BY ar.status_code ORDER BY ar.status_code;
    4|200|Good!
    2|400|Bad request
    1|404|
    2|500|Server error


# How to run the server

    # Initial setup
    cd tstest
    ./setup.sh  # hopefully there will be no errors

    # then visit http://localhost:8080/fibonacci/

    # If you want to run the server after you've done initial setup already, just do
    ./runserver.sh
