<template>
  <ul class="col-lg-4 list-group">
    <!-- :video="video" -> App.vue에서 받아오는 :video, for문 안의 video -->
    <video-list-item
      v-for="video in videos" 
      :key="video.etag" 
      :video="video"
      @videoSelect="onVideoSelect"
      >
    </video-list-item>
  </ul>
</template>

<script>
  import VideoListItem from './VideoListItem'
  export default {
    name: 'VideoList',
    components: {
      VideoListItem,
    },
    methods: {
      onVideoSelect(video) {
        // 'videoSelect'라는 이름으로 'video' 변수를 보냄
        this.$emit('videoSelect', video)
      }
    },
    props: {
      videos: {
        type: Array,
        required: true,
      },
    },
  }
</script>

<style>

</style>
