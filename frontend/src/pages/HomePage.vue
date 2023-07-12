<template>
  <div :class="{'show-bg': showBG}" class="row full-height full-width justify-center items-center text-center bg-grey">
    <div class="column col-6 flex-brea">
      <ChatBox @jar="showBG = true" class="col-6"/>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue';
import ChatBox from '../components/ChatBox.vue'
  const showBG = ref(false)
</script>

<style scoped>
  .show-bg{
    background-image: url("jar.jpg") !important;
  }
</style>
