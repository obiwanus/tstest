# tstest

sqlite> select * from tstest_apirequests;

    1|/posts/1/|GET|12|200|2017-11-16 07:35:35.775873
    2|/posts/2/|GET|11|200|2017-11-16 07:35:46.117000
    3|/posts/|GET|7|200|2017-11-16 07:35:57.622038
    4|/uses/|GET|2|404|2017-11-16 07:36:18.357550
    5|/users/1/|DELETE|3|500|2017-11-16 07:36:38.894064
    6|/users/2/|PUT|3|500|2017-11-16 07:36:47.654048


### Write a query that returns the total number of api_requests where the status code was 200?

    sqlite> select COUNT(*) from tstest_apirequests where status_code=200;
    3
    sqlite> select COUNT(*) from tstest_apirequests where status_code=500;
    2
    sqlite> select COUNT(*) from tstest_apirequests where status_code=404;
    1


### Write a query that gives the count, and average response_ms for every api_endpoint. Sorted by the average

    sqlite> select COUNT(api_endpoint), AVG(response_ms) as avg_response from tstest_apirequests group by api_endpoint order by avg_response;
    1|2.0
    1|3.0
    2|4.0
    1|7.0
    1|11.0
    1|12.0


### Write a query that gives the total count of api_requests per hour ordered by the hour

    sqlite> select COUNT(*) as num_requests, strftime('%H', received) as hour from tstest_apirequests order by hour;
    8|07


### Write a query that gives the total number api requests for each status code, includes the actual code and the description from the second table

    sqlite> select COUNT(*) as num_requests, ar.status_code, sc.description from tstest_apirequests ar left join tstest_statuscodes sc on ar.status_code = sc.status_code group by ar.status_code;
    4|200|Good!
    1|400|Bad request
    1|404|
    2|500|Server error
