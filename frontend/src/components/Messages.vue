<script setup lang="ts">
    import type { Message } from '@/interfaces/message';
import { ref } from 'vue';
    defineProps<{
        messages: Message[]
    }>()
    const test = ref(['coisa 1', 'coisa 2'])
    console.log(test.value)
</script>
<template>
    <h1> teste </h1>
    <div v-for="m in messages">{{m.content}}</div>
</template>
<<<<<<< HEAD
<style scoped>
h2{
    background-color: red;
}
=======

<style scoped>
    

    @tailwind base;
    @tailwind components;
    @tailwind utilities;
>>>>>>> 11c551cbd29b7b14ae7731c5bf68c955e4833a58
</style>