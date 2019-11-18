<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border text-primary" role="status">
      <!-- sr(screen reader) -->
      <span class="sr-only">Loading...</span>
    </div>
    <!-- <div v-else class="login-form"> -->
      <!-- @submit.prevent : 자동으로 새로고침 되는 것을 수정 -->
    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="alert alert-danger" role="alert">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>

      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input 
        type="text" 
        class="form-control" 
        id="id" 
        placeholder="아이디를 입력해주세요."
        v-model="credentials.username"
        >
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input 
        type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호를 입력해주세요."
        v-model="credentials.password"
        >
      </div>
      <!-- <button class="btn btn-primary" @click="login">로그인</button> -->
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'LoginForm',
    data() {
      return {
        // credentials : 로그인 정보 받아오는 곳
        credentials: {
          username: '',
          password: '',
        },
        loading: false,
        errors: [],
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          this.loading = true
          axios.get('http://127.0.0.1:8000', this.credentials)
          .then(res => {
            console.log(res)
          })
          .catch(err =>{
            console.log(err)
          })
        }
        else {
          console.log('로그인 검증 실패')
        }
      },
      checkForm() {
        this.errors = []
        // id가 없는 경우 에러 발생
        if (!this.credentials.username) {
          this.errors.push("아이디를 넣어줘ㅓㅓㅓ")
        }
        if (this.credentials.password.length < 8) {
          this.errors.push("비밀번호가 너무 짧아ㅏㅏㅏ")
        }
        if (this.errors.length == 0) {
          return true
        }
      }
    }
  }
</script>

<style>

</style>
