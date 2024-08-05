# Port Bounce

The goal here was to have a easy way to bounce a large number of ports at once.

Specifically, the problem here was APs that would need to be power-cycled to prepare for a software update to be pushed from the WLC. I wrote this so that we could handle the several thousand APs that needed to be attended to. This was also useful for Cisco Phones as they would sometimes fail to negotiate POE settings properly due to a conflict with LLDP and CDP running on our L2 switches.  
