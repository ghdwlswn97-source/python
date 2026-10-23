# *args => 튜플로 반환
# def average(*scores):
#      return sum(scores) / len(scores)


# **kwargs => 딕셔너리로 반환
# {key:value, key:value}
# {kor:90, eng:89,...}
def average(**scores):
    total =0
    for subject, score in scores.items():
        print(f'{subject} : {score}점')
        total += score

    return total / len(scores)


    # sum(scores)
    # avg= sum(scores)/len(args)
    # score.name = name

    # print(f'{name}의 평균 : {avg}')
    

    





