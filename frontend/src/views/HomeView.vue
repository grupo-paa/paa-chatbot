<template>
  <main>
    <TheWelcome />
    <h1>Aqui  </h1>
    <h1>{{ message }}</h1>
  </main>
</template>

<script setup lang="ts">
  import { ref } from 'vue';
  import axios from 'axios';

  const message = ref('');
  console.log("aqui")
  axios.get('http://localhost:5000/api/data')
    .then(response => {
      message.value = response.data.message;
    })
    .catch(error => {
      console.error(error);
    });

  const setup = () => {
    return {
      message
    };
  };
</script>
