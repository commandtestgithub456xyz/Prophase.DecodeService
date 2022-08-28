# Prophase.DecodeService
Preliminary Task - ProPhase


Structure of Prophase.DecodeService :

To facilitate builds, the following folder structre and rules should be adopted when building Prophase.DecodeService.

*** Folder Structure
Prophase.DecodeService-->
                    Server -> 
                            decodeService -> 

                                ** The main  service project
                                Post method is to convert the encoded hexadecimal value into decoded result
                          Database:
                            No database connection defined
                            
                    Client -> 
                            DecodeRequest -> 

                                ** The main   project
                               Client will request to server to get post response with encoded hexadecimal value.
                               Result:
                                Status Code: 200, Decoded Result: 89 50 70 48

                          Example:-
                                   Change pload value to -->0x74657374206d657373616765
                                   execute server first then client project
                               system return result as
                                Status Code: 200, Decoded Result: test message

                          Database:
                            No database connection defined
