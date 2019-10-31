// 조건문 & 반복문
// if
const userName = prompt('Hello! who r u ??') // juya

switch (userName) {
  case '1q2w3e4r': {
    message = '<h1>This is admin</h1>'
    console.log(message)
  }
  case 'ssafy': {
    message = '<h1>U r ssafy</h1>'
    console.log(message)
  }
  default: {
    message = `<h1>hello ${userName}</h1>`
    console.log(message)
  }
}

{
  /* <h1>This is admin</h1>
  <h1>U r ssafy</h1>
  <h1>hello 1q2w3e4r</h1> */
}

// switch
switch (userName) {
  case '1q2w3e4r': {
    message = '<h1>This is admin</h1>'
    break
  }
  case 'ssafy': {
    message = '<h1>U r ssafy</h1>'
    break
  }
  default: {
    message = `<h1>hello ${userName}</h1>`
    console.log(message)
  }
}

{
  /* <h1>This is admin</h1> */ }
