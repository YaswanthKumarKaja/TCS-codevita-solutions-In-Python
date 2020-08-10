'''CODU loves to play with string of brackets.

He considers string as a good string if it is balanced with stars. A string is considered as balanced with stars if string contains balanced brackets and between every pair of bracket i.e. between opening and closing brackets, there are at least 2 stars(*) present.

CODU knows how to check whether a string is balanced or not but this time he needs to keep a track of stars too. He decided to write a program to check whether a string is good or not. But CODU is not as good in programming as you are, so he decided to take help from you. Will you help him for this task? You need to print Yes and number of balanced pair if string satisfies following conditions(string is good if it satisfies following 2 conditions):

The string is balanced with respect to all brackets.
Between every pair of bracket there is at least two stars.
However if string doesn’t satisfies above conditions then print No and number of balanced pair in string as an output.

Constraints
4 <= String length <= 1000
Input Format
The first and only line of input contains a string of characters (a-z,A-Z), numbers(0-9), brackets( {, [, (, ), ], } ) and stars(*).

Output
Print space separated “Yes” (without quotes) and number of balanced pair if string is good. Else print “No” (without quotes) and number of balanced pair.

Test Case Explanation
Example 1

Input

{**}

Output

Yes 1

Explanation

Here string contains one balanced pair {} and between this pair of bracket there are 2 stars present so the output is Yes with the count of balanced pair as 1.


'''
star_stack=[]
bracket_stack=[]
loop_count=0




s=[x for x in input()]
bracket_count=0
status_flag=0
for i in s:
    if i=="{" or i=="[" or i=="(" :
        loop_count+=1
        bracket_stack.append(i)
        star_stack.append(0)
    elif i=="*":
        if loop_count>0:
            star_stack[-1]+=1
    elif i=="]" or i=="}" or i==")":
        if i=="}" and bracket_stack[-1]=="{":
            bracket_stack.pop()
            #bracket_count+=1
            loop_count-=1
            if star_stack[-1]<2:
                status_flag+=1
            else:
                bracket_count += 1
            if loop_count>0:
                temp=star_stack[-1]
                star_stack.pop()
                star_stack[-1]+=temp
            else:
                star_stack.pop()
        elif i=="]" and bracket_stack[-1]=="[":
            bracket_stack.pop()
            #bracket_count += 1
            loop_count -= 1
            if star_stack[-1] < 2:
                status_flag += 1
            else:
                bracket_count += 1
            if loop_count > 0:
                temp = star_stack[-1]
                star_stack.pop()
                star_stack[-1] += temp
            else:
                star_stack.pop()
        elif i==")" and bracket_stack[-1]=="(":
            bracket_stack.pop()
            #bracket_count += 1
            loop_count -= 1
            if star_stack[-1] < 2:
                status_flag += 1
            else:
                bracket_count += 1
            if loop_count > 0:
                temp = star_stack[-1]
                star_stack.pop()
                star_stack[-1] += temp
            else:
                star_stack.pop()
if status_flag==0  and len(bracket_stack)==0:
    print("Yes",bracket_count)
else:
    print("No",bracket_count)
