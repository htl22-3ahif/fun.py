# What is fun?

This project called fun has the goal to be a server sided application for storing real time information about a game. At example the position of a player. The most common consequence is a multiplayer game, but in can also result in many other things.

# The Node Model

The system's core is the node model. Every "thing" in a game has information. And for every "thing" you want the informations of to be shared on a server, you can create a representative for it. We call it node. In that node, you cande fine every kind of information it has to hold. The client only has to send the informations, fun will handle them and store them in its node.

But merely storing things would be lame. You are also allowed to process this informations on the server, and send them back to the client. This gives you the ability to control the informations on your server or shift the calculations of risky game parts on the server. You never know if you can trust your client.

An other usage would be everything, where a database would be too slow. Like in a database (where you define entites), you define nodes, and the framework will keep it fast.

# Communication

We are not entirely sure how the communication will look like. It will most likely follow the REST psychology, but we are thinking to also do some SOAP stuff.
