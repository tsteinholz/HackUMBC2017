# HackUMBC Fall 2017
A Parking Solution for UMBC.

# Problem
Finding a parking spot during prime-time school hours can be time-consuming,
very time-consuming. Personally, I have been in situations where I come to
school 40 minutes early for class and still end up 5 minutes late after looking
for a parking spot for 35 minutes, and then walking 10 minutes to class because
you ended up in some of the furthest away lots possible.

A Common Technique that I have observed from UMBC students is to systematically
pass by every single parking space in the first lot, then do the same in the
next lot, and so on until you either find a spot or loop back to the first spot.

Your best chance of getting a spot at times like these is to search for a pedestrian
walking towards the lot, and follow them back to their spot, and take it as soon as
they leave.

# Solution
To fix this problem, I am proposing a system that will track how many spots are 
available in which parking lots. So that when drive into UMBC expecting to find
a parking spot in a reasonable time, in the best possible location, they know
exactly where to go.

## How are we going to track what spots are available?
Using pneumatic vehicle counters on every parking lot entrance/exit. These
vehicle counters will be able to collect...

* Direction of Travel (in or out of the parking lot)
* Speed
* The distance between vehicles
* The length of each vehicle

per vehicle. When this data is collected over a substantial period of time
it can be used to make infrastructure improvements, view seasonal trends,
improve traffic flows, and much more.

While all this data can be collected optionally, the only thing we really
care about for this application is the direction of travel for each car.

## How will this data be transferred from the parking lot into the cloud?
Using Symphony Link from Link Labs. Symphony Link is a wireless solution for
enterprise and industrial customers who need to securely connect their IoT
devices to the cloud. Symphony Link is optimized for low power and wide range
which makes it a great candidate for this project.

### RXR / RLP Communication Modules
Each parking sensor device will need a Link Labs RXR or RLP Communication Module
which can connect to the Link Labs Gateway.

### Gateway
This powerful device manages security, uplink and downlink, and much advanced low power, wide-area (LPWA) features only available with Symphony Link. For data backhaul, the gateway features ethernet, WiFi, 3G cellular, or 4G LTE.
The Link Labs Gateway should be installed on one of the two cellular towers that
are registered to the University of Maryland: Baltimore County. This would give
the Gateway a great enough range to cover the entire campus. Although more gateways
might need to be installed if capacity is too great (more than a hundred modules
connected to one gateway).

## How will students view this data from the cloud?
Once we get the data to the cloud, it can go anywhere we want it to go. While
most people would make this a "Parking App", I think that is problematic. We
should not encourage students to drive while looking at their phone. This is not
a "hands-free" app and will need to be looked at in the car. An app is not the
answer to this question.

We should install Symphony connected signs that show up-to-date numbers for the
cars that are in each lot. These signs need to be in strategic locations (such as
the UMBC entrances and in front of the Lots, etc.) that can be discussed and modified
at a later date with more specifics. These signs will display a table of the selected
lots and how many available spaces it has.

The display signs will use the same RXR/RLP Communication Modules to connect to the
Symphony Network.

## Real Architecture Diagram

                       _                                  
                     (`  ).                     _           
                    (     ).      The       .:(`  )`.       
                   _(       '`.     Cloud  :(   .    )      
               .=(`(      .   )     .--    `.  (    ) )      
              ((    (..__.:'-'   .+(   )     ` _`  ) )                 
              `(       ) )       (   .  )       (   ) 
                ` __.:'   )     (   (   ))       `-'.
                       --'       `- __.'

                                  ^
                                  |

                            ____\__/___
                            { LinkLabs }
     |^|  --> --> --> -->   | Gateway  |
     |@|   ^                {----------}  <-- <-- <-- <-- <-- <--
           |                      ^                              ^
           |                      |                        |^|   |
           |                      |                        |@|   |
           |                 //////////                          |
           |                 |  UMBC  |                          |
                             | 1: 15  |   The Display Device     |
          |^|                | 2: 50  |
          |@|                | 3: 2   |                         |^|
                             |--------|                         |@|
                             |        |

### Diagram Key

    |^| = Parking Sensor
    |@|
    
    
    --> = Symphony Link
 

## Simulation Architecture Diagram

                        //////////                          
                        |  UMBC  |    The Display Device                         
                        | 1: 15  |      / Parking Server.
     |^| --> --> -->    | 2: 50  |
     |@|                | 3: 2   | <-- <-- <-- <-- <-- <-- |^|
                        |--------|                         |@|
                        |        |

### Diagram Key

    |^| = Parking Sensor
    |@|    Client
    
    
    --> = TCP Connection
    
