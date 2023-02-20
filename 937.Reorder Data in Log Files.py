def reorderLogFiles(logs):
    let = []
    dig = []

    for log in logs:
        first = log.split(" ", 1)
        if first[1][0].isdigit():
            dig.append(log)
        else:
            let.append(log)

    let.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
    # let = sorted(let, key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))
    return let+dig


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs1 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

print(reorderLogFiles(logs1))