# HackUMBC Fall 2017
A Parking Solution for UMBC

# Problem
Finding a parking spot during prime-time school hours can be time consuming,
very time consuming. Personally I have been in situations where I come to
school 40 minutes early for class and still end up 5 minutes late after looking
for a parking spot for 35 minutes, and then walking 10 minutes to class because
you ended up in some of the furthest away lots possible.

A Common Technique that I have observed from UMBC students is to systematically
pass by every single parking space in the first lot, then do the same in the
next lot, and so on until you either find a spot or loop back to the first spot.

Your best chance of getting a spot at times like these is to search for a pedestrian
walking towards the lot, and follow them back to their spot, and take it as soon as
they leave.


## Real Aricteture
'''
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
           |                 ==========                          |
           |                 |  UMBC  |                          |
                             | 1: 15  |   The Display Device     |
          |^|                | 2: 50  |
          |@|                | 3: 2   |                         |^|
                             |--------|                         |@|
                             |        |

Diagram Key
 |^| = Parking Sensor  || --> = Symphony Link   ||
 |@|                   ||                       ||
 
'''

## Simulation Arcitecture
'''
                        ==========                          
                        |  UMBC  |    The Display Device                         
                        | 1: 15  |      / Parking Server.
     |^| --> --> -->    | 2: 50  |
     |@|                | 3: 2   | <-- <-- <-- <-- <-- <-- |^|
                        |--------|                         |@|
                        |        |

==================================================
 |^| = Parking Sensor  || --> = TCP Connection  ||
 |@|    App            ||                       ||
==================================================
'''

