Topic:
Time Complexity

Important Points

• O(1) → Constant
• O(log n) → Binary Search
• O(n) → Single Loop
• O(n²) → Nested Loops

Remember

One Loop → O(n)

Nested Loop → O(n²)

Three Loops → O(n³)


DSA-la Fast → Slow order-la Time Complexity:

Rank	Time Complexity	         Speed	            Example
🥇 1	O(1)	            ⚡ Fastest          Array index access
🥈 2	O(log n)	         Very Fast          Binary Search
🥉 3	O(n)	             Fast	            Linear Search, Finding Min/Max
4	    O(n log n)	         Good	             Merge Sort, Quick Sort (Average)
5	    O(n²)	             Slow	             Bubble Sort, Selection Sort
6	    O(n³)	             Very Slow	         Triple nested loops
7   	O(2ⁿ)	             Extremely Slow 	 Recursive Fibonacci
8	    O(n!)	             🚨 Slowest	         Permutations, Traveling Salesman (Brute Force)


O(1)
   ↓
O(log n)
   ↓
O(n)
   ↓
O(n log n)
   ↓
O(n²)
   ↓
O(n³)
   ↓
O(2ⁿ)
   ↓
O(n!)






Interview Tip

Good Complexities ✅

O(1)
O(log n)
O(n)
O(n log n)

Avoid if possible ❌

O(n²)
O(n³)
O(2ⁿ)
O(n!)





🔥 Easy Tricks to Remember
Pattern	                        Time Complexity
for i in range(n)	                O(n)
Two nested for loops	            O(n²)
Three nested for loops	            O(n³)
i *= 2	                            O(log n)
i //= 2	                            O(log n)
for(n) + while(log n)	            O(n log n)
while(log n) + while(log n)	        O((log n)²)
n + n/2 + n/4 + ...	                O(n)


🎯 Important Pattern

Indha pattern-a nalla nyabagam vechiko:

Pattern                                 	Complexity
for(n)	                                      O(n)
for(n) + for(n)	                              O(n²)
for(n) + for(n) + while(log n)             	  O(n² log n)
for(n) + while(log n)	                      O(n log n)
while(log n) + while(log n)	                  O((log n)²)
1 + 2 + 4 + ... + n	                          O(n)
n + n/2 + n/4 + ...	                          O(n)