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
Insert Here
