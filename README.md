# AnsibleModuleForHTTP
An Ansible Module for getting the HTTP Return code from a website
## Overview
An Ansible Module written in Python to get the return code of a HTTP Request from a given URL
## Requirements
 - You need to have a user on the remote server configured with passwordless sudo.
- The remote server should also have ssh configured based on Ansible's requirements
## How to use
-   Begin by first cloning the repository with the command:  `git clone https://github.com/vishalbala-nps/AnsibleModuleForHTTP`
-   Change the IP Address of the remote server in the inventory file (or don't change anything if you want to use localhost)
- You can change the URL in the play.yml file under the module name get_status_code
## About HTTP Return Codes
HTTP response status codes indicate whether a specific HTTP request has been successfully completed. All the response status codes are 3 digit numbers 
Responses are grouped in five classes:
- Informational responses
	- The Response Code starts with the digit `1`
	- Example: `102 - Processing` when the server takes time to process
-  Successful responses
	- The Response Code starts with the digit `2`
	- Example: `200 - OK` a typical success response
-  Redirects
	- The Response Code starts with the digit `3`
	- Example: `301 – Resource Moved Permanently` when a URL has been moved permanently to a new one
-  Client errors
	- The Response Code starts with the digit `4`
	- Example: `404 - Page Not Found` a typical failure response when a page does not exist 
-  Server errors 
	- The Response Code starts with the digit `5`
	- Example: `500 – Internal Server Error` when a server encounters an unexpected failure 
