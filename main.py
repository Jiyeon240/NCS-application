import numpy as np

items = [40,7,99,-3]

scores = np.array([
    [80,100,90]
    [80,75,95]
    [80,99,87]
])

print(f"전체 평균 : {np.means(scores)}")
print(f"국 영 수 과목별 평균 : {np.mean(scores, axis=0)}")
#axis =0 열별 평균

print(f"a학생, b학생, c학생 최고점수 : {np.max(scores, axis=1)}")