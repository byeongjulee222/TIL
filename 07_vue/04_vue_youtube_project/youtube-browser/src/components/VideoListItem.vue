<template>
  <li @click="onVideoSelect" class="list-group-item">
    <!-- 미리 캐싱하여 오기 때문에 ()를 사용하지 않는다. -->
    <img :src="thumbnailUrl" alt="img">
    <!-- v-html=""로 하면 글자 그대로 받아오기 때문에 글자가 깨지지 않는다. -->
    <div class="media-body" v-html="video.snippet.title"></div>
  </li>
</template>

<script>
  export default {
    name: 'VideoListItem',
    props: {
      video: {
        type: Object,
        required: true,
      },
    },
    methods: {
      onVideoSelect() {
        // $emit(올릴 이름, 넘길 인자)
        this.$emit('videoSelect', this.video)
      }
    },
    // 데이터를 미리 캐싱하여 
    computed: {
      thumbnailUrl() {
        // 개발자도구 vue에서 타고 들어가는거 확인
        return this.video.snippet.thumbnails.default.url
      }
    },
  }
</script>

<style scoped>
  li {
    display: flex;
    cursor: pointer;
  }

  li:hover {
    background-color: gainsboro;
  }
</style>
