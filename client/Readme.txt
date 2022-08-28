Structure of Client:

To facilitate builds, the following folder structre and rules should be adopted when building Client.

*** Folder Structure
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