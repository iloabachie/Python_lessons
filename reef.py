a = "1,2,3,4\na,b,c,d"
b = "1,'2,3',4"
c = "1,2,3\nmike,dyke,pike"
d = "'1.3','2.5',3,7\n'4.67',5,'9.0075'"


def twist(string):
    print(string)
    
    indices = []    
    for index, val in enumerate(string):
        if val in ["'", '"']:
            indices.append(index)
    print(1, indices)
    
    reps = []
    if "'" in string or '"' in string:
        for _ in range(0, len(indices), 2):
            string = string.replace((rep := string[indices[_]:indices[_+1]+1]), (z:="*"*len(rep)))  
            reps.append((rep, z))    
        print(2, reps)        
    string = string.split("\n")
    print(3, string)
    
    strings = []    
    for _ in string:
        strings.append(_.split(","))
        print(4, strings)    
    
    for index, val in enumerate(strings):        
        val[1], val[2] = val[2], val[1]
        strings[index] = ",".join(val)
        print(5, strings)
    
    # strings.reverse()
    print(6, strings)
    
    string = "\n".join(strings)
    if "*" in string:
        for rep, zz in reps:
            string = string.replace(zz, rep, 1)
    return string



print(twist(a+'\n'+b+'\n'+c+'\n'+d))
# print(twist(d))




class Solution:
    def maxConsecutiveAnswers(self, answerKey: str) -> int:
        streak = []
        count = 1
        for index, value in enumerate(answerKey):
            if index == 0:
                continue
            if value == answerKey[index-1]:
                count += 1
            else:
                streak.append(count)
                count = 1
        streak.append(count)
        print(streak)

        return sum(streak)


print(Solution().maxConsecutiveAnswers("TTFTTTTFTFFFT"))
