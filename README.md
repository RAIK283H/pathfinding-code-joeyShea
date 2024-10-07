CODE OFTEN CRASHES WHEN THE EXTRA CREDIT GRAPH IS REACHED DUE TO IT TAKING TOO LONG. TRY 3-4 TIMES!!!

My random pathing function is quite simple. It looks at all the possible next moves, and picks one. It repeats until the target has
been found, then tries to find the exit. I decided that it would be fine for the player to return to the start before it completes,
but the algorithm does not allow the player to enter the exit node at all until the target has been hit. In the spirit of true
randomness, the player is able to wander between nodes, sometimes causing loops that go on for quite a while. If you wanted to avoid these loops,
you could simply keep track of the nodes that have been visited multiple times already and avoid those in favor of new nodes to optimize the
random exploration.

I decided to add a "Nodes visited" counter in the statistic section. I thought that this would be useful to look at as the player
moves around. You can technically look at the length of the path list that is already displayed, but this often gets cut off for larger graphs and is
not very user friendly. If a side-by-side view of two algorithms was ever implemented, it would also be very useful to see not only how far each
algorithm travels, but how quickly it finds a new node.
