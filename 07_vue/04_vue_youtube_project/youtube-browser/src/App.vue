<template>
 <div id="app">
   <!-- 만약 inputChange 이벤트가 일어나면 onInputChange 라는 method가 실행됨 -->
   <search-bar @inputChange="onInputChange"></search-bar>
   <div class="row">
   <video-detail :video="selectedVideo"></video-detail>
   <!-- VideoList로 내려줄 때 v-bind로 props에 넣을 key값 설정 (=videos에서 videos는 데이터가 들어간 Array) -->
   <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
   </div>
 </div>
</template>
<script>
  import axios from 'axios'
  import SearchBar from './components/SearchBar'
  import VideoList from './components/VideoList'
  import VideoDetail from './components/VideoDetail'
  const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'



  export default {
    name: 'App',  // 최상단 컴포넌트기 때문에 이름이 없어도 되지만 명시적으로 작성한다.
    data() {
      // object를 return하는 함수라 생각
      // 주의사항: 컴포넌트 내에서 데이터를 보내줄 때 
      // return 뒤에 {}로 한 번 더 감싸줘야함(name space 개념과 비슷)
      return {
        videos: [],
        // 선택된 비디오를 넣을 값 지정
        selectedVideo: null,
      }
    },
    components: {
      SearchBar,
      VideoList,
      VideoDetail,
    },
    methods: {
      onVideoSelect(video) {
        // 비디오를 넣음
        this.selectedVideo = video
      },
      //  inputValue : $emit에서 온 e.target.value
      onInputChange(inputValue) {
        //  받은 데이터 뜨는지 콘솔창에서 확인
        //  console.log(inputValue)
        axios.get(API_URL, {
          params: {
            key: API_KEY,
            type: 'video',
            part: 'snippet',
            // url에서 검색어 앞에 붙는거(?q='검색어')
            q: inputValue,
          }
        })
        // 함수내의 함수이기 때문에 반드시 Arrow Function 사용
        .then(response => {
          // 콘솔에서 확인하고 작성
          this.videos = response.data.items
        })
        .catch(error => {
          console.log(error)
        })
      }
    },
  }
</script>
<style>
</style>
