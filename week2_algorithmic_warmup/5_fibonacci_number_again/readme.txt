In this problem, your goal is to compute 𝐹𝑛 modulo 𝑚, where 𝑛 may be really huge: up to 1014. For such
values of 𝑛, an algorithm looping for 𝑛 iterations will not fit into one second for sure. Therefore we need to
avoid such a loop.
To get an idea how to solve this problem without going through all 𝐹𝑖 for 𝑖 from 0 to 𝑛, let’s see what
happens when 𝑚 is small — say, 𝑚 = 2 or 𝑚 = 3.