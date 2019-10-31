// Array Helper Method

// 1. forEach(callback())
// 주어진 callback을 배열에 있는 각 요소에 대해 오름차순으로 한 번씩 실행
// 아무것도 return 하지 않는다. (undefined)
// 콜백함수 - 인자로 다른 함수에 전달된 함수.

// ESS
var colors = ['red', 'blue', 'green']

for (var i = 0; i < colors.length; i++) {
  console.log(colors[i])
}

// ES6
const COLORS = ['red', 'blue', 'green']

COLORS.forEach(function (color){
  console.log(color)
})

COLORS.forEach( color => console.log(color) )

const result = COLORS.forEach( color => console.log(color) )
console.log(result)


// 1-1 연습
function handlePosts() {
  const posts = [
    { id: 23, title: 'News'},
    { id: 52, title: 'Code city'},
    { id: 102, title: 'Python'},
  ]
  // for (let i = 0; i < posts.length; i++) {
  //   console.log(posts[i])
  //   console.log(posts[i].id)
  //   console.log(posts[i].title)
  // }

  // 변수 선언이 필요없음
  posts.forEach(function (post){
    console.log(post)
    console.log(post.id)
    console.log(post.title)
  })
}

handlePosts()

//1-2 연습
const result2 = []

function cal() {
  const images = [
    { height: 10, width: 30 },
    { height: 20, width: 90 },
    { height: 54, width: 32 },
  ]

  images.forEach(function (image){
    result2.push(image.height * image.width)
  })
}

cal()
console.log(result2)


const areas = []

images.forEach(function (image){
  areas.push(image.height * image.width)
})
