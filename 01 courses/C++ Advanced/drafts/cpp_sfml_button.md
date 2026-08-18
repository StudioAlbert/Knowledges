 intro, the needs
	1. graphics needs, 
		1. hoverable, on up , on down, on click
		2. use of vertices
	2. callbacks, solutions and drawbacks
		1. lambda
		2. std::function
			1. can not bind to a member
			2. Flexible but allocating - watch the `[STD]` guidelines on hot paths.