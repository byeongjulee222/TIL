<template>
  <div id="app">
    <div id="nav">
      <!-- 라우터 링크로 연결하고 -->
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link>
    </div>
    <!-- 라우터 뷰로 보여준다 -->
    <div class="row justify-content-center">
      <router-view class="col-6"/>
    </div>
  </div>
</template>

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
