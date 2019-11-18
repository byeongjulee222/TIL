<template>
  <div>
    <LoginForm/>
  </div>
</template>

<script>
// @ 는 /src의 alias(shortcut)
  // import LoginForm from '../components/LoginForm.vue'
  // 보통 상대경로말고 절대경로를 사용한다.
  import LoginForm from '@/components/LoginForm.vue'

  export default {
    name: 'login',
    components: {
      LoginForm,
    }
    
  }
</script>

<style>

</style>
