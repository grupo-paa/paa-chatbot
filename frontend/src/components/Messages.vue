<script setup lang="ts">
    import type { Message } from '@/interfaces/message';
    import MessageComponent from './MessageComponent.vue';
    defineProps<{
        messages: Message[]
    }>()
</script>
<template>
    <div class="block">
        <h1> teste </h1>
        <div v-for="m in messages"><MessageComponent :sent="m.sender != 'bot'" :message="m"/></div>
    </div>
</template>

<style scoped>
</style>