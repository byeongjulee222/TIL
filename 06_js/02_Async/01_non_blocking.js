// const nothing = () => {
//   console.log('wait!!!')
// }

// console.log('Start')
// setTimeout(nothing, 3000)
// console.log('End')

// function sleep_3s() {
//   setTimeout(() => console.log('wake up'), 3000)
// }

// console.log('Start sleeping')
// sleep_3s()
// console.log('End of program')

// function first() {
//   console.log('first')
// }

// function second() {
//   console.log('second')
// }

// function third() {
//   console.log('third')
// }

// first()
// setTimeout(second, 1000)
// third()

// console.log('Hi')

// setTimeout(function ssafy() {
//   console.log('ssafy')
// }, 100)

// console.log('bye')


function printHello() {
  console.log('hello from baz')
}

function baz() {
  setTimeout(printHello, 3000)
}

function bar() {
  baz()
}

function foo() {
  bar()
}

foo()
//http://latentflip.com/loupe/?code=ZnVuY3Rpb24gcHJpbnRIZWxsbygpIHsNCiAgICBjb25zb2xlLmxvZygnSGVsbG8gZnJvbSBiYXonKTsNCn0NCg0KZnVuY3Rpb24gYmF6KCkgew0KICAgIHNldFRpbWVvdXQocHJpbnRIZWxsbywgMzAwMCk7DQp9DQoNCmZ1bmN0aW9uIGJhcigpIHsNCiAgICBiYXooKTsNCn0NCg0KZnVuY3Rpb24gZm9vKCkgew0KICAgIGJhcigpOw0KfQ0KDQpmb28oKTs%3D!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D
