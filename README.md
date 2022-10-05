# check_router_tasmota
Script for checking the router of the second ISP in Multi-WAN, which sometimes freezes.
Given that I did not have access to control the router, I was forced to use the smart socket. 

Script is watching for the state of the router and reboot frozen router via smart socket.
The smart socket was flashed with Tasmota open source firmware.
All actions are performed via an HTTP curl request to the Tasmota API.
