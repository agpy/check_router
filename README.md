# check_router
Script for checking the router of the second ISP in Multi-WAN, which sometimes freezes.
Given that I did not have access to control the router, I was forced to use the smart socket. 

Check if the router is frozen (ping Google DNS), and then reboot it via smart socket.
The smart socket was flashed with Tasmota open source firmware.
All actions are performed via an HTTP curl request to the Tasmota API.
