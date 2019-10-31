const numbers = [1, 2, 3, 4,]

console.log(numbers[0])
console.log(numbers[-1]) // undefined : 정확한 양의 정수 index만 가능
console.log(numbers.length)

// 원본 파괴
console.log(numbers.reverse()) // [ 4, 3, 2, 1 ]
console.log(numbers) // [ 4, 3, 2, 1 ]
console.log(numbers.reverse()) // [ 1, 2, 3, 4 ]
console.log(numbers) // [ 1, 2, 3, 4 ]


// push - 값을 넣긴하는데, 배열의 길이를 return
console.log(numbers.push('a'))
console.log(numbers)


// pop - 배열의 가장 마지막 요소 제거 후 return
console.log(numbers.pop())
console.log(numbers)


// unshift - 배열의 가장 앞에 요소를 추가하고, 배열의 길이를 return
console.log(numbers.unshift('a'))
console.log(numbers)

// shift - 배열의 가장 앞에 요소를 제거 후 return
console.log(numbers.shift())
console.log(numbers)


// boolean return
console.log(numbers.includes(1))
console.log(numbers.includes(0))


console.log(numbers.push('a', 'a'))
console.log(numbers)
console.log(numbers.indexOf('a')) // 4 -> 중복이 존재한다면 처음 요소의 index를 return
console.log(numbers.indexOf('b'))


console.log(numbers.join()) // '1,2,3,4,a,a' -> 아무것도 넣지 않으면 ','를 기준으로 가져옴
console.log(numbers.join('')) // '1234aa'
console.log(numbers.join('-')) // '1-2-3-4-a-a'

console.log(numbers) // 원본은 변화하지 않음.
