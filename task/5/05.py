## 기존 데이터
plt.scatter(dach_length, dach_height, c='red', label='Dachshund')
plt.scatter(samo_length, samo_height, c='blue', marker='^', label='Samoyed')
plt.scatter(mal_length, mal_height, c='green', marker='s', label='Maltese')

## 새로운 데이터
plt.scatter(newdata1[0][0:1], newdata1[0][1:2], s=250, c='purple', label='A')
plt.scatter(newdata2[0][0:1], newdata2[0][1:2], s=250, c='grey', label='B')
plt.scatter(newdata3[0][0:1], newdata3[0][1:2], s=250, c='skyblue', label='C')
plt.scatter(newdata4[0][0:1], newdata4[0][1:2], s=250, c='darkgreen', label='D')

## plt로 나타내기
plt.xlabel('Length')
plt.ylabel('Height')
plt.title('Dog size')
plt.legend(loc='upper left')

plt.show()
