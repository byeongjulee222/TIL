console.log(a) // undefined
var a = 10 // 선언을 최상단으로 끌어올린다.
console.log(a)

// JS가 이해한 코드
// var 할당 과정
// 1. 선언 + 초기화
// 2. 할당
var a // 선언 + 초기화
console.log(a)
a = 10 // 할당
console.log(a)


// let은 안된다. ReferenceError
console.log(b)
let b = 15
console.log(b)

// 마찬가지로 아래와 같은 과정을 거친다
// JS가 이해한 코드
// 1. 선언
// 2. TDZ (임시 사각지대)
// 3. 초기화
// 4. 할당
let b // 선언 + TDZ
console.log(b)
let b = 15 // 할당 불가 (초기화가 아직 안됨)
console.log(b)
// 왜 안되지 ?




// JS가 이해한 코드
var x
var y
if (x === 1) {
  console.log(y) // undefined
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) // 3
}

if (x === 1) {
  console.log(y)
}
