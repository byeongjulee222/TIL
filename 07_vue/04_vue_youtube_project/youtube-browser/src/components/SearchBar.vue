<template>
  <div>
    <!-- @change: 엔터쳤을 때 검색되도록 -->
    <input @change="onInput" type="text">
  </div>
</template>
<script>
  export default {
    name: 'SearchBar',
    methods: {
      onInput(e) {
      //  데이터 보내기 $emit('이벤트 이름', '인자')
       this.$emit('inputChange', e.target.value)
      }
    }
  }
</script>


<style scoped>
/* scoped : 이 vue 파일에만 스타일을 적용하겠다 */
  input {
    width: 75%;
  }

  div {
    text-align: center;
    margin: 20px;
  }
</style>
