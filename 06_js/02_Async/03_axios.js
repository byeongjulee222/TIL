const axios = require('axios');

axios.get('http://jsonplaceholder.typicode.com/posts')
  .then(response => {
     console.log(response)
  })
  // 요청이 잘못되었을 때
  .catch(error => {
    console.log(error)
  })
