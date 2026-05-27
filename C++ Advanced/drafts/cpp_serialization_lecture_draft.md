___
Structure
# What is serializing ?

### What’s this “serialization” thing all about? [](https://isocpp.org/wiki/faq/serialization#serialize-overview "Permalink to this FAQ") [](https://isocpp.org/wiki/faq/serialization# "Recommend an improvement to this FAQ")

It lets you take an object or group of objects, put them on a disk or send them through a wire or wireless transport mechanism, then later, perhaps on another computer, reverse the process: resurrect the original object(s). The basic mechanisms are to flatten object(s) into a one-dimensional stream of bits, and to turn that stream of bits back into the original object(s).

Like the Transporter on Star Trek, it’s all about taking something complicated and turning it into a flat sequence of 1s and 0s, then taking that sequence of 1s and 0s (possibly at another place, possibly at another time) and reconstructing the original complicated “something.”

source : https://isocpp.org/wiki/faq/serialization
# Why Serializing ?

## use cases
- Saving
- transmitting

# Text vs Binary

- Sources :
	- https://isocpp.org/wiki/faq/serialization#serialize-selection

# Solution 1 : reinterpret cast

# Solution 2 : Boost 

https://www.boost.org/doc/libs/1_36_0/libs/serialization/doc/index.html

https://www.boost.org/doc/libs/1_36_0/libs/serialization/example/demo.cpp

# Solution 3 : Visitor pattern

## Visitor pattern presentation

conversation claude : https://claude.ai/share/d528fed0-bbdd-46f5-afa7-9703b34c4c4b

## Practical use case : serializing tilemap




---
Sources
https://www.cs.sjsu.edu/faculty/pearce/modules/lectures/cpp/advanced/Serialization.htm

https://www.boost.org/doc/libs/1_36_0/libs/serialization/doc/index.html

https://www.boost.org/doc/libs/1_36_0/libs/serialization/example/demo.cpp

https://isocpp.org/wiki/faq/serialization

https://github.com/CppCon/CppCon2022/blob/main/Presentations/A-Faster-Serialization-Library-Based-on-Compile-time-Reflection-and-C-20-Yu-Qi-CppCon-2022.pdf

https://github.com/CppCon/CppCon2022/blob/main/Presentations/Killing-C%2B%2B-Serialization-Overhead-%26-Complexity-EyalZedaka.pdf