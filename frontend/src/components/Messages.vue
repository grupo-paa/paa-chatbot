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
<style scoped>
h2{
    background-color: red;
}
</style>