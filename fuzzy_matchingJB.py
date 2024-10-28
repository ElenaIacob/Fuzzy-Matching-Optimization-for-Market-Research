from typing import List

def levenshtein(first_string, second_string):
    len_first = len(first_string)
    len_second = len(second_string)
    
    dp = [[0] * (len_second + 1) for _ in range(len_first + 1)]
    for i in range(len_first + 1):
        dp[i][0] = i
    for j in range(len_second + 1):
        dp[0][j] = j
    
    for i in range(1, len_first + 1):
        for j in range(1, len_second + 1):
            if first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] 
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],   
                    dp[i][j - 1],    
                    dp[i - 1][j - 1] 
                )
                
    return dp[len_first][len_second]

def similarity_score(first_string, second_string):
    len_first = len(first_string)
    len_second = len(second_string)
    distance = levenshtein(first_string, second_string)
    score = 1 - (distance / max(len_first, len_second))
    return score


list_A: List[str] = ["Apple Inc.", "Microsoft Corporation", "International Business Machines"]
list_B: List[str] = ["Apple", "AAPL" "Apple Incorporated", "Microsoft Corp.", "Microsoft Co.",
"Microsoft Azure","Microsoft Office","IBM", "Int'l Bus. Machines", "IBMachines", "MSFT",
"MSoft Corp", "Microsoft, Inc", "Apple Co", "Apple Corp", "Apl Inc"]


results_0 = {}
results_1 = {}
results_2 = {}

for index, company in enumerate(list_B):
    score_0 = similarity_score(list_A[0], company)
    score_1 = similarity_score(list_A[1], company)
    score_2 = similarity_score(list_A[2], company)
    results_0[f"{company}"] = score_0
    results_1[f"{company}"] = score_1
    results_2[f"{company}"] = score_2


sorted_results_0 = sorted(results_0.items(), key=lambda x: x[1], reverse=True)
sorted_results_1 = sorted(results_1.items(), key=lambda x: x[1], reverse=True)
sorted_results_2 = sorted(results_2.items(), key=lambda x: x[1], reverse=True)

print(f"Best match for {list_A[0]} is", sorted_results_0[0][0], f"with a similarity score of {sorted_results_0[0][1]}")
print(f"Best match for {list_A[1]} is", sorted_results_1[0][0], f"with a similarity score of {sorted_results_1[0][1]}")
print(f"Best match for {list_A[2]} is", sorted_results_2[0][0], f"with a similarity score of {sorted_results_2[0][1]}")
