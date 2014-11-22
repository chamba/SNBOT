SNBOT
=====

Microblogging / Social Network Botnet PoC

This is just a simple proof of concept, current weak spot in large botnets is to mantain a C&C, large bot nets will beheaded sooner or later, complex system like P2P require too much effort to work and could also be broken. The concep here is to use a messenger that just cannot be killed, a service millons of people is realing to work. Then use this service to send command to bots, and try be as low profile as possible.

Steps:
1.Client bot is running  (choose your own infection method)
2.a C&C is sync with client bots, so they now what would be the next #hashtag the client bot is going to search
2.b C&C create a new tweet with the given hashtag and wait for client bots to execute
3 Client boot waits for new commands when is a able to find a new command execute, and then continue polling for new commands.

Current implementation only echoes a base64 string when is properly attached to the hashtag, but imagine asymmetric encryption is in place, then we can asure we only execute commands from C&C.

Number of character ir very limited in twitter, a solution to this would be to point to a file in another server where the actual commands are.

#hashtag this is the key here, #hashtag provide a way to anynimously provide commands to all listen clients. But also we need to ensure that hashtag changes each certain time and also that is difficult to guess what would be the next itteration, a way to change the seed in the fly to further obfuscate bot behavior would be a huge improvment.

Any thoughts? feel free to ask at fdlanusse@gmail.com
