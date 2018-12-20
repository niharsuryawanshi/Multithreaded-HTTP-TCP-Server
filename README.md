# Multithreaded-HTTP-TCP-Server
Given is the sample code for a TCP Multithreaded HTTP server coded in python which handles incoming requests from client and responds them accordingly. Mutual Exclusion is implemented using Python events and centralised coordinator algorithm

The Client generates random integer and uploads it to the server.
The server receives that random integer and waits for particular time as no in integer.
Three clients connect simultaneously and performs this task and mutex is implemented using queue and events which avoids race condition.
