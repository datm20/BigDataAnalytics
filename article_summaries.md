Authors of all articles: Connie U. Smith and Lloyd G. Williams

# Software Performance AntiPatterns
**What is the article about?** The authors explore four software performance antipatterns, how they impact performance, as well as how to detect and how to correct them. 

**What have they measured?** The authors did not conduct any practical measurements, the performance impacts they discuss are purely theoretical. For one antipattern they show the increase in system messages caused by the antipattern, for another, they showed the theoretical response time increase from using it. 

**What are their main findings?** They found that these antipatterns can indeed have performance impacts in addition to previously identified problems. They also provide good examples on how to mitigate these antipatterns.

**What can you learn from this article?** This article has taught us how to spot antipatterns that can have negative consequences on performance and how to correct them using other patterns.


# New Software Performance AntiPatterns: More Ways to Shoot Yourself in the Foot

**What is the article about?** The article documents four software performance antipatterns that degrade system responsiveness, throughput and scalability. 

**What have they measured?** The article does not publish any empirical measurements or practical experiments as some of the antipatterns are only relevant in certain settings. They did look at how Response Time, Processing time and Throughput can affect the different antipatterns. For example it depends on how a program is expected to run, if a program is expected to run thousands or even million times a day, then response time and latency is everything. However if the program is expected to run once or twice a day or even less, then it really doesn’t matter if the program takes an hour or so. In short, all the different possible measurements mean little compared to how often the program is expected to run. 

**What are their main findings?** The article found four antipatterns and they are the following; 
Unbalanced Processing - When a program or part of a program cannot get access to available processors or other computer resources. Can also be because a part of a program is doing all the heavy lifting and blocks other processes of the program while working. 
Unnecessary Processing - This occurs when processing is not needed or not needed at that time. 
The Ramp - This is the increase of processing time for a system as it is used. Can come from data structures or other data storage that is ever expanding and causes the program to parse long data structures and that can take time. 
More is Less - Occurs when a system has too many processes running at the same time relative to the available resources and this causes the system to “thrash” rather than accomplishing work.

**What can you learn from this article?** You can learn to recognize self-inflicting issues within the code by balancing workload, eliminate/restructure unwanted/unneeded processing steps, use scalable algorithms for data growth and deploy resources so it can meet performance while under thrashing threshold. 


# More New Software Performance AntiPatterns: Even More Ways to Shoot Yourself in the Foot

**What is the article about?** The dynamic duo bring further antipatterns to light and explain how they might impact performance negatively. This report discusses Falling Dominoes, Empty Semi Trucks, and Tower of Babel. 

**What have they measured?** The authors have calculated the theoretical performance impact of implementing each antipattern and shown how the amount of useful work is reduced by unnecessary work.

**What are their main findings?** Falling Dominoes is an antipattern that results in one small failure possibly bringing down the whole system. Depending on the rate of failure, the problem can propagate rapidly through the system. The Empty Semi Trucks antipattern results in reduced performance due to wasted bandwidth with every message. The Roundtrip antipattern results in many tiny and synchronous messages instead of a few larger ones. The Tower of Babel antipattern involves having different parts of a system using different protocols or data formats, like JSON and XML, and needing to translate between them constantly, reducing the amount of useful work performed.

**What can you learn from this article?** Make sure that broken pieces are isolated until restored or repaired and the system should have some redundancy. Batch requests were possible to combine items to better use the available bandwidth. Minimize conversion, parsing and translation between different protocols and data formats. 
