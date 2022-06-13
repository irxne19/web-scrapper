# _Web-Scrapper_

#### By _**Irene Mathew, Rahul Sharma**_

#### _Displays title of webpage_

## Technologies Used

* _Python 3.10.1_

## Description

The python file takes a webpage as an input and displays the title of the webpage

## Installation Requirements

* Docker should be installed on your system. Visit [get-docker](https://docs.docker.com/get-docker/) for more info.

## Steps to Run

* Clone the repository to your desktop.
* Navigate to the directory using CLI.
* To build the Docker image: **docker build -t web-scrapper --rm .**
* There are two methods to run the Docker image:
    * _Default (Website used: google.com) : **docker run web-scrapper**_
    * _Dynamic (Website used: user-provided): **docker run web-scrapper webpage-link**_
