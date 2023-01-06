# Kibana-and-Flask

Creating Basic Flask WebServer and then Creating a Wrapper for Kibana to filter logs on the basis of User roles.

This repo contains all the details of how you can configure a flask server for fetching logs from any es server be it hosted or not.

Some Points to remeber - 

1. To help make your user experience awesome, You can add three things - (AutoComplete, Fuzzy Searching and a Dedicated UI) We did not need these as our api's would be communicating the same instead of a Human.

2. Once you get the results from the cluster It is essential to check for the queries and parameters and then Build up what we call as Dynamic Search Queries (Sounds Good) and then utilising those queries to filter out the required results.

3. You might be thinking that this is standard but when you will run it on a large file with lots of data and Indexes, then you will find the difference, To get on that understand these things: (Lucene, Parallel Scanning, Difference between Scan and search)

To be continued.
