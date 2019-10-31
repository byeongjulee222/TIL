const a = 13
const b = -3
const c = 3.14 // float
const d = 2.998e8 // 2.998 * 10^8 == 299,800,000
const e = Infinity
const f = -Infinity
const g = NaN

console.log(a, b, c, d, e, f, g)

// 문자열
const sentence1 = 'sentence'
const sentence2 = "sentence"
const sentence3 = `sentence`

// backtick
// const word = "안녕
// 하세요"
// console.log(word)

const word1 = "안녕 \n하세요"
console.log(word1)

// Template Literal
// JS에서 문자열을 입력하는 방식.
const age = 10
const message = `홍길동은 ${age}
세 입니다.`
console.log(message)

// // room 변수를 가리키는 식별자 / 'conference_room'(따옴표 안)은 리터럴
// let room = 'conference_room'

// let hotelRoom = room // 에러, conference_room 식별자는 존재하지 않는다.
// hotelRoom = comference_room

const happy = 'hello'
const hacking = 'world' + ' lol' + '!!!'
console.log(happy, hacking)

let c = 0 // undefined
c // 0
c += 10 // 10
console.log(c) // 10
c -= 3 // 7
c *= 10 // 70
c++ // 70
c // 71

'A' < 'B' // true
'A' < 'a' // true
'A' > 'a' // false

a = 3 // 3
const a = 1 // undefined
const b = '1' // undefined
a == b // true
a === b // false
a !== b // true
a === Number(b) // true

true && true // true
true && false // false
0 && 1 // 0
4 && 7 // 7 , 뒤쪽까지 판단
false || true // true
false || false // false
1 || 0 // 1
4 || 7 // 4 , 앞에가 true면 뒤까지 안본다.

// 3항 연산자
true ? 1 : 2 // 1, true면 앞
false ? 1 : 2 // 2, false면 뒤

const result = Math.PI > 4 ? 'yes' : 'no'
console.log(result) // no


