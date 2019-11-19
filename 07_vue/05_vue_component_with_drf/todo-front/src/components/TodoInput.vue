<template>
  <div class="todo-input">
    <form class="input-group" @submit.prevent="createTodo">
      <input type="text" class="form-control" v-model="title">
      <button type="submit" class="btn btn-primary mb-3">+</button>
    </form>

  </div>
</template>

<script>
  export default {
    name: 'TodoInput',
    data() {
      return {
        title: '',
      }
    },
    methods: {
      createTodo() {
        this.$emit('createTodo', this.title)
        this.title = ''
      }
    }
  }
</script>

<style>

</style>
