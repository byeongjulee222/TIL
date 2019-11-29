<template>
  <div id="app">
    <div id="nav">
      <div v-if="isLoggedIn">
        <!-- 라우터 링크로 연결하고 -->
        <router-link to="/">Home</router-link> |
        <a @click.prevent="logout" href="#">Logout</a>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <!-- 라우터 뷰로 보여준다 -->
    <div class="row justify-content-center">
      <router-view class="col-6"/>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'App',
    // data() {
    //   return {
    //     isAuthenticated: this.$session.has('jwt')
    //   }
    // },
    computed: {
      isLoggedIn: function() {
        return this.$store.getters.isLoggedIn
      }
    },
    // updated() {
    //   // DOM이 re-render될 때 다시 토큰의 존재 여부를 확인
    //   this.isAuthenticated = this.$session.has('jwt')
    // },
    methods: {
      logout() {
        // this.$session.destroy()
        this.$store.dispatch('logout')
        this.$router.push('/login')
      }
    }
  }
// updated
// 타입 : function
// 상세
// 데이터가 변경되어 DOM이 re-render 되고 patch되면 호출된다. (DOM 변화에 반응)
// DOM의 변화는 일반적으로 데이터의 변경에 의해 re-render되는 시점에 일어난다.
// 데이터의 변화(상태의 변화)에 반응하기 위해서는 computed 나 watch를 사용하는 것이 좋다.

// Vuex
// State 관리를 위해 탄생
// 컴포넌트 간의 통신 혹은 데이터 전달을 유기적을 ㅗ관리
// 컴포넌트 간의 통신 혹은 이벤트 등의 관계를 한 곳에서 관리하기 쉽게 구조화

// 현재 todo 프로젝트에서는 Auth 정보(로그인 혹은 로그아웃)은 django로 요청을 보낼 때
// 항상 필요하기 떄문에, 요청을 수행하는 모든 컴포넌트에서 알고 있어야 하고, 그 정보를
// 내가 필요한 순간에 활용할 수 있어야 한다.

// vuex는 vue-session의 대체가 아니고 서로 하는 일이 다르다.
// vuex는 메서드와 data의 대체라고 생각하자


</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
