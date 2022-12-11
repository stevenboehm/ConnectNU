# ConnectNU
## Steven Boehm and Victoria Schaller -- CS 3200 Fall 2022

## Overview
ConnectNU is a club management software, containing three personas - general members, executive board members, and supervisors. The application contains information on roster, dues, participation points, due payments, and event attendance. 

## Walkthrough
https://watch.screencastify.com/v/MyxIHDWt4zfUTKNp9jrL

This code contains the back-end necessary to run an AppSmith UI entitled ConnectNU, available [here](https://appsmith.cs3200.net/app/connectnu/welcome-638fa8645bc9880dbcb1f64a)


### Installation

ConnectNU is launched by navigating into the ConnectNU folder location and launching the Docker containers as follows
```python
docker compose build
```
```python
docker compose up
```

ngrok, utilized to connect the containers on the local server to the AppSmith cloud server is connected as follows
```bash
cd path/to/ngrok/installation
./ ngrok http 4000
```

Forwarding link provided by ngrok is pasted as the URL in the ConnectNU API datasource in the app editor on AppSmith
