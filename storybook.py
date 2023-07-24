"""
As you are reading the book multiple times, you notice that you often get bad endings. You start to suspect there is no way to get to the good endings, so you decide to find out.

Good and bad endings will be separate lists of page numbers, like this:

good_endings = [10, 15, 25, 34]
bad_endings = [21, 30, 40]

Given lists of good endings, bad endings, and a list of the choices along with their options, return a collection of all the reachable good endings, if any.

Examples:

choices1 = [[3, 16, 24]]
find_good_endings(good_endings, bad_endings, choices1)
  Start: 1 -> 2 -> 3(choice) -> 16 -> 17... -> 21(bad ending)
                   |
                   -> 24 -> 25(good ending)
Thus it is possible to reach the good ending at 25 but no others, so we return [25].

choices2 = [[3, 16, 20]]
find_good_endings(good_endings, bad_endings, choices2)
  Start: 1 -> 2 -> 3(choice) -> 16 -> 17... -> 21(bad ending)
                   |
                   > 20 -> 21(bad ending)
No good ending is reachable, so return [].

choices3 = [[3, 16, 19], [20, 2, 17]]
find_good_endings(good_endings, bad_endings, choices3)
                                      +------<-------<----+
                                      v                   |
  Start: 1 -> 2 -> 3(choice) -> 16 -> 17 -> 18 -> 19 -> 20(choice)
              ^       |                           ^       |
              |       +----->------->------>------+       v
              +-------<--------<-------<-------<----------+
                                                
No good ending is reachable, so return [].

Additional Inputs:
choices4 = [[3, 2, 19], [20, 21, 34]]
choices5 = []
choices6 = [[9, 16, 26], [14, 16, 13], [27, 29, 28], [28, 15, 34], [29, 30, 38]]
choices7 = [[9, 16, 26], [13, 31, 14], [14, 16, 13], [27, 12, 24], [32, 34, 15]]
choices8 = [[3, 9, 10]]
choices9 = [[3, 9, 10], [12, 13, 14]]

Complexity Variable:
n = number of pages
(endings and choices are bound by the number of pages)

All Test Cases - snake_case:
find_good_endings(good_endings, bad_endings, choices1) => [25]
find_good_endings(good_endings, bad_endings, choices2) => []
find_good_endings(good_endings, bad_endings, choices3) => []
find_good_endings(good_endings, bad_endings, choices4) => [34]
find_good_endings(good_endings, bad_endings, choices5) => [10]
find_good_endings(good_endings, bad_endings, choices6) => [15, 34]
find_good_endings(good_endings, bad_endings, choices7) => [15, 25, 34]
find_good_endings(good_endings, bad_endings, choices8) => [10]
find_good_endings(good_endings, bad_endings, choices9) => [10]

All Test Cases - camelCase:
findGoodEndings(goodEndings, badEndings, choices1) => [25]
findGoodEndings(goodEndings, badEndings, choices2) => []
findGoodEndings(goodEndings, badEndings, choices3) => []
findGoodEndings(goodEndings, badEndings, choices4) => [34]
findGoodEndings(goodEndings, badEndings, choices5) => [10]
findGoodEndings(goodEndings, badEndings, choices6) => [15, 34]
findGoodEndings(goodEndings, badEndings, choices7) => [15, 25, 34]
findGoodEndings(goodEndings, badEndings, choices8) => [10]
findGoodEndings(goodEndings, badEndings, choices9) => [10]
"""

good_endings = [10, 15, 25, 34]
bad_endings = [21, 30, 40]

choices1 = [
    [3, 16, 24],
]
choices2 = [
    [3, 16, 20],
]
choices3 = [
    [3, 16, 19],
    [20, 2, 17],
]
choices4 = [
    [3, 2, 19],
    [20, 21, 34],
]
choices5 = []
choices6 = [
    [9, 16, 26],
    [14, 16, 13],
    [27, 29, 28],
    [28, 15, 34],
    [29, 30, 38],
]
choices7 = [
    [9, 16, 26],
    [13, 31, 14],
    [14, 16, 13],
    [27, 12, 24],
    [32, 34, 15],
]
choices8 = [
    [3, 9, 10],
]
choices9 = [
    [3, 9, 10],
    [12, 13, 14],
]

def stories(endings: [int], choices: [[int]], option: int) -> int:
    pages = set()
    page = 1
    currentPages = []
    for choice in choices:
        currentPages.append(choice[0])
    while(True):
        pages.add(page)
        if page in endings:
            return page
        if page in currentPages:
            for choice in choices:
                    if page == choice[0]:
                        page = choice[option]
                        if page in pages:
                            return -1
        else:
            page+=1

