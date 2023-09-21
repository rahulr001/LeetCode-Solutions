digits = "234"

Phone_map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def letterCombinations(digits: str):
    if len(digits) == 0 or digits == '1':
        return ''
    combinations = ['']
    for dig in digits:
        new_combinations = []
        for combination in combinations:
            for k in Phone_map[dig]:
                new_combinations.append(combination+k)
        combinations = new_combinations
    return combinations


print(letterCombinations(digits))
